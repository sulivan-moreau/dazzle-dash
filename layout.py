from dash import dcc, html

def create_layout(df):
    # Options pour les filtres
    available_years = sorted(df['year'].unique())
    available_countries = sorted(df['country'].unique())

    # Layout de l'application
    return html.Div([
        html.H1("Tableau de bord sur l'espérance de vie", style={"textAlign": "center", "color": "darkblue"}),

        # Filtres interactifs
        html.Div([
            html.Div([
                html.Label("Année(s) :", style={"fontWeight": "bold", "fontSize": "16px"}),
                dcc.Dropdown(
                    id="year-dropdown",
                    options=[{"label": "Toutes les Années", "value": "all"}] +
                            [{"label": str(year), "value": year} for year in available_years],
                    value=["all"], multi=True
                )
            ], style={"width": "48%"}),

            html.Div([
                html.Label("Pays :", style={"fontWeight": "bold", "fontSize": "16px"}),
                dcc.Dropdown(
                    id="country-dropdown",
                    options=[{"label": "Tous les Pays", "value": "all"}] +
                            [{"label": country, "value": country} for country in available_countries],
                    value=["all"], multi=True
                )
            ], style={"width": "48%"})
        ], style={"display": "flex", "justifyContent": "space-between", "margin": "20px"}),

        # Indicateurs principaux (KPI)
        html.Div([
            html.Div(id="kpi-life-expectancy", style={"width": "24%", "textAlign": "center"}),
            html.Div(id="kpi-gdp", style={"width": "24%", "textAlign": "center"}),
            html.Div(id="kpi-schooling", style={"width": "24%", "textAlign": "center"}),
            html.Div(id="kpi-population", style={"width": "24%", "textAlign": "center"})
        ], style={"display": "flex", "justifyContent": "space-around", "margin": "20px"}),

        # Graphiques interactifs
        html.Div([
            dcc.Graph(id="line-graph", style={"width": "48%", "display": "inline-block"}),
            dcc.Graph(id="scatter-graph", style={"width": "48%", "display": "inline-block"})
        ]),

        html.Div([
            dcc.Graph(id="bar-graph", style={"width": "48%", "display": "inline-block"}),
            dcc.Graph(id="bar-adult-mortality", style={"width": "48%", "display": "inline-block"})
        ]),

        html.Div([
            dcc.Graph(id="choropleth-graph", style={"width": "48%", "display": "inline-block"}),
            dcc.Graph(id="bar-life-expectancy-status", style={"width": "48%", "display": "inline-block"})
        ]),

        html.Div([
            dcc.Graph(id="bar-hiv", style={"width": "48%", "display": "inline-block"}),
            dcc.Graph(id="bar-bmi", style={"width": "48%", "display": "inline-block"})
        ])
    ])
