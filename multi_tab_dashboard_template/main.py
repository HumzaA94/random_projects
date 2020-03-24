from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import flask
import pandas as pd
from tabs import dropdown_tab,datatable_tab
from tabs import tab_functions as tf
from app import app
import callback_functions

app.layout = html.Div([
    dcc.Tabs(id="tabs-example", value='tab-1-example', children=[
        dcc.Tab(label='Tab One', value='tab-1-example'),
        dcc.Tab(label='Tab Two', value='tab-2-example'),
    ]),
    html.Div(id='tabs-content-example')
])


if __name__ == '__main__':
    app.run_server(debug=True) #this line of code will keep your dashboard private, comment the line below
    #app.run_server(debug=False,host="0.0.0.0",port=8049) #this line of code lets you share it with others
                                                        # if you give your IP address with it -> IP_address:8049
