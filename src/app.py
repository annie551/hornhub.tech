import dash
import dash_bootstrap_components as dbc
from dash import Dash, html
import logging
from pathlib import Path

app = Dash(__name__)


app.layout = html.Div(
    [
        html.H1(
            "hello",
        ),
    ],
    id = "hello",
)

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8050, debug=False)
