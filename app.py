# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from afc import *
from ki2 import * 

app = Dash(__name__)


def showAfc(paramAfc1,paramAfc2):
    x1,y1 = afc.getCoordA(paramAfc1,paramAfc2)
    x2,y2 = afc.getCoordB(paramAfc1,paramAfc2)
    dataFrame = afc.getDf(paramAfc1,paramAfc2)

    # Création du scatter plot
    inertie1,inertie2 = afc.get_inertia(paramAfc1,paramAfc2)
    xlabel="Composante 1("+str(inertie1)+")%"
    ylabel="Composante 2 ("+str(inertie2)+")%"
    #Première comoposante
    fig = px.scatter(x=x1,y=y1, labels={
                    "x": xlabel,
                    "y": ylabel,
                },hover_name=dataFrame.index)  
    #Deuxième composante
    fig=fig.add_scatter(x=x2,y=y2,hovertext=dataFrame.columns.values)     
    title='Nuage des '+paramAfc1+'et des'+paramAfc2
    fig.update_layout(title_text=title)
    return fig

def showEcartInertieRuralite():
    x,y=ki2.getCoordInertie()
    fig = px.scatter(x=y,y=x, labels={
                    "x": "Taux de ruralité",
                    "y": "Ecart à l'inertie",
                })
    title="Ecart à l'indépendance selon le taux de ruralité"
    fig.update_layout(title_text=title)
    return fig


#fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children="Etude des disparités entre genres dans l'orientation scolaire"),

    html.Div(children=[
        html.H2(children="Présentation de l'étude"),
        html.P(children="Présentation de l'étude blablabla...") ##### 01 #####
    ]),

    html.Div(children=[
        html.H2(children="Observation des disparités"),
        #D'abord on montre qu'il y a un lien avec le chi2
        html.P(children="Blablabla sur le chi2..."+str(ki2.getKi2("Sexe","Orientation"))),
        #Ensuite on montre le resultat de l'afc
        dcc.Graph(
            id='graph_afc1',
            figure=showAfc("Sexe","Orientation")
        ),
        html.P(children="Graphe 1 blablabla...") #lire un fichier txt avec tous les commentaires des graphes
    ]),

    html.Div(children=[
        html.H2(children="Recherche des facteurs de disparités"),

        html.Div(children=[
            html.H3(children="Impact de la zone géographique: ruralité"),
            dcc.Graph(
                id='graph_ecart_inertie',
                figure=showEcartInertieRuralite()
            ),
            html.P(children="Blablabla on explique... ")
        ]),

        html.Div(children=[
            html.H3(children="Impact social: IPS"),
            html.P(children="Blablabla sur l'IPS"),
            html.Link(href="https://hal.science/hal-01350095/document"),
            html.P(children="Explication du taux de parité blablabla..."+str(ki2.getKi2("IPS","TP"))),
            #Partie code un peu
            html.P(children="Blablabla sur le chi2..."),
            #Ensuite on montre le resultat de l'afc
            dcc.Graph(
                id='graph_afc2',
                figure=showAfc("IPS","TP")
            ),
            html.P(children="Graphe 2 blablabla...") #lire un fichier txt avec tous les commentaires des graphes
        ])
    ]),

    html.Div(children=[
        html.H3(children="Solutions envisageables"),
        html.P("Blablabla....")
    ]),

    html.Footer(children=[
        html.Div("Etude réalisée par CROS Guilhem, HERMET Robin, TILLIER Etienne, TOROSJAN Johan"),
        html.Div("Projet Data Science Polytech Montpellier 2022/2023")
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
