import pandas as pd
import numpy as np 

def makeContinSexeOrientation(df,i,rurality):
    if(rurality):
        df=df[df["Rural"]==i]
    for column in df:
            if("filles" not in df[column].name and "garcons" not in df[column].name):
                df.pop(column)
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
            
        if(isfille):
            FemmeColumn.append(femme)
            if(indexname[0] not in indexes):
                    indexes.append(indexname[0])
        else:
            HommeColumn.append(homme)
            if(indexname[0] not in indexes):
                indexes.append(indexname[0])
    column_values=['Femme','Homme']
    dfnew = pd.DataFrame(list(zip(FemmeColumn,HommeColumn)),columns=column_values,index=indexes)
    dfnew = dfnew.drop(dfnew[(dfnew['Femme'] == 0) | (dfnew['Homme'] == 0)].index)


    return dfnew


#Creer un dataframe de la forme 
#  /   IPS      faible  assez faible ...
#TauxP
#-----------------------------------------
#faible         X       X       
#assez faible   X       X
#...
def makeContinIPSTP(df):
    faibleIPS=[0,0,0,0,0]
    assezfaibleIPS=[0,0,0,0,0]
    moyenIPS=[0,0,0,0,0]
    assezeleveIPS=[0,0,0,0,0]
    eleveIPS=[0,0,0,0,0]
   
    for index,row in df.iterrows():
        if(row["IPS"]=="Faible"):
            if(row["TauxParite"]=="Faible"):
              
                faibleIPS[0]=faibleIPS[0]+1
            if(row["TauxParite"]=="Assez faible"):
                faibleIPS[1]=faibleIPS[1]+1
            if(row["TauxParite"]=="Moyen"):
                faibleIPS[2]=faibleIPS[2]+1
            if(row["TauxParite"]=="Assez elevé"):
                faibleIPS[3]=faibleIPS[3]+1
            if(row["TauxParite"]=="Eleve"):
                faibleIPS[4]=faibleIPS[4]+1
        
        if(row["IPS"]=="Assez faible"):
            if(row["TauxParite"]=="Faible"):
                assezfaibleIPS[0]=assezfaibleIPS[0]+1
            if(row["TauxParite"]=="Assez faible"):
                assezfaibleIPS[1]=assezfaibleIPS[1]+1
            if(row["TauxParite"]=="Moyen"):
                assezfaibleIPS[2]=assezfaibleIPS[2]+1
            if(row["TauxParite"]=="Assez elevé"):
                assezfaibleIPS[3]=assezfaibleIPS[3]+1
            if(row["TauxParite"]=="Eleve"):
                assezfaibleIPS[4]=assezfaibleIPS[4]+1
        
        if(row["IPS"]=="Moyen"):
            if(row["TauxParite"]=="Faible"):
                moyenIPS[0]=moyenIPS[0]+1
            if(row["TauxParite"]=="Assez faible"):
                moyenIPS[1]=moyenIPS[1]+1
            if(row["TauxParite"]=="Moyen"):
                moyenIPS[2]=moyenIPS[2]+1
            if(row["TauxParite"]=="Assez elevé"):
                moyenIPS[3]=moyenIPS[3]+1
            if(row["TauxParite"]=="Eleve"):
                moyenIPS[4]=moyenIPS[4]+1
            
        if(row["IPS"]=="Assez elevé"):
            if(row["TauxParite"]=="Faible"):
                assezeleveIPS[0]=assezeleveIPS[0]+1
            if(row["TauxParite"]=="Assez faible"):
                assezeleveIPS[1]=assezeleveIPS[1]+1
            if(row["TauxParite"]=="Moyen"):
                assezeleveIPS[2]=assezeleveIPS[2]+1
            if(row["TauxParite"]=="Assez elevé"):
                assezeleveIPS[3]=assezeleveIPS[3]+1
            if(row["TauxParite"]=="Eleve"):
                assezeleveIPS[4]=assezeleveIPS[4]+1
        
        if(row["IPS"]=="Eleve"):
            if(row["TauxParite"]=="Faible"):
                eleveIPS[0]=eleveIPS[0]+1
            if(row["TauxParite"]=="Assez faible"):
                eleveIPS[1]=eleveIPS[1]+1
            if(row["TauxParite"]=="Moyen"):
                eleveIPS[2]=eleveIPS[2]+1
            if(row["TauxParite"]=="Assez elevé"):
                eleveIPS[3]=eleveIPS[3]+1
            if(row["TauxParite"]=="Eleve"):
                eleveIPS[4]=eleveIPS[4]+1
        
    column_values=['Faible','Assez faible','Moyen','Assez élevé','Elevé']
    dfnew = pd.DataFrame(list(zip(faibleIPS,assezfaibleIPS,moyenIPS,assezeleveIPS,eleveIPS)),columns=column_values,index=column_values)
    return dfnew



