import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash import Dash

# Load data
# --------------------------------------------
df = pd.read_csv('dataframe', index_col='Time')
# --------------------------------------------

# Set up app and server. Set up the style sheets and prepare for smaller screens.
# --------------------------------------------
app = Dash(name=__name__, external_stylesheets=[dbc.themes.LITERA],
           meta_tags=[{'name': 'viewport',
                       'content': 'width=device-width, initial-scale=1.0'}])
server = app.server
# --------------------------------------------
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Kinetics Approximation",
                        className='text-center text-primary mb-4 pt-4'),
                width=12)  # 12 columns wide, this is the max number of cols available
    ]),

    dbc.Row([
        dbc.Col(id='InfoCol', children=[
            'Adjust the relative rates of k1, k minus1 and k2 to see how the graph changes'
            'If k1 and k minus1 >> k2, the graph will resemble pre-equilibrium approximation'
            'If k2 >> k1, the system will be under steady state approximations.'
        ],
                # How many cols will it take up, and which col will we start counting from.
                # Also, which order do you want this col to appear in wrt the other col in this row.
                width={'size': 3, 'offset': 0.5, 'order': 1}),

        dbc.Col(id='GraphCol', children=[
            dcc.Graph(id='my-second-graph', figure=px.line(df['S'])),

        ],
                width={'size': 8, 'offset': 0, 'order': 2}, className='text-center')
        # Gutters can create space between col components
        # Justify is the left-right justification
    ], no_gutters=False, justify='around'),

    dbc.Row(id='RateSliders', children=[

        dbc.Col(id='k1 label', children=[
            html.P("k1")
        ], width={'size': 1, 'offset': 4, 'order': 1}),

        dbc.Col(id='Slider1Col', children=[
            dcc.Slider(id='Slider1'),
        ], width={'size': 6, 'offset': 0, 'order': 2}),

        dbc.Col(id='k2 label', children=[
            html.P("k2")
        ], width={'size': 1, 'offset': 4, 'order': 3}),

        dbc.Col(id='Slider2Col', children=[
            dcc.Slider(id='Slider2')
        ], width={'size': 6, 'offset': 0, 'order': 4}),


        dbc.Col(id='k3 label', children=[
            html.P("k3")
        ], width={'size': 1, 'offset': 4, 'order': 5}),

        dbc.Col(id='Slider3Col', children=[
            dcc.Slider(id='Slider3')
        ], width={'size': 6, 'offset': 0, 'order': 6}),


    ], no_gutters=False, className='p-2 ml-1 align-bottom text-right'),

], fluid=True)

# App Layout, if using pure Bootstrap, you can use dbc container rather than html.Div
# --------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True)
