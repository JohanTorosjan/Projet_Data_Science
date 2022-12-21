
import string
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def cleanforacm(df):
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
       
        if(indexname[0] not in indexes):
            indexes.append(indexname[0])
        if(isfille):
            FemmeColumn.append(femme)
        else:
            HommeColumn.append(homme)
      
    column_values=['Femme','Homme']
    dfnew = pd.DataFrame(list(zip(FemmeColumn,HommeColumn)),columns=column_values,index=indexes)
    return dfnew


df=pd.read_csv("../data vrac/effectifs-dans-les-enseignements-de-specialites-en-1ere-generale-national.csv",sep=";")
# df=df[df["REGION ACADEMIQUE"]=="OCCITANIE"]


def acm(df):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df)

    pca = PCA()

    # Appliquer l'acm aux données normalisées
    X_pca = pca.fit_transform(X_scaled)

     # Récupération des coordonnées des points dans le nouveau plan factoriel
    x, y = X_pca[:, 0], X_pca[:, 1]

    # Création du scatter plot
    plt.scatter(x, y)


    for i, txt in enumerate(df.index):
        part=txt.split("-")
        txt=" ".join(part[1:])
        plt.annotate(txt, (x[i], y[i]))

    # Ajout d'étiquettes aux axes



    valpropres=pca.explained_variance_

    print("Val propre 1: "+str(valpropres[0]))
    print("Val propre 2: "+str(valpropres[1]))
    
    cp1=pca.explained_variance_ratio_[0]*100
    cp2=pca.explained_variance_ratio_[1]*100
    plt.xlabel('Composante 1('+str(cp1)+")%")
    plt.ylabel('Composante 2 ('+str(cp2)+")%")
    plt.title('Nuage des matières')
    plt.axvline(x=0, color='blue')
    plt.axhline(y=0, color='blue')
    # Affichage du graphe
    plt.show()

    v1, v2 = pca.components_

    # Tracé des axes du nouveau plan factoriel
    plt.arrow(0, 0, v1[0], v1[1], head_width=0.01, head_length=0.01, color='red')
    plt.arrow(0, 0, v2[0], v2[1], head_width=0.01, head_length=0.01, color='red')
    plt.text(v1[0], v1[1], 'Femme', color='red', fontsize=12)
    plt.text(v2[0], v2[1], 'Homme', color='red', fontsize=12)
    plt.axvline(x=0, color='blue')
    plt.axhline(y=0, color='blue')
    plt.xlabel('Composante 1('+str(cp1)+")%")
    plt.ylabel('Composante 2 ('+str(cp2)+")%")
    plt.title('Nuage des variables')
    # Affichage du graphe
    plt.show()
    



df=cleanforacm(df)
acm(df)


