# Author: Lila Morgen
# ProjectName: test
# FileName: demo.py
# Date: 2020/11/26
# Description:

import plotly.graph_objects as go
from plotly import express

import dash
import dash_core_components as dcc
import dash_html_components as html


# fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
# # fig.show()
# fig.write_html('first_figure.html', auto_open=True)

fig = express.line(x=['a', 'b', 'c'], y=[1, 3, 2], title='simple-figure')
# print(fig)
# fig.show()

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])
app.run_server(debug=True, use_reloader=False)
