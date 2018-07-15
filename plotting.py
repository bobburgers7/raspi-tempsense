#!/usr/bin/env python3
# https://plot.ly/python/

import plotly
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('templog.txt')
print(df)
# plotly.offline.plot({
#     "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
#     "layout": go.Layout(title="hello world")
# }, auto_open=True)
