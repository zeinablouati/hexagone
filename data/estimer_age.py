import pandas as pd

# Charger les données avec l'encodage approprié
tb_clients = pd.read_csv("C:/Users/MSI/Desktop/hexagone/data/tb_clients.csv", sep=";", encoding='ISO-8859-1')

# Renommer les colonnes pour corriger les caractères spéciaux
tb_clients.rename(columns={
    '0 Ã  5 ans': '0 à 5 ans',
    '6 Ã  10 ans': '6 à 10 ans',
    '11 Ã  17 ans': '11 à 17 ans',
    '18 Ã  24 ans': '18 à 24 ans',
    '25 Ã  39 ans': '25 à 39 ans',
    '40 Ã  54 ans': '40 à 54 ans',
    '55 Ã  64 ans': '55 à 64 ans',
    '65 Ã  79 ans': '65 à 79 ans',
    'Plus de 80 ans': '80+ ans'
}, inplace=True)

# Définir les âges moyens pour chaque intervalle
age_moyenne = {
    "0 à 5 ans": 2.5,
    "6 à 10 ans": 8,
    "11 à 17 ans": 14,
    "18 à 24 ans": 21,
    "25 à 39 ans": 32,
    "40 à 54 ans": 47,
    "55 à 64 ans": 59.5,
    "65 à 79 ans": 72,
    "80+ ans": 85
}

# Fonction pour estimer l'âge
def estimer_age(row):
    for col, age in age_moyenne.items():
        if row[col] > 0:
            return age
    return None

# Appliquer la fonction pour créer une nouvelle colonne "age_estimé"
tb_clients["age_estimé"] = tb_clients.apply(estimer_age, axis=1)

# Filtrer pour ne garder que les lignes où "age_estimé" n'est pas vide
tb_clients_filtered = tb_clients.dropna(subset=["age_estimé"])

# Enregistrer les résultats filtrés dans un nouveau fichier CSV
output_path = "C:/Users/MSI/Desktop/hexagone/data/tb_clients_age_estime_filtre.csv"
tb_clients_filtered[["Nom", "codgeo", "age_estimé"]].to_csv(output_path, index=False, sep=";")

print(f"Le fichier filtré avec l'estimation des âges a été enregistré sous : {output_path}")
