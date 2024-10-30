import pandas as pd

# Charger le fichier CSV en précisant le séparateur
tb_clients = pd.read_csv('C:/Users/MSI/Desktop/hexagone/output/tb_clients.csv', sep=';')

# Afficher les noms des colonnes pour vérifier leur structure
print(tb_clients.columns)

# Vérifiez et ajustez les colonnes d'estimation ici
def estimer_sexe(row):
    if row['F'] > row['M']:
        return 'F'
    elif row['M'] > row['F']:
        return 'M'
    else:
        return 'Inconnu'

def estimer_age(row):
    # Logique simplifiée pour illustrer le calcul de l'âge estimé
    for col in ['0 à 5 ans', '6 à 10 ans', '11 à 17 ans', '18 à 24 ans', 
                '25 à 39 ans', '40 à 54 ans', '55 à 64 ans', '65 à 79 ans', 'Plus de 80 ans']:
        if row[col] > 0:
            return col
    return 'Inconnu'

# Application des fonctions d'estimation
tb_clients['e_sexe'] = tb_clients.apply(estimer_sexe, axis=1)
tb_clients['e_age'] = tb_clients.apply(estimer_age, axis=1)
tb_clients['e_top_age_ok'] = tb_clients['e_age'].apply(lambda x: 2 if x != 'Inconnu' else 3)

# Sauvegarder dans un nouveau fichier CSV
tb_clients.to_csv('C:/Users/MSI/Desktop/hexagone/output/enrichi_age.csv', sep=';', index=False)

print("Le fichier enrichi a été exporté avec succès.")
