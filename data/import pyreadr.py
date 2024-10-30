import pyreadr
import pandas as pd


result = pyreadr.read_r("coeff_menage.RData")




for key in result.keys():
    print(key)




data = result["coeff_menage"]


data.to_excel("coeff_menage.xlsx", index=False)


print("Fichier Excel créé avec succès.")

