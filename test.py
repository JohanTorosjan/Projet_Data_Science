
import pandas as pd
import numpy as np
from fanalysis.ca import CA


def cleanNan(df):
    for column in df:
        if(df[column].hasnans):
            df.pop(column)



##df -> (int,int,int,int)
def getinfoski2(df):
    RuralFemme=0
    RuralHomme=0
    UrbainFemme=0
    UrbainHomme=0


    totalruralHomme=0
    totalruralFemme=0
    totalurbainHomme=0
    totalurbainFemme=0

    for index, row in df.iterrows():
        if(row['Rural']=="Oui"):
            RuralFemme=RuralFemme+row["EFFECTIF TOTAL FILLES"]
            RuralHomme=RuralHomme+row["EFFECTIF TOTAL GARCONS"]

        else:
            UrbainFemme=UrbainFemme+row["EFFECTIF TOTAL FILLES"]
            UrbainHomme=UrbainHomme+row["EFFECTIF TOTAL GARCONS"]


    return(RuralFemme/(RuralFemme+RuralHomme)*100,RuralHomme/(RuralHomme+RuralFemme)*100,UrbainFemme/(UrbainFemme+UrbainHomme)*100,UrbainHomme/(UrbainHomme+UrbainFemme)*100)



def getfillesgarcons(df):
    for column in df:
            if("filles" not in df[column].name and "garcons" not in df[column].name):
                df.pop(column)
    return df

def test(df):
    FemmeColumn=[]
    HommeColumn=[]
    indexes=[]
    for column in df:
        isfille="filles" in df[column].name
        femme=0
        homme=0
        val=0
        for i in range(0,len(df.index)):
            if(np.isnan(df[column].values[i])):
                val=0
            else:
                val=df[column].values[i]
            if(isfille):
                femme=val+femme
                indexname=df[column].name.split("filles")
            else:
                homme=val+homme
                indexname=df[column].name.split("garcons")
       
        if(indexname[0] not in indexes):
            indexes.append(indexname[0])
        if(isfille):
            FemmeColumn.append(femme)
        else:
            HommeColumn.append(homme)
      
    column_values=['Femme','Homme']

    dfnew = pd.DataFrame(list(zip(FemmeColumn,HommeColumn)),columns=column_values,index=indexes)
    return dfnew



def ACP(df):
   pass


df1=pd.read_csv("../data vrac/fr-en-adresse-et-geolocalisation-etablissements-premier-et-second-degre.csv",sep=";")
df1['Commune'] = df1['Commune'].str.upper()
df1["Rural"] = np.where(df1['Commune'].str.contains('MONTPELLIER|NÎMES|PERPIGNAN|TOULOUSE'),"Non","Oui")
df1.rename(columns = {'Code établissement':'NUMERO ETABLISSEMENT'}, inplace = True)


df2=pd.read_csv("../data vrac/effectifs-dans-les-enseignements-de-specialites-en-1ere-generale-national.csv",sep=";")
#df2=df2[df2["REGION ACADEMIQUE"]=="OCCITANIE"]


# df=pd.merge(df1,df2,on='NUMERO ETABLISSEMENT')


#cleanNan(df2)

df3=getfillesgarcons(df2)
#print(df3)

df3=test(df3)
df3.to_csv(path_or_buf="datas.csv",sep=";")
AFC(df3)
#IPS