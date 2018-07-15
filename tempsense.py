#!/usr/bin/env python3
import os
import pyowm
import time
from datetime import datetime

owm = pyowm.OWM('29186bf4c93a1c8c48837b56de4749e7')


def sensor():
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i
    return ds18b20


def read(ds18b20):
    location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    farenheit = (celsius * 1.8) + 32
    return celsius, farenheit


def loop(ds18b20):
    while True:
        if read(ds18b20) != None:
            tempLog = open('/home/pi/templog.txt', 'a')
            fahrenheitTemp = read(ds18b20)
            # this city ID is for Concord, CA (USA) - concord, ca will give Canada
            observation = owm.weather_at_id(5339111)
            w = observation.get_weather()
            outsideTemp = w.get_temperature('fahrenheit')

            # make into a csv file so can eventually graph it.  format: time,weather temp, probe temp
            tempLog.write(datetime.now().strftime('%Y-%m-%d %H:%M') + ',')
            tempLog.write(str(outsideTemp['temp_max']) + ' F,')
            tempLog.write(str(format(fahrenheitTemp[1], '.2f')) + ' F\n')
            print("time, weather temp, probe temp")
            print(datetime.now().strftime('%Y-%m-%d %H:%M') + ',' + str(outsideTemp['temp_max']) + ' F,' + str(
                format(fahrenheitTemp[1], '.2f')) + ' F')
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
