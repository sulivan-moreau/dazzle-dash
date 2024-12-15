from dash import Dash, html
import index  # Page principale

# Initialisation de l'application Dash
app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server

# Définition du layout principal
app.layout = html.Div([
    index.layout  # Utilise le layout principal importé
])

if __name__ == "__main__":
    app.run_server(debug=True)
