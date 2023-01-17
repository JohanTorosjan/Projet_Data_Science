from pandasql import sqldf
from ki2 import *
import pandas as pd



df=pd.read_csv("data cleaned/datawithrural.csv",sep=",")
df["TauxParite"]=0.0

for index,row in df.iterrows():
    
    totalfilles=0
    matieresScientifiquesfilles=0

    for column in df:
        part=df[column].name.split("-")
        if  "filles" in df[column].name and len(part)>1 and not (np.isnan(row[column])):
            totalfilles=totalfilles+row[column]
        matieresNonEgales="MATHEMATIQUES" in df[column].name or "PHYSIQUE CHIMIE" in df[column].name or "SCIENCE DE L INGENIEUR" in df[column].name or "NUMERIQUE ET SCIENCES INFORMATIQUES" in df[column].name
        if ("filles" in df[column].name) and (matieresNonEgales)  and ("SCIENCES DE LA VIE ET DE LA TERRE"  not in df[column].name and "LANGUES" not in df[column].name):
           matieresScientifiquesfilles=matieresScientifiquesfilles+row[column]
    if(totalfilles>0):
        df.loc[index,'TauxParite']=(matieresScientifiquesfilles/totalfilles)*100

for index,row in df.iterrows():
    if(np.isnan(row["TauxParite"]) or row["TauxParite"]==0.0):
        df=df.drop(index=index)



def normalizeIPS(df):
    faible=[0,np.percentile(df["IPS"],20)]
    assezfaible=[np.percentile(df["IPS"],20),np.percentile(df["IPS"],40)]
    moyen=[np.percentile(df["IPS"],40),np.percentile(df["IPS"],60)]
    assezeleve=[np.percentile(df["IPS"],60),np.percentile(df["IPS"],80)]
    eleve=[np.percentile(df["IPS"],80),np.percentile(df["IPS"],100)]
    for index,row in df.iterrows():
        if(row["IPS"]>faible[0] and row["IPS"]<faible[1]):
            df.loc[index,'IPS']="Faible"
        elif(row["IPS"]>assezfaible[0] and row["IPS"]<assezfaible[1]):
            df.loc[index,'IPS']="Assez faible"
        elif(row["IPS"]>moyen[0] and row["IPS"]<moyen[1]):
            df.loc[index,'IPS']="Moyen"
        elif(row["IPS"]>assezeleve[0] and row["IPS"]<assezeleve[1]):
            df.loc[index,'IPS']="Assez elevé"
        elif(row["IPS"]>eleve[0] and row["IPS"]<eleve[1]):
            df.loc[index,'IPS']="Eleve"
        print(row["IPS"])
    return df

def normalizeTP(df):
    faible=[0,np.percentile(df["TauxParite"],20)]
    assezfaible=[np.percentile(df["TauxParite"],20),np.percentile(df["TauxParite"],40)]
    moyen=[np.percentile(df["TauxParite"],40),np.percentile(df["TauxParite"],60)]
    assezeleve=[np.percentile(df["TauxParite"],60),np.percentile(df["TauxParite"],80)]
    eleve=[np.percentile(df["TauxParite"],80),np.percentile(df["TauxParite"],100)]
    for index,row in df.iterrows():
        if(row["TauxParite"]>faible[0] and row["TauxParite"]<faible[1]):
            df.loc[index,'TauxParite']="Faible"
        elif(row["TauxParite"]>assezfaible[0] and row["TauxParite"]<assezfaible[1]):
            df.loc[index,'TauxParite']="Assez faible"
        elif(row["TauxParite"]>moyen[0] and row["TauxParite"]<moyen[1]):
            df.loc[index,'TauxParite']="Moyen"
        elif(row["TauxParite"]>assezeleve[0] and row["TauxParite"]<assezeleve[1]):
            df.loc[index,'TauxParite']="Assez elevé"
        elif(row["TauxParite"]>eleve[0] and row["TauxParite"]<eleve[1]):
            df.loc[index,'TauxParite']="Eleve"
    return df

df=normalizeIPS(df)
df=normalizeTP(df)
df.to_csv("data cleaned/datawithall.csv")
# # df=df[df["TauxParite"]>20]
# # print(len(df))
# # df=df[df["IPS"]<100]
# # print(len(df))
# print(np.percentile(df["TauxParite"],50))
# print(len(df))
# df=df[df["IPS"]<100]
# print(len(df))
