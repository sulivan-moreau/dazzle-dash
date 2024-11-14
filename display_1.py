# import plotly.express as px
# import pandas as pd

# df = pd.read_csv('lifeExpectancyClean.csv')

# print(df.head())

# fig = px.bar(df, x='year', y='life_expectancy')
# fig.show()

# from dash import Dash, dcc, html, Input, Output
# import pandas as pd
# import plotly.express as px

# app = Dash(__name__)
# df = pd.read_csv('lifeExpectancyClean.csv')

# app.layout = html.Div([
#     html.H4('Restaurant tips by day of week'),
#     dcc.Dropdown(
#         id="dropdown",
#         options=[{'label': country, 'value': country} for country in df['country'].unique()],
#         value="France",
#         clearable=False,
#     ),
#     dcc.Graph(id="graph"),
# ])


# @app.callback(
#     Output("graph", "figure"), 
#     Input("dropdown", "value"))
# def update_bar_chart(day):
#     df = px.data.tips() 
#     mask = df["day"] == day
#     # fig = px.bar(df[mask], x="year", y="life_expectancy", 
#     #              color="smoker", barmode="group")
#     fig = px.bar(df[mask], x="year", y="life_expectancy")
#     return fig


# app.run_server(debug=True)

# df = px.data.gapminder().query("country == 'Canada'")
# fig = px.bar(df, x='year', y='pop',
#              hover_data=['lifeExp', 'gdpPercap'], color='lifeExp',
#              labels={'pop':'population of Canada'}, height=400)
# fig.show()
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Initialisation de l'application Dash
app = Dash(__name__)

# Chargement des données
df = pd.read_csv('lifeExpectancyClean.csv')

# Mise en page de l'application
app.layout = html.Div([
    html.H4('Population and Life Expectancy by Country and Year'),
    dcc.Dropdown(
        id="dropdown",
        options=[{'label': country, 'value': country} for country in df['country'].unique()],
        value="France",  # Valeur par défaut
        clearable=False,
    ),
    dcc.Graph(id="graph"),
])

# Définition du callback pour mettre à jour le graphique
@app.callback(
    Output("graph", "figure"), 
    Input("dropdown", "value"))
def update_bar_chart(selected_country):
    # Filtrer les données pour le pays sélectionné
    filtered_df = df[df["country"] == selected_country]
    
    # Créer le graphique avec couleur selon l'espérance de vie
    fig = px.bar(filtered_df, x="year", y="life_expectancy", color="life_expectancy",
                 title=f"Population and Life Expectancy in {selected_country} Over Time",
                 labels={'population': 'Population', 'year': 'Year', 'life_expectancy': 'Life Expectancy'})
    
    # Personnalisation des couleurs pour un effet similaire au graphique de l'image
    fig.update_traces(marker=dict(coloraxis=None))
    fig.update_layout(coloraxis_colorbar=dict(title="Life Expectancy"))

    return fig

# Exécution de l'application
if __name__ == '__main__':
    app.run_server(debug=True)
