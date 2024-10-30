import pandas as pd
import matplotlib.pyplot as plt

# Charger les données enrichies
file_path = "C:/Users/MSI/Desktop/hexagone/output/jointure_enfants_age.csv"
df = pd.read_csv(file_path, sep=";")
df.columns = df.columns.str.strip()  # Nettoyer les noms de colonnes

# Filtrer pour le pays France uniquement
df_france = df[df["Pays"] == "FRA"]

# Comptage des occurrences par ville
ville_counts = df_france["Ville"].value_counts()

# Limiter aux 10 premières villes pour un affichage plus clair
plt.figure(figsize=(12, 8))
ville_counts.head(10).plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Répartition des Villes pour le Pays : FRA (Top 10)")
plt.xlabel("Ville")
plt.ylabel("Nombre d'enregistrements")
plt.xticks(rotation=45)
plt.show()
