from dash import html, dcc, callback, Output, Input
from layout import overview_layout, indicator_layout, comparison_layout  # Import des layouts

# Layout principal avec navigation
layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Vue d\'ensemble | ', href='/'),
        dcc.Link('Analyse par indicateur | ', href='/indicators'),
        dcc.Link('Comparaison par statut', href='/comparison'),
    ], style={'padding': '20px', 'font-size': '18px'}),
    html.Div(id='page-content')  # Contenu dynamique des pages
])

# Callback pour la navigation entre les pages
@callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/':
        return overview_layout
    elif pathname == '/indicators':
        return indicator_layout
    elif pathname == '/comparison':
        return comparison_layout
    else:
        return html.H1("404: Page non trouvée")
