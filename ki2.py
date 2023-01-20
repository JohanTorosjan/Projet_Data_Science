import pandas as pd 
import numpy as np
from contingence import *
import scipy.stats as st







def GetInertie(df):
    for column in df:
            if("filles" not in df[column].name and "garcons" not in df[column].name):
                df.pop(column)
    X=[]
    Y=[]
    n=0
    for column in df:
        for i in range(0,len(df.index)):
            if(np.isnan(df[column].values[i])):
                occ=0
            else:
                occ=int(df[column].values[i])
            if "filles" in df[column].name:
                fil=df[column].name.split("filles")
                name=fil[0]
                X.extend(["F"]*occ)
                Y.extend([name]*occ)
            elif "garcons" in df[column].name:
                fil=df[column].name.split("garcons")
                name=fil[0]
                X.extend(["H"]*occ)
                Y.extend([name]*occ)
            n+=occ
    data = {
        'Sexe':X,
        'Choix':Y
    }
    df = pd.DataFrame(data)
    X = "Sexe"
    Y = "Choix"
    cont = df[[X, Y]].pivot_table(index=X, columns=Y, aggfunc=len).fillna(0).copy().astype(int)
    cont = cont.astype(int)
    st_chi2, st_p, st_dof, st_exp = st.chi2_contingency(cont)
    return(st_chi2/n)

def getKi2fromCont(df):
    st_chi2, st_p, st_dof, st_exp = st.chi2_contingency(df)
    return st_chi2


class ki2:
    def getCoordInertie():
        Y=[]
        X=[]    
        for i in range(1,5):

            ### TODO ###
            df=pd.read_csv("data cleaned/datawithrural.csv",sep=",")

            df=df[df["Rural"]==i]
            Y.append(i)
            X.append(GetInertie(df))
        return X,Y
    

    def getKi2(var1,var2):
        df=pd.read_csv("dataWarehouse/datas.csv",sep=",")  
        dfContigence=contingence.getContigence(df,var1,var2)
        return getKi2fromCont(dfContigence)

