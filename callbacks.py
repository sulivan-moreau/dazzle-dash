from dash import Input, Output
import plotly.express as px
import pandas as pd

def register_callbacks(app, df):
    # Convertir les colonnes en numériques pour éviter les erreurs
    numerical_columns = ["life_expectancy", "gdp", "schooling", "population", 
                        "adult_mortality", "hiv/aids", "bmi", "total_expenditure"]
    for col in numerical_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    @app.callback(
        [Output("kpi-life-expectancy", "children"),
         Output("kpi-gdp", "children"),
         Output("kpi-schooling", "children"),
         Output("kpi-population", "children"),
         Output("line-graph", "figure"),
         Output("scatter-graph", "figure"),
         Output("bar-graph", "figure"),
         Output("bar-adult-mortality", "figure"),
         Output("choropleth-graph", "figure"),
         Output("bar-life-expectancy-status", "figure"),
         Output("bar-hiv", "figure"),
         Output("bar-bmi", "figure")],
        [Input("year-dropdown", "value"),
         Input("country-dropdown", "value")]
    )
    def update_dashboard(selected_years, selected_countries):
        # Filtrage des données
        filtered_df = df.copy()
        if "all" not in selected_years:
            filtered_df = filtered_df[filtered_df['year'].isin(selected_years)]
        if "all" not in selected_countries:
            filtered_df = filtered_df[filtered_df['country'].isin(selected_countries)]

        # Calcul des KPI
        life_expectancy_avg = round(filtered_df['life_expectancy'].mean(), 2)
        gdp_avg = round(filtered_df['gdp'].mean(), 2)
        schooling_avg = round(filtered_df['schooling'].mean(), 2)
        population_total_millions = round(filtered_df['population'].sum() / 1_000_000, 2)

        # Graphique linéaire
        line_fig = px.line(filtered_df, x="year", y="life_expectancy", color="country",
                           title="Évolution de l'espérance de vie", markers=True)

        # Graphique de dispersion PIB vs espérance de vie
        scatter_fig = px.scatter(filtered_df, x="gdp", y="life_expectancy", size="population", color="country",
                                 title="Corrélation entre PIB et Espérance de Vie")

        # Graphique pour taux de scolarisation
        schooling_data = filtered_df.groupby(["country", "status"], as_index=False)["schooling"].mean()
        schooling_data = schooling_data.sort_values(by=["status", "schooling"], ascending=[True, False])
        bar_fig = px.bar(schooling_data, x="schooling", y="country", color="status",
                         title="Taux de scolarisation moyen", orientation="h",
                        #  color_discrete_map={"Developpé": "red", "En developpement": "blue"})

        # Graphique pour Adult Mortality
        adult_mortality_data = filtered_df.groupby(["country", "status"], as_index=False)["adult_mortality"].mean()
        adult_mortality_data = adult_mortality_data.sort_values(by=["status", "adult_mortality"], ascending=[True, False])
        bar_adult_mortality = px.bar(adult_mortality_data, x="adult_mortality", y="country", color="status",
                                     title="Taux de mortalité adulte moyen par pays", orientation="h",
                                     color_discrete_map={"Developpé": "red", "En developpement": "blue"})

        # Carte géographique pour total_expenditure
        choropleth_fig = px.choropleth(filtered_df, 
                                       locations="country", 
                                       locationmode="country names",
                                       color="total_expenditure", 
                                       title="Dépenses de Santé Moyennes par pays",
                                       color_continuous_scale=px.colors.sequential.Plasma)

        # Espérance de vie moyenne par statut
        life_expectancy_status = filtered_df.groupby("status", as_index=False)["life_expectancy"].mean()
        bar_life_expectancy_status = px.bar(life_expectancy_status, x="status", y="life_expectancy", color="status",
                                            title="Espérance de vie moyenne par statut",
                                            color_discrete_map={"Developpé": "red", "En developpement": "blue"})

        # Graphique pour HIV/AIDS
        hiv_data = filtered_df.groupby(["country", "status"], as_index=False)["hiv/aids"].mean()
        hiv_data = hiv_data.sort_values(by=["status", "hiv/aids"], ascending=[True, False])
        bar_hiv = px.bar(hiv_data, x="hiv/aids", y="country", color="status",
                         title="Taux moyen de HIV/AIDS par pays", orientation="h",
                         color_discrete_map={"Developpé": "red", "En developpement": "blue"})

        # Graphique pour IMC (BMI)
        bmi_data = filtered_df.groupby(["country", "status"], as_index=False)["bmi"].mean()
        bmi_data = bmi_data.sort_values(by=["status", "bmi"], ascending=[True, False])
        bar_bmi = px.bar(bmi_data, x="bmi", y="country", color="status",
                         title="IMC moyen par pays", orientation="h",
                         color_discrete_map={"Developpé": "red", "En developpement": "blue"})

        return (f"Espérance de Vie Moyenne : {life_expectancy_avg} ans",
                f"PIB Moyen : {gdp_avg}",
                f"Taux de Scolarisation Moyen : {schooling_avg * 100:.2f} %",
                f"Population Totale : {population_total_millions} M",
                line_fig, scatter_fig, bar_fig, bar_adult_mortality,
                choropleth_fig, bar_life_expectancy_status, bar_hiv, bar_bmi)
