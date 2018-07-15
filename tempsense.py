#!/usr/bin/env python3
import os
import pyowm
import time
from datetime import datetime

from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()
temperature_in_fahrenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)
print(temperature_in_fahrenheit)


def loop(ds18b20):
    while True:
        if read(ds18b20) != None:
            tempLog = open('/home/pi/templog.txt', 'a')
            fahrenheitTemp = sensor.get_temperature(W1ThermSensor.DEGREES_F)

            # fahrenheitTemp = read(ds18b20)
            # this city ID is for Concord, CA (USA) - concord, ca will give Canada
            observation = owm.weather_at_id(5339111)
            w = observation.get_weather()
            outsideTemp = w.get_temperature('fahrenheit')

            # make into a csv file so can eventually graph it.  format: time,weather temp, probe temp
            tempLog.write(datetime.now().strftime('%Y-%m-%d %H:%M') + ',')
            tempLog.write(str(outsideTemp['temp_max']) + ' F,')
            tempLog.write(str(fahrenheitTemp) + '\n')
            #tempLog.write(str(format(fahrenheitTemp[1], '.2f')) + ' F\n')
            print("time, weather temp, probe temp")
            print(datetime.now().strftime('%Y-%m-%d %H:%M') + ',' + str(outsideTemp['temp_max']) + ' F,' + str(
                fahrenheitTemp) + ' F')
            tempLog.close()
            time.sleep(1800)


def kill():
    quit()


if __name__ == '__main__':
    try:
        serialNum = sensor()
        loop(serialNum)
    except KeyboardInterrupt:
        kill()
