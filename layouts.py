import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd


head_div_style = {'padding': '0.25%', 'text-align': 'center'}
big_div_style = {'padding': '0.25%', 'padding-top': '0.5%', 'padding-bottom': '0.5%'}
graph_style = {'padding': '3%', 'padding-top': '0.5%', 'background-color': '#fff', 'height': '100%'}
df = pd.DataFrame()


layout = html.Div([
    dcc.Location(id='url', refresh=True),
    dcc.Interval(id='interval1',
                 interval=1280,  # in milliseconds
                 n_intervals=0),
    dcc.Interval(id='interval2',
                 interval=320,  # in milliseconds
                 n_intervals=0),
    html.Div([  # header
        html.Div([
            html.Img(
                src='/assets/Tecnología deportiva.png',
                height='58 px',
                width='auto')
        ], className='col-2', style=head_div_style),
        html.Div([
            html.H1('Rowing Corrector pa')
        ], className='col-8'),
        html.Div([
            html.Img(
                src='/assets/UTN_logo.png',
                height='53 px',
                width='auto')
        ], className='col-2', style=head_div_style)
    ], className='row align-items-center', style=head_div_style),  # header
    html.Hr(),

    html.Div([
        dbc.Row([
            dcc.Graph(id='asdasd')
            ]),
        dbc.Row(html.H1("CLASIFICACIÓN", id='label'), className='my-5', style={'text-align': 'center'})
    ], className='col-12 align-items-center', style=big_div_style)
], className='container')
