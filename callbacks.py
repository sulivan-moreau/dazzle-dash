from dash import Input, Output
from app import app
import pandas as pd
import plotly.express as px

# Chargement des données
df = pd.read_csv("lifeExpectancyClean.csv")
df = df.dropna(subset=['life_expectancy', 'adult_mortality', 'hiv/aids', 'gdp', 'schooling'])

# Dictionnaire pour mapper les options dropdown aux colonnes réelles
INDICATOR_MAP = {
    "Mortalité adulte": "adult_mortality",
    "VIH/SIDA": "hiv/aids",
    "PIB": "gdp",
    "Scolarisation": "schooling"
}

@app.callback(
    Output('indicator-graph', 'figure'),
    Input('indicator-dropdown', 'value')
)
def update_scatter_plot(selected_indicator_label):
    # Convertit le label sélectionné en colonne
    selected_indicator = INDICATOR_MAP.get(selected_indicator_label)

    if selected_indicator not in df.columns:
        return px.scatter(title="Indicateur non valide ou manquant")

    # Création du graphique
    fig = px.scatter(
        df,
        x=selected_indicator,
        y='life_expectancy',
        title=f"Espérance de vie vs {selected_indicator_label}",
        labels={selected_indicator: selected_indicator_label, 'life_expectancy': 'Espérance de vie'}
    )
    fig.update_traces(marker=dict(size=8, opacity=0.7))
    return fig
