import pandas as pd
from dash import html, dcc
import plotly.express as px

# Chargement des données
df = pd.read_csv("lifeExpectancyClean.csv")

# Nettoyage des données (gdp et autres colonnes numériques)
df['gdp'] = pd.to_numeric(df['gdp'], errors='coerce').fillna(0)

# Statistiques principales
total_countries = df['country'].nunique()
average_life_expectancy = df['life_expectancy'].mean().round(2)
average_population = (df['population'].mean() / 1_000_000).round(2)
average_gdp = (df['gdp'].mean() / 1_000).round(2)
total_expenditure = df['total_expenditure'].sum().round(2)

# Graphiques
fig_life_expectancy_year = px.line(
    df.groupby("year")['life_expectancy'].mean().reset_index(),
    x="year", y="life_expectancy",
    title="Average Life Expectancy by Year", markers=True
)

status_count = df['status'].value_counts().reset_index()
status_count.columns = ['status', 'count']
fig_status = px.pie(
    status_count, names="status", values="count",
    title="Hepatitis B by Status", hole=0.4
)

fig_top_gdp = px.bar(
    df.groupby('country')['gdp'].sum().nlargest(10).reset_index(),
    x="gdp", y="country", orientation="h",
    title="Top 10 Countries by GDP", text="gdp"
)

fig_population = px.bar(
    df.groupby('country')['population'].sum().nlargest(10).reset_index(),
    x="population", y="country", orientation="h",
    title="Country Analysis Based on Population", text="population"
)

top_life_expectancy = df.groupby("country")['life_expectancy'].mean().nlargest(10)

# Layout complet du dashboard
dashboard_layout = html.Div([
    html.H1("LIFE EXPECTANCY ANALYSIS", style={"textAlign": "center", "color": "darkred"}),

    # Statistiques principales
    html.Div([
        html.Div(f"TOTAL COUNTRIES: {total_countries}", className="stat-box"),
        html.Div(f"AVERAGE LIFE EXPECTANCY: {average_life_expectancy}", className="stat-box"),
        html.Div(f"AVERAGE POPULATION: {average_population}M", className="stat-box"),
        html.Div(f"AVERAGE GDP: {average_gdp}K", className="stat-box"),
        html.Div(f"TOTAL EXPENDITURE: {total_expenditure}K", className="stat-box"),
    ], style={"display": "flex", "justifyContent": "space-around", "margin": "20px"}),

    # Graphiques principaux
    html.Div([
        dcc.Graph(figure=fig_life_expectancy_year, style={"width": "48%", "display": "inline-block"}),
        dcc.Graph(figure=fig_status, style={"width": "48%", "display": "inline-block"}),
    ]),

    html.Div([
        dcc.Graph(figure=fig_top_gdp, style={"width": "48%", "display": "inline-block"}),
        dcc.Graph(figure=fig_population, style={"width": "48%", "display": "inline-block"}),
    ]),

    # Tableau des pays avec la meilleure espérance de vie
    html.Div([
        html.H3("LIFE EXPECTANCY BY POPULATION", style={"textAlign": "center", "marginBottom": "20px"}),
        html.Table([
            html.Tr([html.Th("Country"), html.Th("Average Life Expectancy")])
        ] + [
            html.Tr([html.Td(country), html.Td(round(value, 1))])
            for country, value in top_life_expectancy.items()
        ], style={"margin": "auto", "textAlign": "center", "width": "50%"})
    ])
], style={"margin": "20px"})
