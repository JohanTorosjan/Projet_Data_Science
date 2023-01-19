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

# def makeContinSexeOrientation(df):

#     for column in df:
#             if("filles" not in df[column].name and "garcons" not in df[column].name):
#                 df.pop(column)
#     X=[]
#     Y=[]
#     n=0


#     for column in df:
#         for i in range(0,len(df.index)):
#             if(np.isnan(df[column].values[i])):
#                 occ=0
#             else:
#                 occ=int(df[column].values[i])
#             if "filles" in df[column].name:
#                 fil=df[column].name.split("filles")
#                 name=fil[0]
#                 X.extend(["F"]*occ)
#                 Y.extend([name]*occ)     
#             elif "garcons" in df[column].name:
#                 fil=df[column].name.split("garcons")
#                 name=fil[0]
#                 X.extend(["H"]*occ)
#                 Y.extend([name]*occ)
#             n+=occ
#     data = {
#         'Sexe':X,
#         'Choix':Y
#     }
#     df = pd.DataFrame(data)
#     return df



class contingence:


    def getContigence(df,var1,var2):
        if(var1=="Sexe" and var2=="Orientation"):
            return makeContinSexeOrientation(df,0,False)
        if(var1=="IPS" and var2=="TP"):
            return makeContinIPSTP(df)
        return None
    def getContigenceWithRurality(df,i):
        return makeContinSexeOrientation(df,i,True)
