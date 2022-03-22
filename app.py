from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)



app.layout = html.Div(children=[
    html.H1(
        className="title",
        children = ["Intgeration check"]
        )
    ]
    
)

if __name__ == '__main__':
    app.run_server(debug=True)