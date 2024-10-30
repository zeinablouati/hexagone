import pandas as pd

# Charger les données
df = pd.read_csv("C:/Users/MSI/Desktop/hexagone/output/jointure_enfants_age.csv", sep=";")
df.columns = df.columns.str.strip()  # Nettoyer les noms de colonnes

# Ajouter toutes les nouvelles colonnes spécifiées
columns_to_add = [
    "e_PCS", "c_indice_qualite_pcs", "e_situation_fam", "c_indice_qualite_menage",
    "e_etudes", "c_indice_qualite_formation", "h_ind", "locat_hlm", 
    "e_habitat_individuel", "e_habitat_hlm", "e_statut_hab", "c_indice_qualite_logement",
    "e_proba_1_enfant", "e_proba_2_enfants", "e_proba_m5", "e_proba_5_10", 
    "e_proba_10_15", "e_proba_15_20", "e_typo_commune_2010", "e_taille_commune", 
    "e_seg_commerces", "e_sous_seg_commerces", "e_seg_logement", "i_rev", "e_revenus", 
    "e_decile", "c_indice_qualite_rev", "e_dept", "e_region_9", "e_Region", 
    "e_lib_dept", "e_reg"
]
for col in columns_to_add:
    df[col] = None

# Estimation de e_etudes (niveau d'études) à partir des colonnes d'éducation
def estimer_e_etudes(row):
    niveaux = ["< Bac", "Bac-Bac + 2", "> Bac + 2"]
    valeurs = row[niveaux].dropna().values if all(n in df.columns for n in niveaux) else []
    if valeurs.size == 0:
        return None
    proba = valeurs / valeurs.sum()
    return niveaux[proba.argmax()]

df["e_etudes"] = df.apply(estimer_e_etudes, axis=1)

# Calcul de c_indice_qualite_formation pour l'estimation des études
def indice_qualite_etudes(row):
    niveaux = ["< Bac", "Bac-Bac + 2", "> Bac + 2"]
    valeurs = row[niveaux].dropna().values if all(n in df.columns for n in niveaux) else []
    if valeurs.size == 0:
        return None
    return valeurs.std() / valeurs.sum()

df["c_indice_qualite_formation"] = df.apply(indice_qualite_etudes, axis=1)

# Probabilité d'habiter en habitation individuelle (h_ind) et en HLM (locat_hlm)
def estimer_prob_habitation(row):
    if row["Ensemble des logements"] == 0:
        return None, None
    h_ind = row["Individuel"] / row["Ensemble des logements"]
    locat_hlm = row["HLM"] / row["Ensemble des logements"]
    return h_ind, locat_hlm

# Appliquer la fonction si les colonnes nécessaires sont présentes
if "Individuel" in df.columns and "Ensemble des logements" in df.columns and "HLM" in df.columns:
    df["h_ind"], df["locat_hlm"] = zip(*df.apply(estimer_prob_habitation, axis=1))
else:
    print("Colonnes nécessaires pour l'habitation individuelle et HLM manquantes.")

# Enregistrement du DataFrame mis à jour avec toutes les colonnes dans un fichier CSV
output_file = "C:/Users/MSI/Desktop/hexagone/output/jointure_estimee.csv"
df.to_csv(output_file, sep=';', index=False)
print(f"Les estimations sont terminées, et le fichier consolidé est sauvegardé sous le nom : {output_file}")
