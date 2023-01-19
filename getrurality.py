import pandas as pd
import unidecode

class getrurality:



    def launch():
        indiceRuralite = {"Communes très peu denses": 4, "Communes peu denses": 3, "Communes de densité intermédiaire" : 2, "Communes densément peuplées" : 1}
        DFdensite=pd.read_csv("data vrac/data sorted/grille_densite_2021.csv",sep=",",index_col="NomCommune")
        print(DFdensite)
        hashtable = DFdensite.to_dict(orient='dict')['Libellé typologie']
        df=pd.read_csv("data vrac/effectifs-dans-les-enseignements-de-specialites-en-1ere-generale-national.csv",sep=";")
        df["Rural"]=0
        for index, row in df.iterrows():
            if row["COMMUNE"] in hashtable:
                df.loc[index,'Rural']=int(indiceRuralite[hashtable[row["COMMUNE"]]])
        df.to_csv("data cleaned/datawithrural3.csv")

        DFips=pd.read_csv("data vrac/fr-en-ips_lycees.csv",sep=";",index_col="UAI")
        
        DFips.index = DFips.index.map(str.upper)
        hashtable = DFips.to_dict(orient='dict')['IPS Ensemble GT-PRO']
        df["IPS"]=0.0
        for index, row in df.iterrows():
            if row["NUMERO ETABLISSEMENT"] in hashtable:
                df.loc[index,'IPS']=float(hashtable[row["NUMERO ETABLISSEMENT"]])
        df.to_csv("data cleaned/datawithrural.csv")