#Creer un dataframe de la forme 
#  /   Ruralité 1       2 ...
#TauxP
#-----------------------------------------
#faible         X       X       
#assez faible   X       X
#...
def makeContinRuralTP(df):
    Indice_1=[0,0,0,0,0]
    Indice_2=[0,0,0,0,0]
    Indice_3=[0,0,0,0,0]
    Indice_4=[0,0,0,0,0]

    for index,row in df.iterrows():

       



        if(row["Rural"]==1):
            if(row["TauxParite"]=="Faible"):
                Indice_1[0]=Indice_1[0]+1
            if(row["TauxParite"]=="Assez faible"):
                Indice_1[1]=Indice_1[1]+1   
            if(row["TauxParite"]=="Moyen"):
                Indice_1[2]=Indice_1[2]+1
            if(row["TauxParite"]=="Assez elevé"):
                Indice_1[3]=Indice_1[3]+1
            if(row["TauxParite"]=="Eleve"):
                Indice_1[4]=Indice_1[4]+1
        
        if(row["Rural"]==2):
            
            if(row["TauxParite"]=="Faible"):
                Indice_2[0]=Indice_2[0]+1
            if(row["TauxParite"]=="Assez faible"):
                Indice_2[1]=Indice_2[1]+1
            if(row["TauxParite"]=="Moyen"):
                Indice_2[2]=Indice_2[2]+1
            if(row["TauxParite"]=="Assez elevé"):
                Indice_2[3]=Indice_2[3]+1
            if(row["TauxParite"]=="Eleve"):
                Indice_2[4]=Indice_2[4]+1


        if(row["Rural"]==3):
            if(row["TauxParite"]=="Faible"):
                Indice_3[0]=Indice_3[0]+1
            if(row["TauxParite"]=="Assez faible"):
                Indice_3[1]=Indice_3[1]+1
            if(row["TauxParite"]=="Moyen"):
                Indice_3[2]=Indice_3[2]+1
            if(row["TauxParite"]=="Assez elevé"):
                Indice_3[3]=Indice_3[3]+1
            if(row["TauxParite"]=="Eleve"):
                Indice_3[4]=Indice_3[4]+1
        
        if(row["Rural"]==4):
            if(row["TauxParite"]=="Faible"):
                Indice_4[0]=Indice_4[0]+1
            if(row["TauxParite"]=="Assez faible"):
                Indice_4[1]=Indice_4[1]+1
            if(row["TauxParite"]=="Moyen"):
                Indice_4[2]=Indice_4[2]+1
            if(row["TauxParite"]=="Assez elevé"):
                Indice_4[3]=Indice_4[3]+1
            if(row["TauxParite"]=="Eleve"):
                Indice_4[4]=Indice_4[4]+1
        
    column_values=['Communes densément peuplées','Communes de densité intermédiaire','Communes peu denses','Communes très peu denses']
    index=['Faible','Assez faible','Moyen','Assez élevé','Elevé']
    dfnew = pd.DataFrame(list(zip(Indice_1,Indice_2,Indice_3,Indice_4)),columns=column_values,index=index)
    return dfnew

class contingence:


    def getContigence(df,var1,var2):
        if(var1=="Sexe" and var2=="Orientation"):
            return makeContinSexeOrientation(df,0,False)
        if(var1=="IPS" and var2=="TP"):
            return makeContinIPSTP(df)
        if(var1=="Ruralite" and var2=="TP"):
            return makeContinRuralTP(df)
        return None
    def getContigenceWithRurality(df,i):
        return makeContinSexeOrientation(df,i,True)
