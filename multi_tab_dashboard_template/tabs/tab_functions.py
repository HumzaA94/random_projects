import dash
from dash.dependencies import Input, Output,State
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objs as go
import flask
import dash_table

def generate_banner(title):
    return html.Label(children=title)

def single_value_dropdown(container_id,div_id,label_name,list1):
    return html.Div(
    id= container_id, #container_id used to design the the container of the dropdown in css,
    children = [      #if more than 1 container will have the exact feature, a classname might be more convenient
    html.Label(children=label_name),
    html.Br(),
    dcc.Dropdown(
    id=div_id,
    options=[{'label': l, 'value': l} for l in list1],
    value=list1[0],
    style={'display':'inline-block','width':'300px','height':'30px'} #can have it in css or here
    ),],
    )

def multi_value_dropdown(div_id,label_name,list1):
    return html.Div(
    id= div_id,
    children = [
    html.Label(children=label_name),
    html.Br(),
    dcc.Dropdown(
    options=[{'label': l, 'value': l} for l in list1],
    value=[list1[0],list1[1]],
    style={'display':'inline-block','width':'300px','height':'30px'},
    multi=True
    ),],
    )

def create_table(div_id,df,page_no):
    return (dash_table.DataTable(
        id=div_id,
        columns=[{"name": i, "id": i, "deletable": True, "selectable": True} for i in df.columns],
        data=df.to_dict('records'),
        editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= page_no))
