import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
from tabs import tab_functions as tb

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

tab_2_layout = html.Div([
    html.Br(),
    tb.create_table("data-table",df,15),
    html.Div(id='datatable-interactivity-container')
])
