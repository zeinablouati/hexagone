import pandas as pd

# Charger les fichiers CSV et effectuer la jointure
def charger_et_joindre_fichiers():
    # Charger le fichier principal `sorties_elfy_output.csv`
    Enrichissement_géomarketing = pd.read_csv("C:/Users/MSI/Desktop/hexagone/output/enrichi_age.csv", sep=";")
    Enrichissement_géomarketing.columns = Enrichissement_géomarketing.columns.str.strip()  # Nettoyer les noms de colonnes

    # Charger le fichier de référence géographique `tbRefGeo.csv`
    coeff_enfants_coeff_enfants = pd.read_csv("C:/Users/MSI/Desktop/hexagone/data/coeff_enfants_coeff_enfants.csv", sep=";", low_memory=False)
    coeff_enfants_coeff_enfants.columns = coeff_enfants_coeff_enfants.columns.str.strip()  # Nettoyer les noms de colonnes

    # Afficher les colonnes pour vérifier
    print("Colonnes de Enrichissement_géomarketing:", Enrichissement_géomarketing.columns)
    print("Colonnes de coeff_enfants_coeff_enfants:", coeff_enfants_coeff_enfants.columns)

    # Vérifier si `codgeo` est bien présent dans les deux DataFrames
    if 'codgeo' not in Enrichissement_géomarketing.columns:
        print("Erreur : La colonne 'codgeo' est absente de Enrichissement_géomarketing.")
        return None
    if 'codgeo' not in coeff_enfants_coeff_enfants.columns:
        print("Erreur : La colonne 'codgeo' est absente de coeff_enfants_coeff_enfants.")
        return None

    # Effectuer la jointure sur la colonne `codgeo`
    df_complet = Enrichissement_géomarketing.merge(coeff_enfants_coeff_enfants, on="codgeo", how="left")

    return df_complet

# Obtenir la table complète avec les données consolidées
df_complet = charger_et_joindre_fichiers()
if df_complet is not None:
    # Enregistrer le DataFrame consolidé dans un fichier CSV avec le séparateur `;`
    output_file = "C:/Users/MSI/Desktop/hexagone/output/jointure_enfants_age.csv"
    df_complet.to_csv(output_file, sep=';', index=False)
    print(f"La jointure est terminée, et le fichier consolidé est sauvegardé sous le nom : {output_file}")
