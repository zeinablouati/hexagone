import pandas as pd
import os
# Chemin du fichier CSV d'entrée
input_file = 'C:/Users/MSI/Desktop/hexagone/data/sorties_elfy.csv'
# lecture du fichier d'entrée
sorties_elfy = pd.read_csv(input_file, sep=";", low_memory=False)
sorties_elfy.columns = sorties_elfy.columns.str.strip()  # Nettoyage des noms de colonnes
# Fonction simulée pour enrichir les données avec les codes géographiques
def geocode_simulation(table):
    # Vérifier l'existence des colonnes nécessaires
    if 'Insee' not in table.columns or 'Iris_CodeIris' not in table.columns:
        raise ValueError("Les colonnes 'Insee' et 'Iris_CodeIris' sont nécessaires mais manquantes.")
    # Création des nouvelles colonnes
    table['c_insee'] = table['Insee'].astype(str).str.zfill(5)  # Code INSEE sur 5 caractères
    table['c_iris'] = table['Iris_CodeIris'].fillna('0000').astype(str).str[-4:]  # Code IRIS sur 4 caractères

    # Définir la qualité de l'enrichissement IRIS
    table['c_qualite_iris'] = table['Iris_CodeIris'].apply(lambda x: 1 if pd.notna(x) else 8)
    # Concaténer c_insee et c_iris pour obtenir codgeo
    table['codgeo'] = table['c_insee'] + table['c_iris']
    # Vérification des formats
    assert table['c_insee'].str.len().eq(5).all(), "c_insee n'est pas toujours de 5 caractères"
    assert table['c_iris'].str.len().eq(4).all(), "c_iris n'est pas toujours de 4 caractères"
    assert table['codgeo'].str.len().eq(9).all(), "codgeo n'est pas toujours de 9 caractères"
    return table
# Appel de la fonction de géocodage
sorties_elfy = geocode_simulation(sorties_elfy)
# Enregistrement du fichier de sortie avec toutes les colonnes d'origine plus les nouvelles colonnes
output_file = os.path.join(os.path.dirname(input_file), 'C:/Users/MSI/Desktop/hexagone/output/geocodage.csv')
sorties_elfy.to_csv(output_file, index=False)
print(f"Fichier de sortie avec colonnes ajoutées enregistré : {output_file}")
