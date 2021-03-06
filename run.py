# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app, server
from pages import about, index


navbar = dbc.NavbarSimple(
    
    brand='Post Here',
    brand_href='/', 
    children=[
        dbc.NavItem(dcc.Link('About', href='/about', className='nav-link'))
    ],
    sticky='top',
    color='dark', 
    light=False, 
    dark=True
)

footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/scottwmwork'), 
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/scott-maxwell-415171142/')
                ], 
                className='lead'
            )
        )
    )
)


app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    navbar, 
    footer,
    dbc.Container(id='page-content', className='mt-4'), 
    html.Hr()
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/about':
        return about.layout
    else:
        return dcc.Markdown('## Page not found')

if __name__ == '__main__':
    app.run_server(debug=True)
