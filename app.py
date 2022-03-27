from email import message
from dash import Dash, html, dcc, Input,Output
from hashlib import md5, sha1,sha256, sha512

app = Dash(__name__)

app.layout = html.Div(children=[
    html.Div(
        className ="Center-card",
        children = [
            html.H1(
            className = "title",
            children = ["Test d'integration"]
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
                    {'label': 'sha-512', 'value': 'sha-512'},
                    {'label': 'md5', 'value': 'md5'}, 
                ]
            ),

            html.Br(),

            

            html.Div(
                className='arealabel',
                children='Message initial:'
                ),
            dcc.Textarea(
                id = "initial_message",
                className = "textarea",
            ),

            html.Br(),

            dcc.Input(
                id = "message-digest",
                className="digest"
            ),
            html.Br(),
            
            html.Br(),



            html.Hr(),

            

            html.Br(),


            html.Div(
                className='arealabel',
                children='Message a vérifier:'
                ),
            dcc.Textarea(
                id= 'message-to-check',
                className = "textarea",

            ),
            html.Br(),
            dcc.Input(
                id="hashed1",
                className="digest"
            ),
            html.Br(),
            

            html.Br(),

            html.Button(
                id="hash1",
                className="Button btn1",
                n_clicks=0,
                children=[
                    "hash"
                    ]),
            html.Button(
                id = 'copy' ,
                className="Button btn2",
                n_clicks=0,
                children=[
                    "copy"
                ]),
            
            
            html.Button(
                id = 'check' ,
                className="Button btn3",
                n_clicks=0,
                children=[
                    "check"
                ]),

            html.Br(),
            html.Div(
                id = "result",
                className = "result",
                children = [
                    "",
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
        elif fun == 'sha-512':
            return sha512(msg.encode('UTF-8')).hexdigest()
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
            elif fun == 'sha-512':
                return sha512(msg.encode('UTF-8')).hexdigest()
        else:
            return ''



cool_message = html.Div(
    className="cool",
    children="✅ Le message n'est pas modifié.",
)
not_cool_message = html.Div(
    className="not_cool",
    children="❌ Le message est modifié.",
)


@app.callback(
    Output(component_id='result',component_property='children'),
    Input(component_id='hashed1',component_property='value'),
    Input(component_id='message-digest',component_property='value'),
    Input(component_id='check',component_property="n_clicks"),
)
def check(digest1,digest2,click):
    if click:
        if digest1 == digest2 :
            return cool_message
        else :
            return not_cool_message




if __name__ == '__main__':
    app.run_server(debug=True)