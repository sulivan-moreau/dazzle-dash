from dash import Dash
import index  # Importation de la navigation
import layout  # Importation des pages spécifiques
import callbacks  # Importation des interactions

# Initialisation de l'application Dash
app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server  # Serveur pour déploiement

# Définition du layout de l'application (première page : Vue d'ensemble)
app.layout = layout.overview_layout

# Lancement du serveur
if __name__ == '__main__':
    app.run_server(debug=True)
