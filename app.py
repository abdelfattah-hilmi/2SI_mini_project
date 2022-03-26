from email import message
from dash import Dash, html, dcc, Input,Output
from hashlib import md5, sha1,sha256

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

            dcc.Dropdown(
                id = "hash_function",
                className = "hash_function",
                clearable = False,
                value = 'sha-1',
                options=[
                    {'label': 'sha-1', 'value': 'sha-1'},
                    {'label': 'sha-256', 'value': 'sha-256'},
                    {'label': 'md5', 'value': 'md5'},
                    
                ]
            ),

            html.Br(),

            

            html.H4('messge'),
            dcc.Textarea(
                id = "initial_message",
                className = "textarea",
            ),
            html.Br(),
            dcc.Input(
                id = "message-digest"
            ),
            html.Br(),
            
            html.Br(),



            html.Hr(),

            

            html.Br(),


            html.H4('messge2'),
            dcc.Textarea(
                id= 'message-to-check'
            ),
            html.Br(),
            dcc.Input(
                id="hashed1"
            ),
            html.Br(),
            

            html.Br(),

            html.Button(
                id="hash1",
                n_clicks=0,
                children=[
                    "hash"
                    ]),
            html.Button(
                id = 'copy' ,
                n_clicks=0,
                children=[
                    "copy"
                ]),
            
            
            html.Button(
                id = 'check' ,
                n_clicks=0,
                children=[
                    "check"
                ]),

            html.Br(),
            html.Div(
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
    Output(component_id='message-digest',component_property='value'),
    Input(component_id='hash_function',component_property='value'),
    Input(component_id='initial_message',component_property='value'),
)
def hash(fun,msg):
    if msg:
        if fun == 'sha-1':
            return sha1(msg.encode('UTF-8')).hexdigest() 
        elif fun == 'sha-256':
            return sha256(msg.encode('UTF-8')).hexdigest()
        elif fun == 'md5':
            return md5(msg.encode('UTF-8')).hexdigest()
    else:
        return ''



@app.callback(
    Output(component_id='message-to-check',component_property='value'),
    Input(component_id='initial_message',component_property='value'),
    Input(component_id='copy',component_property='n_clicks')
)
def copy(msg,click):
    if click != 0:
        return msg
    
@app.callback(
    Output(component_id='hashed1',component_property='value'),
    Input(component_id='message-to-check',component_property='value'),
    Input(component_id='hash1',component_property='n_clicks'),
    Input(component_id='hash_function',component_property='value'),
)
def hash_2(msg,click,fun):
    if click != 0:
        if msg:
            if fun == 'sha-1':
                return sha1(msg.encode('UTF-8')).hexdigest() 
            elif fun == 'sha-256':
                return sha256(msg.encode('UTF-8')).hexdigest()
            elif fun == 'md5':
                return md5(msg.encode('UTF-8')).hexdigest()
        else:
            return ''


@app.callback(
    Output(component_id='result',component_property='children'),
    Input(component_id='hashed1',component_property='value'),
    Input(component_id='message-digest',component_property='value'),
    Input(component_id='check',component_property="value"),
)
def check(digest1,digest2,click):
    if click != 0:
        if digest1 == digest2 :
            return 'cool'
        else :
            return 'not cool' 




if __name__ == '__main__':
    app.run_server(debug=True)