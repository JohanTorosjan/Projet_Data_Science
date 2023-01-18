import pandas as pd
import unidecode

class getrurality:



    def launch():
        indiceRuralite = {"Communes très peu denses": 4, "Communes peu denses": 3, "Communes de densité intermédiaire" : 2, "Communes densément peuplées" : 1}
        DFdensite=pd.read_csv("data vrac/grille_densite_2021.csv",sep=",")
        #DFdensite=pd.read_csv("data vrac/grille_densite_2019.csv",sep=",",index_col="Libell? des communes")
        for index, row in DFdensite.iterrows():
            ville = DFdensite.loc[index, "NomCommune"]
            DFdensite.loc[index, "NomCommune"] = str(ville).upper()
            DFdensite.loc[index, "NomCommune"] = unidecode.unidecode(DFdensite.loc[index, "NomCommune"])
        #hashtable = DFdensite.to_dict(orient='dict')['Typo degr? de densit?']
        DFdensite.set_index("NomCommune")
        hashtable = DFdensite.to_dict(orient='dict')['Libellé typologie']
        df=pd.read_csv("data vrac/effectifs-dans-les-enseignements-de-specialites-en-1ere-generale-national.csv",sep=";")
        df["Rural"]=0
        print(hashtable)
        for index, row in df.iterrows():
            if row["COMMUNE"] in DFdensite:
                df.loc[index,'Rural']=int(indiceRuralite[DFdensite.loc[row["COMMUNE"], 'Libellé typologie']])
                #df.loc[index,'Rural']=int(indiceRuralite[hashtable[row["COMMUNE"]]])
                #df.loc[index,'Rural']=int(hashtable[row["COMMUNE"]])
            #else:
                #print(row["COMMUNE"])
        df.to_csv("data cleaned/datawithrural3.csv")

        DFips=pd.read_csv("data vrac/fr-en-ips_lycees.csv",sep=";",index_col="UAI")
        
        DFips.index = DFips.index.map(str.upper)
        hashtable = DFips.to_dict(orient='dict')['IPS Ensemble GT-PRO']
        df["IPS"]=0.0
        for index, row in df.iterrows():
            if row["NUMERO ETABLISSEMENT"] in hashtable:
                df.loc[index,'IPS']=float(hashtable[row["NUMERO ETABLISSEMENT"]])
        df.to_csv("data cleaned/datawithrural.csv")
