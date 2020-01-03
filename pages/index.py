import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pickle

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

# Loading the scikit Learn models with Pickle
filename = 'assets/nlp_model.plk'
model_pkl = open(filename, 'rb')
model = pickle.load(model_pkl)

column1 = dbc.Col(
    [

    ]
)

column2 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Enter your post's title here:
           
            """
        ),

        dbc.Input(
            id = 'input',placeholder="Post text...", bs_size="lg", className="mb-3"
        ),
        dcc.Markdown(""" You should post in: """),
        html.P(id = 'output')
    ],
    md=5,
)



@app.callback(Output("output", "children"), [Input("input", "value")])
def output_text(value):
    if value == '':
        return ''
    else:
        return 'r/{}'.format(str(model.predict([value])[0]))


column3 = dbc.Col(
    [

    ]
)

layout = dbc.Row([column1, column2, column3])