#!/usr/bin/env python3
import pyowm
import time
from datetime import datetime
from w1thermsensor import W1ThermSensor
import pandas as pd


# my API code
owm = pyowm.OWM('29186bf4c93a1c8c48837b56de4749e7')
sensor = W1ThermSensor()

def loop(ds18b20):
    while True:
        if ds18b20 != None:
            tempLog = open('/home/pi/templog.txt', 'a')
            fahrenheitTemp = sensor.get_temperature(W1ThermSensor.DEGREES_F)

            # this city ID is for Concord, CA (USA) - concord, ca will give Canada
            observation = owm.weather_at_id(5339111)
            w = observation.get_weather()
            outsideTemp = w.get_temperature('fahrenheit')

            # make into a csv file so can eventually graph it.  format: time,weather temp, probe temp
            tempLog.write(datetime.now().strftime('%Y-%m-%d %H:%M') + ',')
            tempLog.write(str(outsideTemp['temp_max']) + ' F,')
            tempLog.write(str(format(fahrenheitTemp, '.2f')) + ' F\n')
            #tempLog.write(str(format(fahrenheitTemp[1], '.2f')) + ' F\n')
            print("time, weather temp, probe temp")
            print(datetime.now().strftime('%Y-%m-%d %H:%M') + ',' + str(outsideTemp['temp_max']) + ' F,' + str(
                format(fahrenheitTemp, '.2f')) + ' F')
            tempLog.close()
            time.sleep(1800)

def kill():
    quit()

if __name__ == '__main__':
    try:
        serialNum = sensor
        loop(serialNum)
    except KeyboardInterrupt:
        kill()