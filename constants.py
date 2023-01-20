#Fichiers des constantes textes concernant l'étude affichées dans l'app

#Presentation de l'étude
PRESENTATION=(
    "Dans cette étude statistique, nous avons décidées d ‘étudiés les disparités entre genres dans l'orientation scolaire et professionnelle.\n"+
    "Le but est dans un premier temps d'identifier quelles sont  les disparités dans le parcours scolaire du public féminin, " +
    "puis dans un second temps de tenter d'identifier les facteurs influant sur  ces disparités afin de réfléchir aux actions à mettre en place dans le futur pour que l’orientation soit le moins genrés possible.\n"+ 
    "Pour ce faire, nous nous sommes basées  sur des données ouvertes disponibles sur data.education.gouv, concernant principalement des élèves de secondes entre 2020 et 2022,"+
    " ainsi que des données ouvertes mises en ligne par l’INSEE."
)

#Presenation des disparites + Partie 1 de l'explication du premier XH2 (à afficher juste avant la valeur du XHI2)
XHI2_AFC1_PT1=(
    "Afin d’observer les disparités, nous avons premièrement pensé à regarder les voeux des eleves de secondes dans les différentes filières et selon leurs sexe."+
    "En effet, les voeux de secondes ayant un véritable impact sur l’orientation professionelle, "+
    "il nous semblait intéressant de voir si une disparité pouvait déja être observé à un age adolescent et plus particulièrement si le sexe influait sur le choix des eleves.\n\n"+

    "Afin de certifier une corrélation entre le sexe et les voeux d’orientation de notre public de seconde, , un test du Xhi2 a été réalisé. "+
    "Celui a pour objectif de quantifier l'écart à l'indépendance entre nos deux variables qualitatives “sexe” et “choix”.\n"+
    "Nous avons ainsi poser les hypothèses suivantes :\n" +
    "H0 : Il n’existe pas de relation entre le sexe et la prise de décision des eleves de secondes\n"+
    "H1: Le sexe influe sur la prise de décision des eleves de secondes\n\n"+

    "La valeur du Xhi2 est ici de  …" 
)

#Partie 2 de l'explication du premier XHI2 (à afficher après la valeur du XHI2)
XHI2_AFC1_PT2=(
    "Pour un degré de liberté valant (I-1)(J–1)=17 ici et avec un risque de première espèce fixé à 5%, la valeur du Xhi2 est supérieure au seuil q(95%, 17)." +
    "On peut alors rejetter l’hypothèse d’indépendance entre sexe et choix d’orientation et conclure de manière significative à l’existence d’un lien entre ces deux variabes.\n"+
    "Dans l’optique de représenter ce lien, une Analyse Factorielle de Correspondance entre ces variables a été réalisée."
)

#Analyse premiere AFC (Orientation/Sexe)
PRESENTATION_AFC1=(
    "Cette AFC, où la totalité l’information est representé sur le premier axe, nous permet malgrés tout d’observer les disparités suivantes :\n"+
    "On observe à l’extremité gauche 2 choix de matière particulièrement écartés que sont “ Danse”,  “ Humanité, Littérature et philosophie/ langue  et sciences économiques et sociales”.\n"+
    "On observe à l’extrémité droite 4 choix de matières particulièrement écartés que sont “sciences informatique, “Sciences de l’ingénieur,”Mathématique” et “Physique chimie”.\n"+
    "En portant en oeil aux modalités “ Homme” et “Femme” représenté aussi sur cette afc, nous pouvons remarqué que les variables présentes à gauches sont corrélés avec le sexe féminin alors que les variables situés à droite corrélent avec le sexe masculin.\n\n"+

    "Cette observation et le test du Xhi2 réalisé précédemment nous ont donc permis de mettre en lumière que le sexe influe sur le voeux des éléves de seconde, " +
    "et que les femmes ont plutot tendance à s’orienter vers des matières “ littéraires” ou “sociales” alors que les hommes ont plutot tendance à s’orienter vers des matière dites “scientifique”.\n\n"+

    "Cette disparité, observable en école d’ingénieur par exemple, est donc déjà observable chez les élèves de seconde. "+
    "Cela nous pousse donc à nous poser la question des facteurs qui influe sur cette décision de s’orienter selon son sexe."
)

