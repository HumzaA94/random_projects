import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import  plotly.graph_objs as go
from tabs import tab_functions as tf
import flask

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
continent = df['continent'].unique()
continent = sorted(continent,reverse=False)

tab_1_layout = html.Div(
    id="app-container",
    children=[
        html.Br(),
        tf.single_value_dropdown("single-dropdown-container","continent-dropdown","Continent Selection",continent),
        tf.multi_value_dropdown('multi-dropdown',"Continent selections",continent),
        dcc.Interval(id="interval-component",
        interval=10*1000,
        n_intervals=50,
        disabled=True),
        html.Div(
        id="graph-container",
        children=[
            #html.Div(id="dropdown-content"), used as a debugger, uncomment in callback_functions.py
            html.Br(),
            tf.generate_banner("Graph Section"),
            dcc.Graph(id="graph-chart")]),])
