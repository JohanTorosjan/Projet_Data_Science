from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import prince
from contingence import *
import scipy.stats as st



def getCoordonates(df):
    x=[]
    y=[]
    for index,row in df.iterrows():
        x.append(row[0])
        y.append(row[1])
    return x,y


class afc:
    
   
    
    def getCoordA(var1,var2):
        df=pd.read_csv("dataWarehouse/datas.csv",sep=",")  
        dfContigence=contingence.getContigence(df,var1,var2)
        ca = prince.CA(n_components=2,
        n_iter=3,
        copy=True,
        check_input=True,
        engine='auto',
        random_state=42)
        dfContigence.columns.rename(var1, inplace=True)
        dfContigence.index.rename(var2, inplace=True)
        ca = ca.fit(dfContigence)
        ca.transform(dfContigence)
        return getCoordonates(ca.row_coordinates(dfContigence))


    def getCoordB(var1,var2):
        df=pd.read_csv("dataWarehouse/datas.csv",sep=",")  
        dfContigence=contingence.getContigence(df,var1,var2)
        ca = prince.CA(n_components=2,
        n_iter=3,
        copy=True,
        check_input=True,
        engine='auto',
        random_state=42)
        dfContigence.columns.rename(var1, inplace=True)
        dfContigence.index.rename(var2, inplace=True)
        ca = ca.fit(dfContigence)
        ca.transform(dfContigence)
        return getCoordonates(ca.column_coordinates(dfContigence))


    def getDf(var1,var2):
        df=pd.read_csv("dataWarehouse/datas.csv",sep=",")  
        dfContigence=contingence.getContigence(df,var1,var2)
        return dfContigence
    
    def get_inertia(var1,var2):
        df=pd.read_csv("dataWarehouse/datas.csv",sep=",")  
        dfContigence=contingence.getContigence(df,var1,var2)
        ca = prince.CA(n_components=2,
        n_iter=3,
        copy=True,
        check_input=True,
        engine='auto',
        random_state=42)
        dfContigence.columns.rename(var1, inplace=True)
        dfContigence.index.rename(var2, inplace=True)
        ca = ca.fit(dfContigence)
        return ca.explained_inertia_[0],ca.explained_inertia_[1]
