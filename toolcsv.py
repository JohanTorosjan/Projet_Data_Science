import pandas as pd
import unidecode


print("slt")
DFdensite=pd.read_csv("data vrac/grille_densite_2021.csv",sep=",")
for index, row in DFdensite.iterrows():
    ville = DFdensite.loc[index, "NomCommune"]
    ville = str(ville).upper()
    ville = unidecode.unidecode(ville)
    DFdensite.loc[index, "NomCommune"] = ville
print(DFdensite)
DFdensite.to_csv("data vrac/data sorted/grille_densite_2021.csv")