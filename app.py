from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app.layout = html.Div(
    className="background",
    children=[html.Div(
             className ="header",
                        children = [
                        html.H1(
                        className = "title",
                        children = ["Intgeration check"])
                    ]
                    ),
             html.Div(
             className="Center",
             children=[
                    html.Div(
                        className="right",
                        children=[html.H2("right")]
                        

                    ),
                    html.Div(
                        className="left",
                        children=[html.H2("left")]
                    ),
             ]
         ),
                    html.Br(),

            html.Div(
                className="footer",
                children=[html.H2("footer")]
            )
    ]
    
    

)



if __name__ == '__main__':
    app.run_server(debug=True)