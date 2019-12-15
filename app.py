import dash
import dash_bootstrap_components as dbc

"""
Different themes:

dbc.themes.BOOTSTRAP
dbc.themes.CERULEAN
dbc.themes.COSMO
dbc.themes.CYBORG
dbc.themes.DARKLY
dbc.themes.FLATLY
dbc.themes.JOURNAL
dbc.themes.LITERA
dbc.themes.LUMEN
dbc.themes.LUX
dbc.themes.MATERIA
dbc.themes.MINTY
dbc.themes.PULSE
dbc.themes.SANDSTONE
dbc.themes.SIMPLEX
dbc.themes.SKETCHY
dbc.themes.SLATE
dbc.themes.SOLAR
dbc.themes.SPACELAB
dbc.themes.SUPERHERO
dbc.themes.UNITED
dbc.themes.YETI
"""

external_stylesheets = [
    dbc.themes.DARKLY, # Bootswatch theme
]

meta_tags=[
    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)
app.config.suppress_callback_exceptions = True
app.title = 'post_here' # appears in browser title bar
server = app.server
