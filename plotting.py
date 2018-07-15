#!/usr/bin/env python3
# https://plot.ly/python/

import os
import plotly
import plotly.graph_objs as go
import pandas as pd

plotly.tools.set_credentials_file(username='daw007', api_key='FzbP6kHpdwPM4DLJsOjQ')
df = pd.read_csv('templog2.txt')

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
plotly.plotly.plot(data, filename='basic-line', auto_open=True)

# print(df['weather'])
# plotly.offline.plot({
#     "data": data,
#     "layout": go.Layout(title="Hydro")
# }, auto_open=True)
