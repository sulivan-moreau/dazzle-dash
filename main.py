import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def load_data(file_path):
    """
    Charge le fichier CSV et retourne le DataFrame.
    """
    return pd.read_csv(file_path)

def clean_column_names(df):
    """
    Nettoie les noms de colonnes pour les rendre uniformes (snake_case).
    """
    df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()
    return df

def handle_missing_values(df):
    """
    Impute les valeurs manquantes dans les colonnes numériques en utilisant la moyenne.
    """
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        df[col].fillna(df[col].mean(), inplace=True)
    return df

def normalize_columns(df, columns):
    """
    Normalise les colonnes spécifiées entre 0 et 1.
    """
    scaler = MinMaxScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

def add_ratios(df):
    """
    Crée des ratios pour des colonnes spécifiques.
    """
    # Vérifie si 'population' est présente et non nulle pour éviter les divisions par zéro
    if 'population' in df.columns and (df['population'] > 0).all():
        df['infant_deaths_ratio'] = df['infant_deaths'] / df['population'] * 1000
        df['under_five_deaths_ratio'] = df['under-five_deaths'] / df['population'] * 1000
    return df

def remove_outliers(df, column, min_value, max_value):
    """
    Supprime les valeurs aberrantes en fonction d'une plage spécifique pour une colonne donnée.
    """
    df = df[(df[column] >= min_value) & (df[column] <= max_value)]
    return df

def save_data(df, file_path):
    """
    Sauvegarde le DataFrame nettoyé dans un fichier CSV.
    """
    df.to_csv(file_path, index=False)
    print(f"Les données nettoyées ont été exportées sous le nom '{file_path}'.")

def main():
    # Charger les données
    file_path = "Life_expectancy_data.csv"
    df = load_data(file_path)

    # Nettoyer les noms des colonnes
    df = clean_column_names(df)

    # Gérer les valeurs manquantes
    df = handle_missing_values(df)

    # Normaliser certaines colonnes
    columns_to_normalize = ['gdp', 'percentage_expenditure', 'schooling']
    df = normalize_columns(df, columns_to_normalize)

    # Ajouter des ratios pertinents
    df = add_ratios(df)

    # Gérer les valeurs aberrantes (exemple pour 'bmi')
    df = remove_outliers(df, 'bmi', 10, 60)

    # Sauvegarder les données nettoyées
    cleaned_file_path = "Life_expectancy_data_cleaned.csv"
    save_data(df, cleaned_file_path)

if __name__ == "__main__":
    main()
    