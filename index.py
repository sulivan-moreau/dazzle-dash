from dash import html, dcc, callback, Output, Input
import layout  # Import direct du fichier layout

# Layout principal avec navigation
layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Vue d\'ensemble | ', href='/'),
        dcc.Link('Analyse par indicateur | ', href='/indicators'),
        dcc.Link('Comparaison par statut', href='/comparison'),
    ], style={'padding': '20px', 'font-size': '18px'}),
    html.Div(id='page-content')
])

# Gestion dynamique des pages
@callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/':
        return layout.overview_layout
    elif pathname == '/indicators':
        return layout.indicator_layout
    elif pathname == '/comparison':
        return layout.comparison_layout
    else:
        return html.H1("404: Page non trouvée")
