from dash import html, dcc
from layout import dashboard_layout  # Import unique pour la page principale

# Layout pour la navigation
layout = html.Div([
    html.Div(id='page-content'),
    dashboard_layout  # Affiche directement le dashboard interactif
])
