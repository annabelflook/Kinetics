import pandas as pd
import calculate_data as cd

from dash import Dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import plotly.express as px
import app_layout


# Define the app and layout
# --------------------------------------------
app = Dash(name=__name__, external_stylesheets=[dbc.themes.LITERA],
           meta_tags=app_layout.meta_tags())
server = app.server
app.layout = app_layout.app_layout()

# Get data from COPASI pycotools
# --------------------------------------------
mod = cd.load_model(1, 1, 1)
global_df = pd.DataFrame(cd.get_data(mod))
cd.delete_files()


@app.callback(
    Output('intermediate-value', 'children'),
    [Input('k1 slider', 'value'),
     Input('k_minus1 slider', 'value'),
     Input('k2 slider', 'value')]
)
def compute_data(selected_k1, selected_kminus1, selected_k2):
    """
    New rate constants are selected by the slider bars and run into COPASI
    using pycotools module. New data is converted to json.

    :param selected_k1:
    :param selected_kminus1:
    :param selected_k2:
    :return: json in an invisible intermediate section to be recalled by the app.
    """
    new_mod = cd.load_model(selected_k1, selected_kminus1, selected_k2)
    updated_df = pd.DataFrame(cd.get_data(new_mod))
    cd.delete_files()
    return updated_df.to_json()


@app.callback(
    Output('timeseries', 'figure'),
    Input('intermediate-value', 'children'))
def update_figure(computed_data):
    """
    Displays the updated json in the app.
    :param computed_data:
    :return: Updated figure
    """
    df = pd.read_json(computed_data)
    fig = px.line(df[['S', 'I', 'P', 'C']])
    fig.update_layout(transition_duration=100)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
