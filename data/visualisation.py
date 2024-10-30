import pandas as pd
import matplotlib.pyplot as plt

# Charger les données enrichies
file_path = "C:/Users/MSI/Desktop/hexagone/output/jointure_enfants_age.csv"
df = pd.read_csv(file_path, sep=";")
df.columns = df.columns.str.strip()  # Nettoyer les noms de colonnes

# Remplacer les valeurs manquantes par 0 dans les colonnes de niveaux d'études
df[["< Bac", "Bac-Bac + 2", "> Bac + 2"]] = df[["< Bac", "Bac-Bac + 2", "> Bac + 2"]].fillna(0)

# Agréger les niveaux d'études par pays en sommant les valeurs pour chaque niveau d'étude
etude_par_pays = df.groupby("Pays")[["< Bac", "Bac-Bac + 2", "> Bac + 2"]].sum()

# Graphique en secteurs (pie chart) pour chaque pays (limité aux 5 premiers pour plus de clarté)
for pays in etude_par_pays.index[:5]:  # Limiter aux 5 premiers pays
    plt.figure(figsize=(8, 6))
    niveaux_etude = etude_par_pays.loc[pays]
    niveaux_etude.plot(kind="pie", autopct='%1.1f%%', startangle=90, colors=["skyblue", "salmon", "lightgreen"])
    plt.title(f"Répartition des Niveaux d'Études dans le Pays : {pays}")
    plt.ylabel("")  # Retirer l'étiquette de l'axe y pour un meilleur affichage
    plt.show()

# Graphique à barres empilées pour comparer les niveaux d'études entre les principaux pays
etude_par_pays.head(10).plot(kind="bar", stacked=True, figsize=(12, 8), color=["skyblue", "salmon", "lightgreen"])
plt.title("Comparaison des Niveaux d'Études entre Pays (Top 10)")
plt.xlabel("Pays")
plt.ylabel("Nombre total de personnes")
plt.xticks(rotation=45)
plt.legend(title="Niveau d'Étude")
plt.show()
