from dash import Dash, html, dcc, Input,Output
from hashlib import sha1,sha256

app = Dash(__name__)



app.layout = html.Div(children=[
    html.Div(
        className ="Center-card",
        children = [
            html.H1(
            className = "title",
            children = ["Intgeration check"]
            ),

            html.Br(),

            html.Select(
                id = "hash_function",
                className="select",
                children = [
                    html.Option("sha-1"),
                    html.Option("sha-256"),
                    html.Option("md5"), 
                ]
            ),

            html.Br(),

            

            html.H4('messge'),
            dcc.Textarea(
                id = "initial_message",
                className = "textarea",
            ),
            html.Br(),
            dcc.Input(),
            html.Br(),
            
            html.Br(),



            html.Hr(),

            

            html.Br(),


            html.H4('messge2'),
            dcc.Textarea(),
            html.Br(),
            dcc.Input(),
            html.Br(),
            

            html.Br(),

            html.Button("hash"),
            html.Button("copy"),
            html.Button("clear"),
            html.Button("check"),

            html.Br(),
            html.P(
                id = "result",
                className = "result",
                children = [
                    "placeholder",
                ]
            ),
        ]
        )
    ])



@app.callback(
    Output(component_id='result',component_property='children'),
    Input(component_id='hash_function',component_property='children'),
    Input(component_id='initial_message',component_property='value'),
)
def hash(fun,msg):
    print(fun)
    print(msg)
    print('------')




if __name__ == '__main__':
    app.run_server(debug=True)