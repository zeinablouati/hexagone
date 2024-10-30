import pandas as pd
import matplotlib.pyplot as plt

# Charger les données enrichies
file_path = "C:/Users/MSI/Desktop/hexagone/output/jointure_enfants_age.csv"
df = pd.read_csv(file_path, sep=";")
df.columns = df.columns.str.strip()  # Nettoyer les noms de colonnes

# Remplacer les valeurs manquantes par 0 pour éviter les erreurs
df[["Total", "Individuel", "Couple avec enfant", "Couple sans enfant", "Famille monoparentale"]] = \
    df[["Total", "Individuel", "Couple avec enfant", "Couple sans enfant", "Famille monoparentale"]].fillna(0)

# Agréger les données pour obtenir la somme des différentes catégories
population_par_type = df[["Total", "Individuel", "Couple avec enfant", "Couple sans enfant", "Famille monoparentale"]].sum()

# Graphique en secteur pour visualiser la proportion de chaque type de ménage par rapport à la population totale
plt.figure(figsize=(8, 8))
population_par_type[1:].plot(kind="pie", autopct='%1.1f%%', startangle=90, colors=["skyblue", "salmon", "lightgreen", "orange"])
plt.title("Comparaison des Types de Ménages par Rapport à la Population Totale")
plt.ylabel("")  # Retirer l'étiquette de l'axe y pour un meilleur affichage
plt.legend(["Individuel", "Couple avec enfant", "Couple sans enfant", "Famille monoparentale"])
plt.show()

# Graphique à barres montrant la comparaison entre la population totale et les différents types de ménages
plt.figure(figsize=(10, 6))
population_par_type.plot(kind="bar", color=["gray", "skyblue", "salmon", "lightgreen", "orange"], edgecolor="black")
plt.title("Comparaison de la Population Totale et des Types de Ménages")
plt.xlabel("Type de Population")
plt.ylabel("Nombre de ménages")
plt.xticks(rotation=45)
plt.legend(title="Type de Population")
plt.show()
