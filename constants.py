#Fichiers des constantes textes concernant l'étude affichées dans l'app

#Presentation de l'étude
PRESENTATION=(
    "Dans cette étude statistique, nous avons décidées d'étudier les disparités entre genres dans l'orientation scolaire et professionnelle.\n"+
    "Le but est dans un premier temps d'identifier quelles sont les disparités dans le parcours scolaire du public féminin, " +
    "puis dans un second temps de tenter d'identifier les facteurs influant sur ces disparités afin de réfléchir aux actions à mettre en place dans le futur pour que l’orientation soit le moins genré possible.\n"+ 
    "Pour ce faire, nous nous sommes basés sur des données ouvertes disponibles sur data.education.gouv, concernant principalement des élèves de seconde entre 2020 et 2022,"+
    "ainsi que des données ouvertes mises en ligne par l’INSEE."
)

#Presenation des disparites + Partie 1 de l'explication du premier XH2 (à afficher juste avant la valeur du XHI2)
XHI2_AFC1_PT1=(
    "Afin d’observer les disparités, nous avons premièrement pensé à regarder les voeux des élèves de seconde dans les différentes filières et selon leur sexe."+
    "En effet, les voeux de seconde ayant un véritable impact sur l’orientation professionelle, "+
    "il nous semblait intéressant de voir si une disparité pouvait déja être observé à un âge adolescent et plus particulièrement si le sexe influait sur le choix des élèves.\n\n"+

    "Afin de certifier une corrélation entre le sexe et les voeux d’orientation de notre public de seconde, un test du Xhi2 a été réalisé. "+
    "Celui-ci a pour objectif de quantifier l'écart à l'indépendance entre nos deux variables qualitatives “sexe” et “choix”.\n"+
    "Nous avons ainsi poser les hypothèses suivantes :\n" +
    "H0: Il n’existe pas de relation entre le sexe et la prise de décision des élèves de seconde\n"+
    "H1: Le sexe influe sur la prise de décision des élèves de secondes. \n\n"+

    "La valeur du Xhi2 est ici de  " 
)

#Partie 2 de l'explication du premier XHI2 (à afficher après la valeur du XHI2)
XHI2_AFC1_PT2=(
    " Pour un degré de liberté valant (I-1)(J–1)=17 ici et avec un risque de première espèce fixé à 5%, la valeur du Xhi2 est supérieure au seuil q(95%, 17)." +
    "On peut alors rejetter l’hypothèse d’indépendance entre sexe et choix d’orientation et conclure de manière significative à l’existence d’un lien entre ces deux variabes.\n"+
    "Dans l’optique de représenter ce lien, une Analyse Factorielle de Correspondance entre ces variables a été réalisée."
)

#Analyse premiere AFC (Orientation/Sexe)
PRESENTATION_AFC1=(
    "Cette AFC, où la totalité l’information est representée sur le premier axe, nous permet malgré tout d’observer les disparités suivantes :\n"+
    "on observe, à l’extremité gauche, 2 choix de matière particulièrement écartés que sont “Danse”,  “Humanité, Littérature et philosophie/ langue  et sciences économiques et sociales”.\n"+
    "On observe, à l’extrémité droite, 4 choix de matières particulièrement écartés que sont “Sciences Informatique, “Sciences de l’ingénieur, ”Mathématique” et “Physique chimie”.\n"+
    "En portant un oeil aux modalités “ Homme” et “Femme” représentées aussi sur cette AFC, nous pouvons remarquer que les variables présentes à gauche sont corrélées avec le sexe féminin alors que les variables situées à droite corrélent avec le sexe masculin.\n\n"+

    "Cette observation et le test du Xhi2 réalisé précédemment nous ont donc permis de mettre en lumière que le sexe influe sur le voeux des élèves de seconde, " +
    "et que les femmes ont plutôt tendance à s’orienter vers des matières “ littéraires” ou “sociales” alors que les hommes ont plutôt tendance à s’orienter vers des matières dites “scientifiques”.\n\n"+

    "Cette disparité, observable en école d’ingénieur par exemple, est donc déjà observable chez les élèves de seconde. "+
    "Cela nous pousse donc à nous poser la question des facteurs qui influent sur cette décision de s’orienter selon son sexe."
)

