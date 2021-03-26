#!/usr/bin/env python
import bluepy.btle as btle

#Delegate methods
class ReadDelegate(btle.DefaultDelegate):
    def handleNotification(self, cHandle, data):
        print("Here is the data...")
        print(data)

#Create peripheral, connect, services and write...
p = btle.Peripheral('70:91:8F:1A:53:C7', "random")