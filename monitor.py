import time
import os
import urllib

from igrill import IGrillV2Peripheral

from prometheus_client import Gauge, push_to_gateway, CollectorRegistry
from prometheus_client.exposition import basic_auth_handler

import logging
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

ADDRESS = '70:91:8F:1A:53:C7'
DATA_FILE = '/tmp/igrill.json'
INTERVAL = 1
PUSHGATEWAY = os.environ['PROMBBQ_PUSHSERVER']

# Prometheus Setup
registry = CollectorRegistry()
probe_one = Gauge('bbq_probe_one_temp', 'Temp of probe one', registry=registry)
probe_two = Gauge('bbq_probe_two_temp', 'Temp of probe two', registry=registry)
probe_three = Gauge('bbq_probe_three_temp', 'Temp of probe three', registry=registry)
probe_four = Gauge('bbq_probe_four_temp', 'Temp of probe four', registry=registry)
battery = Gauge('bbq_battery', 'Battery of the iGrill', registry=registry)

def promAuthHandler(url, method, timeout, headers, data):
    user=os.environ['PROMBBQ_BASIC_AUTH_USER']
    passwd=os.environ['PROMBBQ_BASIC_AUTH_PASSSWORD']
    return basic_auth_handler(url, method, timeout, headers, data, user, passwd)


if __name__ == '__main__':

    periph = IGrillV2Peripheral(ADDRESS)

    while True:
        temps = periph.read_temperature(False, 0)
        batt = periph.read_battery()

        i=1
        for index, temp in temps.items():
            if temp != 63536.0:
                print("bbq/probe{} - {}".format(i, temp))
                if i == 1:
                    probe_one.set(temp)
                if i == 2:
                    probe_two.set(temp)
                if i == 3:
                    probe_three.set(temp)
                if i == 4:
                    probe_four.set(temp)
            i+=1

        print("bbq/battery - {}%".format(batt))
        battery.set(batt)

        push_to_gateway(PUSHGATEWAY, job='prombbq', registry=registry, handler=promAuthHandler)
        time.sleep(INTERVAL)
