#!/usr/bin/env python3
import pyowm
import time
import config
from datetime import datetime
from w1thermsensor import W1ThermSensor
import plotly
import plotly.graph_objs as go
import pandas as pd

# my API code
connect(cfg.mysql["host"], cfg.mysql["user"], cfg.mysql["password"])

owm = pyowm.OWM(config.keys["pyowmapikey"])
sensor = W1ThermSensor()
plotly.tools.set_credentials_file(username=config.keys["plotlylogin"], api_key=config.keys["plotlyapikey"])

tempLog = open('orinda-upstairs-templog.txt', 'a')
fahrenheitTemp = sensor.get_temperature(W1ThermSensor.DEGREES_F)

# this city ID is for Orinda, CA (USA)
observation = owm.weather_at_id(5379678)
w = observation.get_weather()
outsideTemp = w.get_temperature('fahrenheit')

# make into a csv file so can eventually graph it.  format: time,weather temp, probe temp
tempLog.write(datetime.now().strftime('%Y-%m-%d %H:%M') + ',')
tempLog.write(str(outsideTemp['temp_max']) + ',')
tempLog.write(str(format(fahrenheitTemp, '.2f')) + '\n')
# tempLog.write(str(format(fahrenheitTemp[1], '.2f')) + ' F\n')

print("time, weather temp, probe temp")
print(datetime.now().strftime('%Y-%m-%d %H:%M') + ',' + str(outsideTemp['temp_max']) + ' F,' + str(
    format(fahrenheitTemp, '.2f')) + ' F')
tempLog.close()

df = pd.read_csv('orinda-upstairs-templog.txt')
weatherTrace = go.Scatter(
    x=df['time'],
    y=df['weather'],
    mode='lines',
    name='Weather'
)

probeTrace = go.Scatter(
    x=df['time'],
    y=df['probe'],
    mode='lines',
    name='Probe'
)
data = [weatherTrace, probeTrace]

plotly.offline.plot({
    "data": data,
    "layout": go.Layout(title="Hydro")
}, auto_open=False)
# plotly.plotly.plot(data, filename='temp-line', auto_open=False, fileopt='overwrite')
