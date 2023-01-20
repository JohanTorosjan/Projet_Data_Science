# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from afc import *
from ki2 import * 
from constants import *

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
    fig.add_scatter(x=x2,y=y2,hovertext=dataFrame.columns.values,mode="markers")    
    title='Nuage des '+paramAfc1+' et des '+paramAfc2
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
        html.H2(children="1. Présentation de l'étude"),
        html.P(children=PRESENTATION)
    ]),

    html.Div(children=[
        html.H2(children="2. Observation des disparités"),
        #D'abord on montre qu'il y a un lien avec le chi2
        html.P(children=XHI2_AFC1_PT1+str(ki2.getKi2("Sexe","Orientation"))+". "+XHI2_AFC1_PT2),
        #Ensuite on montre le resultat de l'afc
        dcc.Graph(
            id='graph_afc1',
            figure=showAfc("Sexe","Orientation")
        ),
        html.P(children=PRESENTATION_AFC1) 
    ]),

    html.Div(children=[
        html.H2(children="3. Les facteurs de disparités"),

        html.Div(children=[
            html.H3(children="3.1 Les indices utilisés"),
            html.P(children="Afin d’étudier les facteurs, nous nous sommes basées sur 3 indice associés à un lycée que nous allons décrire: il s'agit respectivement du taux de parité, de l'IPS et du niveau de ruralité"),
        ]),

        html.Div(children=[
            html.H4(children="3.1.1 Présentation du taux de parité"),
            html.P(children=PRESENTATION_TAUX_PARITE)
        ]),

        html.Div(children=[
            html.H4(children="3.1.2 Présentation de l'IPS"),
            html.P(children=PRESENTATION_IPS),
            html.Link(href="https://hal.science/hal-01350095/document"),
        ]),

        html.Div(children=[
            html.H4(children="3.1.1 Présentation de l'indice de ruralité"),
            html.P(children=PRESENTATION_INDICE_RURAL)
        ]),

        html.Div(children=[
            html.H3(children="3.2 Impact de la zone géographique: ruralité"),
            html.P(children=INTRO_HYPOTHESES_XHI2_AFC2+str(ki2.getPvalue("Ruralite","TP"))+XHI2_AFC2),
            dcc.Graph(
                id='graph_afc2',
                figure=showAfc("Ruralite","TP")
            ),
            html.P(children=PRESENTATION_AFC2),
            dcc.Graph(
                id='graph_ecart_independance',
                figure=showEcartInertieRuralite()
            ),
            html.P(children=PRESENTATION_GRAPHE_ECART_INERTIE)
        ]),

        html.Div(children=[
            html.H3(children="3.3 Impact de la situation sociale: IPS"),
            html.P(children=AFC3_INTRO+str(ki2.getPvalue("IPS","TP"))),
            html.P(children="Nous avons réalisé l'AFC suivante:"),
            dcc.Graph(
                id='graph_afc3',
                figure=showAfc("IPS","TP")
            ),
            html.P(children=PRESENTATION_AFC3) #lire un fichier txt avec tous les commentaires des graphes
        ])
    ]),

    html.Div(children=[
        html.H2(children="4. Solutions envisageables"),
        html.P(children=SOLUTIONS),
        html.P(children=SOL1),
        html.P(children=SOL2),
        html.P(children=SOL3),
        html.P(children=SOL4),
        html.P(children=SOL5),
    ]),

    html.Footer(children=[
        html.Div("Etude réalisée par CROS Guilhem, HERMET Robin, TILLIER Etienne, TOROSJAN Johan"),
        html.Div("Projet Data Science Polytech Montpellier 2022/2023")
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
