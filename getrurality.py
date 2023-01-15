import pandas as pd


class getrurality:



    def launch():
        indiceRuralite = {"Communes très peu denses": 4, "Communes peu denses": 3, "Communes de densité intermédiaire" : 2, "Communes densément peuplées" : 1}
        DFdensite=pd.read_csv("data vrac/grille_densite_2021.csv",sep=",",index_col="Commune")
        #DFdensite=pd.read_csv("data vrac/grille_densite_2019.csv",sep=",",index_col="Libell? des communes")
        #DFdensite.index = DFdensite.index.map(str.upper)
        #hashtable = DFdensite.to_dict(orient='dict')['Typo degr? de densit?']
        hashtable = DFdensite.to_dict(orient='dict')['Libellé typologie']
        df=pd.read_csv("data vrac/effectifs-dans-les-enseignements-de-specialites-en-1ere-generale-national.csv",sep=";")
        df["Rural"]=0
        for index, row in df.iterrows():
            if row["COMMUNE"] in hashtable:
                df.loc[index,'Rural']=indiceRuralite[hashtable[row["COMMUNE"]]]
                #df.loc[index,'Rural']=int(hashtable[row["COMMUNE"]])
        df.to_csv("data cleaned/datawithrural3.csv")