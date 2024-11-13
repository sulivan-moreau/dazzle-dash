from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# Charger les données
df = pd.read_csv('lifeExpectancyClean.csv')

# Initialiser l'application avec un thème Bootstrap
app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])  # Vous pouvez changer le thème ici

# Layout de l'application
app.layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1("Dashboard - Espérance de Vie", className="text-center text-primary mt-4 mb-4"))),
    
    dbc.Row([
        dbc.Col([
            html.Label("Sélectionnez un pays :"),
            dcc.Dropdown(
                id='country-dropdown',
                options=[{'label': country, 'value': country} for country in df['country'].unique()],
                value='France'  # Pays par défaut
            ),
        ], width=3),
        dbc.Col(dcc.Graph(id='life-expectancy-graph'), width=9),
    ], className="mb-4"),
    
    dbc.Row(dbc.Col(dcc.Graph(id='correlation-graph'), width=12), className="mb-4"),
    
    dbc.Row(dbc.Col(html.H2("Table des données", className="text-center mb-4"))),
    dbc.Row(dbc.Col(
        dash_table.DataTable(
            id='data-table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
            page_size=10,
            style_table={'overflowX': 'auto', 'margin': '0 auto'},
            style_cell={'textAlign': 'left', 'padding': '5px'},
            style_header={'backgroundColor': 'lightblue', 'fontWeight': 'bold'}
        ),
        width=12
    )),
], fluid=True)

# Callback pour mettre à jour le graphique d'espérance de vie en fonction du pays sélectionné
@app.callback(
    Output('life-expectancy-graph', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_life_expectancy_graph(selected_country):
    filtered_df = df[df['country'] == selected_country]
    fig = px.line(filtered_df, x='year', y='life_expectancy', title=f"Évolution de l'espérance de vie - {selected_country}")
    fig.update_layout(xaxis_title="Année", yaxis_title="Espérance de vie")
    return fig

# Callback pour afficher la corrélation entre l'alcool et l'espérance de vie
@app.callback(
    Output('correlation-graph', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_correlation_graph(selected_country):
    filtered_df = df[df['country'] == selected_country]
    fig = px.scatter(filtered_df, x='alcohol', y='life_expectancy',
                     title=f"Corrélation entre la consommation d'alcool et l'espérance de vie - {selected_country}",
                     trendline="ols")
    fig.update_layout(xaxis_title="Consommation d'alcool", yaxis_title="Espérance de vie")
    return fig

# Exécuter l'application
if __name__ == '__main__':
    app.run_server(debug=True)