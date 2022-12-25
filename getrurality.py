import pandas as pd



if (__name__=="__main__"):
    DFdensite=pd.read_csv("data vrac/grille_densite_2019.csv",sep=",",index_col="Libell? des communes")
    DFdensite.index = DFdensite.index.map(str.upper)
    hashtable = DFdensite.to_dict(orient='dict')['Typo degr? de densit?']
    df=pd.read_csv("data vrac/effectifs-dans-les-enseignements-de-specialites-en-1ere-generale-national.csv",sep=";")
    df["Rural"]=0
    for index, row in df.iterrows():
        if row["COMMUNE"] in hashtable:
            df.loc[index,'Rural']=int(hashtable[row["COMMUNE"]])
    df.to_csv("data cleaned/datawithrural.csv")