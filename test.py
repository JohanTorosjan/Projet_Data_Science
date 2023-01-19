from pandasql import sqldf
from ki2 import *
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import prince

def getCoordonates(df):
    x=[]
    y=[]
    for index,row in df.iterrows():
        x.append(row[0])
        y.append(row[1])
    return x,y




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


#Creer un dataframe de la forme 
#  /   IPS      faible  assez faible ...
#TauxP
#-----------------------------------------
#faible         X       X       
#assez faible   X       X
#...
def makeContin(df):

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
    print(dfnew)
    st_chi2, st_p, st_dof, st_exp = st.chi2_contingency(dfnew)
    print("\nki2: "+str(st_chi2))
    print("p value: "+str(st_p))
    
    



    dc=pd.DataFrame(pd.get_dummies(dfnew[['Faible','Assez faible','Moyen','Assez élevé','Elevé']]))

    print(dfnew)
    print("-----")
    print(dc)
    ca = prince.CA(n_components=2,
    n_iter=3,
    copy=True,
    check_input=True,
    engine='auto',
    random_state=42)
    dc.columns.rename('IPS', inplace=True)
    dc.index.rename('Taux de parite', inplace=True)
    ca = ca.fit(dc)



    print(type(ca.row_coordinates(dc)))
    print(ca.row_coordinates(dc))
    print(ca.column_coordinates(dc))

    
    Dips=pd.DataFrame(ca.row_coordinates(dc))

    X_ips,Y_ips=getCoordonates(Dips)

    print(X_ips)
    print(Y_ips)
    ipsplt=plt.scatter(X_ips,Y_ips,marker = 'o', c = 'lime')
    

    plt.axvline(x=0, color='blue')
    plt.axhline(y=0, color='blue')
    for u, txt in enumerate(dc.index):
        plt.annotate(txt, (X_ips[u], Y_ips[u]))
    Dtp=pd.DataFrame(ca.column_coordinates(dc))

    X_tp,Y_tp=getCoordonates(Dtp)
    tpplt=plt.scatter(X_tp,Y_tp, marker = 'X', c = 'red')

    
    plt.axvline(x=0, color='blue')
    plt.axhline(y=0, color='blue')
    for u, txt in enumerate(dc.index):
        plt.annotate(txt, (X_tp[u], Y_tp[u]))
    plt.legend([ipsplt,tpplt],['IPS','Taux de parité'])
    plt.show()
    



#     dc.head()
#     print(dc)
#     mca_df=MCA(dc,benzecri=False)
# # Valeurs singulières
#     print(mca_df.L)
# # Composantes principales des colonnes (modalités) print(mca_df.fs_c())
# # Premier plan principal
#     col=[1,1,2,2,2,3,3,5,5,5,6,6,6,7,7,7]
#     print(mca_df.fs_c())
#     plt.scatter(mca_df.fs_c()[:, 0],mca_df.fs_c()[:, 1],c=col)
#     for i,j,nom in zip(mca_df.fs_c()[:,0],mca_df.fs_c()[:,1],dc.columns):
#         plt.text(i,j,nom)
#     plt.show()
#     #   Valeurs singulières

#     # scaler = StandardScaler()
        
#     # X_scaled = scaler.fit_transform(dfnew)
#     # pca = PCA()
    #     # Appliquer l'afc aux données normalisées
    # X_pca = pca.fit_transform(X_scaled)
    #     # Récupération des coordonnées des points dans le nouveau plan factoriel
    # x, y = X_pca[:, 0], X_pca[:, 1]



    # for u, txt in enumerate(dfnew.index):
    #         plt.annotate(txt, (x[u], y[u]))
    
    # print(x)
    # print(y)
    # v1,v2,v3,v4,v5= pca.components_
    # print(v1)
    # print(v2)
    # print(v3)
    # print(v4)
    # print(v5)
    
        # Création du scatter plot
    # plt.scatter(x, y)
    # plt.plot(v1[0],v1[1])
    # plt.annotate("Faible",(v1[0],v1[1]))
    # plt.plot(v2[0],v2[1])
    # plt.annotate("Assez Faible",(v2[0],v2[1]))
    # plt.plot(v3[0],v3[1])
    # plt.annotate("Moyen",(v3[0],v3[1]))
    # plt.plot(v4[0],v4[1])
    # plt.annotate("Assez élevé",(v4[0],v4[1]))
    # plt.plot(v5[0],v5[1])
    # plt.annotate("Elevé",(v5[0],v5[1]))

    #plt.show()


df=normalizeIPS(df)
df=normalizeTP(df)
df.to_csv("data cleaned/datawithall.csv")
makeContin(df)
# # df=df[df["TauxParite"]>20]
# # print(len(df))
# # df=df[df["IPS"]<100]
# # print(len(df))
# print(np.percentile(df["TauxParite"],50))
# print(len(df))
# df=df[df["IPS"]<100]
# print(len(df))
