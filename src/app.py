import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import logging
from pathlib import Path

app = Dash(__name__)

# Define the layout for the homepage
homepage_layout = html.Div(
    [
        html.H1("Welcome to the Homepage"),
        html.Button("Login", id="login-button", n_clicks=0),
        html.Div(id="redirect-div")
    ]
)

# Define the layout for the login page
login_layout = html.Div(
    [
        html.H1("Login Page"),
        dcc.Input(id="username-input", type="text", placeholder="Username"),
        dcc.Input(id="password-input", type="password", placeholder="Password"),
        html.Button("Submit", id="login-submit-button", n_clicks=0),
        html.Div(id="login-status")
    ]
)

# Define callback to handle button click and redirect to login page
@app.callback(
    Output("redirect-div", "children"),
    [Input("login-button", "n_clicks")]
)
def redirect_to_login_page(n_clicks):
    if n_clicks > 0:
        return dcc.Location(pathname="/login", id="login-url")

# Define callback to handle login form submission
@app.callback(
    Output("login-status", "children"),
    [Input("login-submit-button", "n_clicks")],
    [State("username-input", "value"), State("password-input", "value")]
)
def authenticate_user(n_clicks, username, password):
    if n_clicks > 0:
        # Perform authentication here (placeholder)
        if username == "admin" and password == "admin":
            return "Login successful!"
        else:
            return "Invalid username or password."

# Define the app layout combining both homepage and login page
app.layout = html.Div(
    [
        dcc.Location(id="url"),
        html.Div(id="page-content")
    ]
)

# Define callback to switch between pages based on URL
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def display_page(pathname):
    if pathname == "/login":
        return login_layout
    else:
        return homepage_layout

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8050, debug=False)
