import pandas as pd
import numpy as np




#### STATICS METHODS ####

#Add the columns "TauxParite"
def addTP(df):
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

    return df


#Normalize the IPS 
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
    return df

#Normalize the TP
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




class etl:

    ## Create a data warehouse
    def createdataWarehouse():
        
        #main df
        df=pd.read_csv("dataLake/effectifs-dans-les-enseignements-de-specialites-en-1ere-generale-national.csv",sep=";")
        
        #New columns
        df["Rural"]=0
        df["IPS"]=0.0
        df["TauxParite"]=0.0


        #Add ips
        DFips=pd.read_csv("dataLake/fr-en-ips_lycees.csv",sep=";",index_col="UAI")

        DFips.index = DFips.index.map(str.upper)
        hashtable = DFips.to_dict(orient='dict')['IPS Ensemble GT-PRO']
        for index, row in df.iterrows():
            if row["NUMERO ETABLISSEMENT"] in hashtable:
                df.loc[index,'IPS']=float(hashtable[row["NUMERO ETABLISSEMENT"]])
        
        #Add rural with cleaned datas

        ####### TODO ######


        #Add TP (calculated)
        df = addTP(df)

        ##Normalize quantitatives values
        df=normalizeIPS(df)
        df=normalizeTP(df)

        df.to_csv("dataWarehouse/datas.csv")
        return df
   
    if(__name__=="__main__"):
        createdataWarehouse()
        print("Data Warehouse created")



