from dash import Input, Output
from app import app
import pandas as pd
import plotly.express as px

df = pd.read_csv("lifeExpectancyClean.csv")

# Callback pour mettre à jour le graphique en fonction de l'indicateur sélectionné
@app.callback(
    Output('indicator-graph', 'figure'),
    Input('indicator-dropdown', 'value')
)
def update_indicator_graph(selected_indicator):
    return px.scatter(
        df, x=selected_indicator, y='life_expectancy',
        title=f"Relation entre life_expectancy et {selected_indicator}"
    )
