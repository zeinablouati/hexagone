import pandas as pd

# Fonction pour charger et joindre les trois fichiers
def charger_et_joindre_trois_fichiers():
    # Charger chaque fichier avec sa colonne de jointure spécifique
    fichier_logement = pd.read_csv("C:/Users/MSI/Desktop/hexagone/data/coeff_logement_coeff_logement.csv", sep=";")
    fichier_logement.columns = fichier_logement.columns.str.strip()
    
    fichier_formation = pd.read_csv("C:/Users/MSI/Desktop/hexagone/data/coeff_formation_coeff_formation.csv", sep=";")
    fichier_formation.columns = fichier_formation.columns.str.strip()
    
    fichier_menage = pd.read_csv("C:/Users/MSI/Desktop/hexagone/data/coeff_menage_coeff_menage.csv", sep=";")
    fichier_menage.columns = fichier_menage.columns.str.strip()

    # Joindre les fichiers successivement
    df_temp = fichier_logement.merge(fichier_formation, left_on="match_log", right_on="match_formation", how="outer")
    df_complet = df_temp.merge(fichier_menage, left_on="match_log", right_on="match_menage", how="outer")

    return df_complet

# Obtenir la table complète avec les données consolidées
df_complet = charger_et_joindre_trois_fichiers()
if df_complet is not None:
    # Enregistrer le DataFrame consolidé dans un fichier CSV avec le séparateur `;`
    output_file = "C:/Users/MSI/Desktop/hexagone/output/jointure_log_men_form.csv"
    df_complet.to_csv(output_file, sep=';', index=False)
    print(f"La jointure est terminée, et le fichier consolidé est sauvegardé sous le nom : {output_file}")
