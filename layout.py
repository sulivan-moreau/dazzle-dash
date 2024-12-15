import pandas as pd
from dash import html, dcc
import plotly.express as px

df = pd.read_csv("lifeExpectancyClean.csv")

# Layout Vue d'ensemble



overview_layout = html.Div([
    html.H1("Vue d'ensemble des indicateurs clés"),
    dcc.Graph(
        figure=px.imshow(
            df[['life_expectancy', 'adult_mortality', 'hiv/aids', 'gdp']].corr(), 
            color_continuous_scale='viridis',  # Utilise 'viridis' ou une autre palette valide
            title="Matrice de corrélation des indicateurs clés"
        )
    )
])


indicator_layout = html.Div([
    html.H1("Analyse par indicateur spécifique"),
    dcc.Dropdown(
        id='indicator-dropdown',
        options=[
            {'label': 'Mortalité adulte', 'value': 'adult_mortality'},
            {'label': 'VIH/SIDA', 'value': 'hiv/aids'},
            {'label': 'PIB', 'value': 'gdp'},
        ],
        value='adult_mortality'
    ),
    dcc.Graph(id='indicator-graph')  # Graphique interactif
])

import pandas as pd
from dash import html, dcc
import plotly.express as px

df = pd.read_csv("lifeExpectancyClean.csv")

# Sélection des colonnes numériques et groupement par status
df_numeric = df.select_dtypes(include='number')
df_grouped = df_numeric.join(df['status']).groupby('status').mean().reset_index()

comparison_layout = html.Div([
    html.H1("Comparaison des indicateurs par statut des pays"),
    dcc.Graph(
        figure=px.bar(
            df_grouped,
            x='status',
            y=['life_expectancy', 'gdp', 'schooling'],
            barmode='group',
            title="Comparaison des indicateurs par statut (développé vs en développement)"
        )
    )
])


