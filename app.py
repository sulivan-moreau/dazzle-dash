import dash
from dash import Input, Output
import pandas as pd
from layout import create_layout
from callbacks import register_callbacks

# Initialisation de l'application Dash
app = dash.Dash(__name__)

# Chargement des données
df = pd.read_csv("lifeExpectancyClean.csv")

# Définir le layout
app.layout = create_layout(df)

# Enregistrement des callbacks
register_callbacks(app, df)

# Lancer l'application
if __name__ == "__main__":
    app.run_server(debug=True)
