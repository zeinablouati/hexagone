import pandas as pd

# Charger les fichiers CSV et effectuer la jointure
def charger_et_joindre_fichiers():
    # Charger le fichier principal `sorties_elfy_output.csv`
    geocodage = pd.read_csv("C:/Users/MSI/Desktop/hexagone/output/geocodage.csv", sep=";")
    geocodage.columns = geocodage.columns.str.strip()  # Nettoyer les noms de colonnes

    # Charger le fichier de référence géographique `tbRefGeo.csv`
    tbRefGeo = pd.read_csv("C:/Users/MSI/Desktop/hexagone/data/tbRefGeo.csv", sep=";", low_memory=False)
    tbRefGeo.columns = tbRefGeo.columns.str.strip()  # Nettoyer les noms de colonnes

    # Afficher les colonnes pour vérifier
    print("geocodage", geocodage.columns)
    print("Colonnes de tbRefGeo:", tbRefGeo.columns)

    # Vérifier si `codgeo` est bien présent dans les deux DataFrames
    if 'codgeo' not in geocodage.columns:
        print("Erreur : La colonne 'codgeo' est absente de geocodage.")
        return None
    if 'codgeo' not in tbRefGeo.columns:
        print("Erreur : La colonne 'codgeo' est absente de tbRefGeo.")
        return None

    # Effectuer la jointure sur la colonne `codgeo`
    df_complet = geocodage.merge(tbRefGeo, on="codgeo", how="left")

    return df_complet

# Obtenir la table complète avec les données consolidées
df_complet = charger_et_joindre_fichiers()
if df_complet is not None:
    # Enregistrer le DataFrame consolidé dans un fichier CSV avec le séparateur `;`
    output_file = "C:/Users/MSI/Desktop/hexagone/output/tb_clients.csv"
    df_complet.to_csv(output_file, sep=';', index=False)
    print(f"La jointure est terminée, et le fichier consolidé est sauvegardé sous le nom : {output_file}")
