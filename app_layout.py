import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html


def app_layout():
    return (dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Kinetics Approximation",
                            className='text-center text-primary mb-4 pt-4'),
                    width=12)  # 12 columns wide, this is the max number of cols available
        ]),

        dbc.Row([
            dbc.Col(id='InfoCol', children=[
                'Adjust the relative rates of k1, k minus1 and k2 to see how the graph changes'
            ],
                    # How many cols will it take up, and which col will we start counting from.
                    # Also, which order do you want this col to appear in wrt the other col in this row.
                    width={'size': 3, 'offset': 0.5, 'order': 1}),

            dbc.Col(id='GraphCol', children=[
                dcc.Graph(id='timeseries'),
            ], width={'size': 8, 'offset': 0, 'order': 2}, className='text-center'),
            # Gutters can create space between col components
            # Justify is the left-right justification
            dbc.Col(id='intermediate-value', style={'display': 'none'}),

        ], no_gutters=False, justify='around'),

        dbc.Row(id='RateSliders', children=[

            # Slider labels
            # -----------------------------------------------
            dbc.Col(id='k1 label', children=[
                html.P("k1")
            ], width={'size': 1, 'offset': 4, 'order': 1}),

            dbc.Col(id='k2 label', children=[
                html.P("k2")
            ], width={'size': 1, 'offset': 4, 'order': 3}),

            dbc.Col(id='k3 label', children=[
                html.P("k3")
            ], width={'size': 1, 'offset': 4, 'order': 5}),

            # Slider bars
            # -----------------------------------------------
            dbc.Col(id='Slider1Col', children=[
                dcc.Slider(
                    id='k1 slider',
                    min=0.1,
                    max=1,
                    value=0.5,
                    marks={0.1: str('k1 = 0.1'),
                           0.5: str('k1 = 0.5'),
                           1: str('k1 = 1')},
                    step=None
                ),
            ], width={'size': 6, 'offset': 0, 'order': 2}),

            dbc.Col(id='Slider2Col', children=[
                dcc.Slider(
                    id='k_minus1 slider',
                    min=0.1,
                    max=1,
                    value=0.5,
                    marks={0.1: str('k-1 = 0.1'),
                           0.5: str('k-1 = 0.5'),
                           1: str('k-1 = 1')},
                    step=None
                ),
            ], width={'size': 6, 'offset': 0, 'order': 4}),

            dbc.Col(id='Slider3Col', children=[
                dcc.Slider(
                    id='k2 slider',
                    min=0.1,
                    max=1,
                    value=0.5,
                    marks={0.1: str('k2 = 0.1'),
                           0.5: str('k2 = 0.5'),
                           1: str('k2 = 1')},
                    step=None
                ),
            ], width={'size': 6, 'offset': 0, 'order': 6}),

        ], no_gutters=False, className='p-2 ml-1 align-bottom text-right'),

    ], fluid=True)
    )


def meta_tags():
    return [{'name': 'viewport',
            'content': 'width=device-width, initial-scale=1.0'}]


if __name__ == '__main__':
    from dash import Dash

    app = Dash(name=__name__, external_stylesheets=[dbc.themes.LITERA],
               meta_tags=meta_tags())

    server = app.server
    app.layout = app_layout()
    app.run_server(debug=True, port=8080)
