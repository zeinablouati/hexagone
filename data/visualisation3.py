import pandas as pd
import matplotlib.pyplot as plt

# Charger les données enrichies
file_path = "C:/Users/MSI/Desktop/hexagone/output/jointure_estimee.csv"
df = pd.read_csv(file_path, sep=";")
df.columns = df.columns.str.strip()  # Nettoyer les noms de colonnes

# Filtrer les données pour les colonnes nécessaires
df_filtered = df[["codgeo", "Pays", "e_age"]]

# Remplacer les valeurs manquantes par 0 dans la colonne âge pour éviter les erreurs
df_filtered["e_age"] = df_filtered["e_age"].fillna(0)

# Grouper les données par code géographique et pays pour compter les âges
age_distribution = df_filtered.groupby(["codgeo", "Pays"])["e_age"].value_counts().unstack().fillna(0)

# Limiter aux 10 premiers codes géographiques pour plus de clarté
age_distribution = age_distribution.head(10)

# Graphique à barres empilées pour afficher la répartition de l'âge par code géographique et pays
age_distribution.plot(kind="bar", stacked=True, figsize=(14, 8), colormap="viridis")
plt.title("Répartition de l'Âge par Code Géographique et Pays")
plt.xlabel("Code Géographique et Pays")
plt.ylabel("Nombre d'individus")
plt.xticks(rotation=45)
plt.legend(title="Âge")
plt.show()