#Presentation Taux de Parité, à mettre en premier apres l'analyse de l'AFC1
PRESENTATION_TAUX_PARITE=(
    "L’AFC réalisé dans la partie 1 nous a donc extrapolé quelques matières que l’on peut qualifier à tendance masculine.\n\n"+
    "Les “voeux à tendances masculines” sont donc calculé comme étant des voeux comportant les combinaisons “ mathématique/physique chimie/ numérique/ingénieur ”\n\n"+
    "Ainsi, afin de pouvoir décrire la qualité d’un lycée à ne pas tendre vers ce comportement dispersif, et afin d'évaluer la part de femme ayant réalisées des choix"+
    " d'orientation dont on dira qu'il ne leur correspond pas (à tendance masculine), un taux de parité est calculé pour chaque lycée.\n"+
    "Le Taux de Parité ( TP ) d’un lycée est ainsi définie comme suit: \n\n"+
    "TP (lycée)  = Nombres de voeux féminin à tendances masculine (lycée) / Nombre de voeux totals féminin (lycée) \n\n"+
    "Ce taux, ensuite discrétisé en “ Faible”, “ Assez Faible”, “Moyen”, “Assez Elevé” et “Elevé”  nous permetra ainsi, combinées aux autres indices d’extrapoler les facteurs "
)

#Presentation de l'IPS à mettre apres le taux de partité et juste avant l'affichage de la val du XHI2
PRESENTATION_IPS=(
    "L'indice de position sociale des élèves (IPS) est un outil de mesure quantitatif de la situation sociale des élèves face aux apprentissages dans les établissements scolaires français."+
    " Plus l'indice est élevé, plus l'élève évolue dans un contexte familial favorable aux apprentissages. Cet indice est construit à partir des professions et catégories socioprofessionnelles"+
    " (PCS) des représentants légaux des élèves et est considéré comme la moyenne pondérée de caractéristiques telles que les diplômes, les pratiques culturelles, les conditions matérielles, "+
    "le capital culturel et l’implication des parents dans la scolarité. Cette méthodologie statistique est décrite dans l’article de Rocher (2016) et s’appuie sur une ACM réalisée à partir du panel de la DEPP d’élèves entrés en sixième en 2007.\n"+
    "Nous utilisons ici cet indice afin d'évaluer la situation sociale de l'élève dans l'optique de quantifier et de représenter l'impact social sur les choix des élèves en fonction de leur sexe."
)

PRESENTATION_INDICE_RURAL=(
    "L'indice de ruralité de l'INSEE est un indicateur qui mesure le degré de ruralité d'un territoire en France. Il est basé sur une classification des communes en fonction de critères tels que la densité de population, la présence d'équipements publics"+
    " et la proximité avec des villes. Les communes sont classées en 4 catégories :  \"Communes très peu denses\", \"Communes peu denses\", \"Communes de densité intermédiaire\", \"Communes densément peuplées\". "+
    "Cet indice est utilisé pour établir des politiques de développement territorial et pour étudier les différences de niveaux de vie entre les zones rurales et urbaines. Couplée à nos données, il permet de déterminer dans quelle type de zone se trouve le lycée étudié"+
    ", et ainsi observer l’impact de la ruralité sur les choix des élèves."
)

#Analyse du deuxième XHI2, après la val du XHI2 et avant la deuxième AFC
XHI2_AFC2=(
    "On rejette ici l’hypothèse d’indépendance entre IPS et taux de parité et concluons à une forte dépendance entre ces deux variables,"+ 
    " représentée dans l'AFC suivante."
)

#Analyse de la deuxième AFC (IPS/Taux de ruralité)
PRESENTATION_AFC2=(
    "Cette AFC est vraiment parlante. En effet, on observe de fortes concordances entre chaque modalité d'IPS et de taux de parité. " + 
    "Par exemple, les lycées ayant un IPS dit faible ont tendance à avoir un taux de parité également faible. "+
    "Cela est d'autant plus marqué pour les extrêmes (\"faible\" et \"élevé\") ainsi que pour les modalités \"assez faible\" des deux variables.\n"+
    "On peut en déduire qu'une élève évoluant dans un contexte familial et social défavorable ou assez défavorable aux apprentissages aura moins tendance à s'orienter vers des spécialisations à dominante masculine.\n"+
    "En revanche, une élève se développant dans un contexte très favorable aura plus tendance à prendre le risque de s'orienter vers ce type de spécialisation.\n\n"+

    "En reprenant la première AFC détaillée précédemment, on pourrait traduire cela en disant que les lycéennes issues de milieu plutôt favorable aux apprentissages ont tendance à se diriger plus facilement vers des matières scientifiques."
)