#Presentation Taux de Parité, à mettre en premier apres l'analyse de l'AFC1
PRESENTATION_TAUX_PARITE=(
    "L’AFC réalisée dans la partie 1 nous a donc extrapolé quelques matières que l’on peut qualifier à tendance masculine.\n\n"+
    "Les “voeux à tendances masculines” sont donc calculés comme étant des voeux comportant les combinaisons “mathématique/physique chimie/ numérique/ingénieur ”\n\n"+
    "Ainsi, afin de pouvoir décrire la qualité d’un lycée à ne pas tendre vers ce comportement dispersif, et afin d'évaluer la part de femme ayant réalisée des choix"+
    " d'orientation dont on dira qu'il ne leur correspond pas (à tendance masculine), un taux de parité est calculé pour chaque lycée.\n"+
    "Le Taux de Parité ( TP ) d’un lycée est ainsi défini comme suit: \n\n"+
    "TP (lycée)  = Nombre de voeux féminin à tendance masculine (lycée) / Nombre de voeux total féminin (lycée) \n\n"+
    "Ce taux, ensuite discrétisé en “ Faible”, “ Assez Faible”, “Moyen”, “Assez Elevé” et “Elevé”  nous permetra ainsi, combiné aux autres indices, d’extrapoler les facteurs. "
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

INTRO_HYPOTHESES_XHI2_AFC2=(
    "Ainsi nous avons décidé d’étudier la corrélation entre la ruralité et le taux de parité, nous avons donc posé les hypothèses suivantes: "+
    "H0: La zone dans laquelle se situe un lycée et le taux de parité sont indépendants"
    "H1: Il existe une corrélation entre le niveau de ruralité et le taux de parité "
    "Ainsi, aprés réalisation d’un test du Xhi2, nous obtenons la p-value suivante: "
)

#Analyse du deuxième XHI2, après la val du XHI2 et avant la deuxième AFC
XHI2_AFC2=(
    "Avec un risque de première espèce fixé à 5%, on rejette ici l’hypothèse d’indépendance entre la ruralité et le taux de parité et concluons à une forte dépendance entre ces deux variables,"+ 
    " représentée dans l'AFC suivante."
)

#Analyse de la deuxième AFC (Taux de ruralité/Taux de parité)
PRESENTATION_AFC2=(
    "Tout d’abord, la modalité “Commune très peu dense” étant associée à aucun lycée, sa représentation éloignée ne nous apporte aucune information."+
    "Néanmoins, nous pouvons observer un regroupement des modalités \"Élevé\" et \"Assez élevé\" du taux de parité autour de la modalité \"communes densément peuplé\", tout comme un regroupement des modalités \"Assez faible\", \"faible\" et \"moyen\" autour des modalités de ruralité \"peu dense\" et \"densité intermédiaire\"."+
    "Ces résultats sont marquants car ils démontrent que dans les zones les plus denses, équipées de nombreux équipements publics ou proches des grandes villes, la disparité tend à disparaître."+
    "Néanmoins,  et malgré un regroupement des modalités, un calcul de l’écart à l’indépendance des variables sexe et choix a été calculé pour différents niveaux de ruralité: "

)

PRESENTATION_GRAPHE_ECART_INERTIE=(
    "Ce graphique montre bien que, malgré tout, l’indépendance est loin d'être atteinte entre ces deux variables, et cela nous pousse à vouloir identifier d’autres facteurs."
)


#Analyse du troisième XHI2, après la val du XHI2 et avant la troisième AFC
AFC3_INTRO=(
    "L’IPS représentant quantitativement la situation socio-culturelle des enfants présents dans le lycée, nous avons observé une corrélation entre l’IPS et le taux de parité en procédant à un test du Xhi2 entre les 2 variables \"IPS\" et \"Taux de parité\"."+
    "Ici encore, le résultat est sans appel avec une p-value égale à "
)

#Analyse de la troisième AFC (IPS/Taux de ruralité)
PRESENTATION_AFC3=(
    "Cette AFC est vraiment parlante. En effet, on observe de fortes concordances entre chaque modalité d'IPS et de taux de parité. " + 
    "Par exemple, les lycées ayant un IPS dit faible ont tendance à avoir un taux de parité également faible. "+
    "Cela est d'autant plus marqué pour les extrêmes (\"faible\" et \"élevé\") ainsi que pour les modalités \"assez faible\" des deux variables.\n"+
    "On peut en déduire qu'une élève évoluant dans un contexte familial et social défavorable ou assez défavorable aux apprentissages aura moins tendance à s'orienter vers des spécialisations à dominante masculine.\n"+
    "En revanche, une élève se développant dans un contexte très favorable aura plus tendance à prendre le risque de s'orienter vers ce type de spécialisation.\n\n"+

    "En reprenant la première AFC détaillée précédemment, on pourrait traduire cela en disant que les lycéennes issues de milieu plutôt favorable aux apprentissages ont tendance à se diriger plus facilement vers des matières scientifiques."+
    "Néanmoins, il est quand même important de rappeler que l’IPS  est un résumé simplifié de la réalité, qui ne peut rendre compte à lui seul de la complexité de la situation socio-économique et culturelle des élèves accueillis dans un établissement."
)

SOLUTIONS=(
    "Pour conclure, nous avons vu  qu'il existe une forte disparité des genres dans l’orientation et que plusieurs facteurs complexes sont corrélés à ces différents niveaux de disparités."+
    "Finalement, il existe plusieurs autres raisons pour lesquelles les femmes s'orientent moins vers les spécialités scientifiques que les hommes. L'une des principales raisons est la persistance de stéréotypes de genre qui font croire aux femmes qu'elles ne sont pas aussi capables que les hommes dans les matières scientifiques. Les préjugés inconscients à l'égard des femmes dans les domaines scientifiques peuvent aussi jouer un rôle dans les choix d'orientation des jeunes filles, ainsi que dans les perceptions des enseignants, des parents et des mentors."+
    "Il y a aussi un manque de modèles féminins dans les domaines scientifiques qui peut dissuader les jeunes filles de poursuivre des études dans ces domaines. Les discriminations et les obstacles structurels qui sont encore présents dans les milieux professionnels scientifiques peuvent également dissuader les femmes de poursuivre une carrière dans ces domaines."+
    "Il y a plusieurs actions qui peuvent être mises en place pour rendre l'orientation moins genrée: "
)

SOL1=(
    "Sensibilisation et formation des professionnels de l'orientation sur les biais de genre et les stéréotypes de genre."
)

SOL2=(
    "Mise en place de programmes d'éducation sur les genres dans les écoles et les collèges pour briser les stéréotypes de genre et favoriser l'égalité des sexes."
)

SOL3=(
    "Encourager les filles à étudier des domaines traditionnellement masculins, comme les sciences, les mathématiques et les technologies, et les garçons à étudier des domaines traditionnellement féminins, comme les sciences sociales et les sciences de l'éducation."
)

SOL4=(
    "Favoriser la diversité dans les choix d'orientation, en proposant des programmes d'orientation qui tiennent compte des intérêts et des compétences des élèves, plutôt que de se baser sur les stéréotypes de genre."
)

SOL5=(
    "Inclure des personnes de différents genres dans les processus de prise de décision en matière d'orientation et les inclure dans les programmes de mentorat pour les élèves."
)