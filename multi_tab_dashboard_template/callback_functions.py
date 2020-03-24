import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from app import app
from tabs import dropdown_tab,datatable_tab
from tabs import tab_functions as tf
import  plotly.graph_objs as go
import pandas as pd
import numpy as np
import flask


#one can have the callbacks of each tab into separate scripts as well

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

#callback for main script
@app.callback(Output('tabs-content-example', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    if tab =='tab-1-example':
        return dropdown_tab.tab_1_layout
    elif tab == 'tab-2-example':
        return datatable_tab.tab_2_layout


#callback for dropdown_tab script
#following callback used as debugger
# @app.callback(Output("dropdown-content","children"),inputs=[Input("continent-dropdown","value")])
# def test(value):
#     return 'You  have selected {} to plot the scatter plots'.format(value)

@app.callback(Output("graph-chart", "figure"),inputs=[Input("continent-dropdown", "value")])
def draw_graph(continent):
    dff = df[df['continent']==continent]
    trace=go.Scatter(
        x=dff["country"].tolist(),
        y=dff["gdpPercap"].tolist(),
        mode='markers',
        marker=dict(size=8,color='#0000ff')
    )
    data=[trace]

    layout=go.Layout(
        font=dict(family='Carlito',size=14,color='#A9A9A9'),
        title="Plotting {}'s {} by Country Scatter Plot".format(continent,"GDP per Capita"))
    fig = go.Figure(data=data,layout=layout)
    return fig


#callbacks for datatable_tab
@app.callback(
    Output('data-table', 'style_data_conditional'),
    [Input('data-table', 'selected_columns')]
)
def update_styles(selected_columns):
    return [{
        'if': { 'column_id': i },
        'background_color': '#D2F3FF'
    } for i in selected_columns]

@app.callback(
    Output('datatable-interactivity-container', "children"),
    [Input('data-table', "derived_virtual_data"),
     Input('data-table', "derived_virtual_selected_rows")])
def update_graphs(rows, derived_virtual_selected_rows):
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []

    dff = df if rows is None else pd.DataFrame(rows)

    colors = ['#7FDBFF' if i in derived_virtual_selected_rows else '#0074D9'
              for i in range(len(dff))]

    return [
        dcc.Graph(
            id=column,
            figure={
                "data": [
                    {
                        "x": dff["country"],
                        "y": dff[column],
                        "type": "bar",
                        "marker": {"color": colors},
                    }
                ],
                "layout": {
                    "xaxis": {"automargin": True},
                    "yaxis": {
                        "automargin": True,
                        "title": {"text": column}
                    },
                    "height": 250,
                    "margin": {"t": 10, "l": 10, "r": 10},
                },
            },
        )
        # check if column exists - user may have deleted it
        # If `column.deletable=False`, then you don't
        # need to do this check.
        for column in ["pop", "lifeExp", "gdpPercap"] if column in dff
    ]
