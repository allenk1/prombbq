import json
import time

from igrill import IGrillV2Peripheral

import logging
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

ADDRESS = '70:91:8F:1A:53:C7'
DATA_FILE = '/tmp/igrill.json'
INTERVAL = 1

if __name__ == '__main__':

    periph = IGrillV2Peripheral(ADDRESS)

    while True:

        sensor_data = {
            'temperature': periph.read_temperature(False, 0),
            'battery': periph.read_battery(),
        }

        print('Writing sensor data: {}'.format(sensor_data))
        with open(DATA_FILE, 'w') as f:
            f.write(json.dumps(sensor_data))

        time.sleep(INTERVAL)
