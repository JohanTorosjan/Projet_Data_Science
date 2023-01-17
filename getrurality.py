import pandas as pd

class getrurality:
    def launch():
        DFdensite=pd.read_csv("data vrac/grille_densite_2019.csv",sep=",",index_col="Libell? des communes")
        DFdensite.index = DFdensite.index.map(str.upper)
        hashtable = DFdensite.to_dict(orient='dict')['Typo degr? de densit?']
        df=pd.read_csv("data vrac/effectifs-dans-les-enseignements-de-specialites-en-1ere-generale-national.csv",sep=";")
        df["Rural"]=0
        for index, row in df.iterrows():
            if row["COMMUNE"] in hashtable:
                df.loc[index,'Rural']=int(hashtable[row["COMMUNE"]])

        DFips=pd.read_csv("data vrac/fr-en-ips_lycees.csv",sep=";",index_col="UAI")
        
        DFips.index = DFips.index.map(str.upper)
        hashtable = DFips.to_dict(orient='dict')['IPS Ensemble GT-PRO']
        df["IPS"]=0.0
        for index, row in df.iterrows():
            if row["NUMERO ETABLISSEMENT"] in hashtable:
                df.loc[index,'IPS']=float(hashtable[row["NUMERO ETABLISSEMENT"]])
        df.to_csv("data cleaned/datawithrural.csv")