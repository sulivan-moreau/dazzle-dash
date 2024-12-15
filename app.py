from dash import Dash
import index  # Importation de la navigation
import callbacks  # Importation des interactions

# Initialisation de l'application Dash
app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server  # Serveur pour déploiement

# Définition du layout de l'application avec navigation
app.layout = index.layout  # Utilise le layout avec la navigation

# Lancement du serveur
if __name__ == '__main__':
    app.run_server(debug=True)
