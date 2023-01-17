import pandas as pd
import numpy as np
import scipy.stats as st

import matplotlib.pyplot as plt


class ki2:
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

    def launch():
        Y=[]
        X=[]
        for i in range(1,5):
            df=pd.read_csv("data cleaned/datawithrural.csv",sep=",")
            df=df[df["Rural"]==i]
            Y.append(i)
            X.append(ki2.GetInertie(df))
        plt.title("Ecart à l'indépendance en fonction de la ruralité")
        plt.xlabel("Niveau de ruralité")
        plt.ylabel("Inertie (Chi2/n)")
        plt.plot(Y,X)
        plt.savefig("graph out/InertieEnFonctionDeLaRuralite.jpg")