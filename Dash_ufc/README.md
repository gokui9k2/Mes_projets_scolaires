# Mon Application Shiny UFC



## Interface
![Texte alternatif](Image/Interface.png)


## Introduction et Vue d'Ensemble

Cette application Shiny est conçue pour la visualisation et l'analyse des données des combattants de l'UFC. Elle propose des fonctionnalités telles que des cartes interactives, des graphiques et des analyses statistiques.

## C'est quoi l'ufc?

L'UFC, ou Ultimate Fighting Championship, est une organisation de premier plan dans le monde des arts martiaux mixtes (MMA). Fondée en 1993, l'UFC a joué un rôle crucial dans la popularisation du MMA à l'échelle mondiale. Elle organise des combats entre des athlètes hautement qualifiés dans diverses disciplines de combat, telles que le jiu-jitsu brésilien, la lutte, la boxe, le kickboxing, et le judo. L'UFC est reconnue pour ses événements spectaculaires, rassemblant les meilleurs combattants du monde dans des tournois qui testent leurs compétences et leur endurance. Avec ses règles strictes et son format de compétition, l'UFC a transformé le MMA en un sport professionnel respecté et suivi par des millions de fans à travers le monde.

## Table des Matières
- [Guide Développeur](#guide-développeur)
- [Guide Utilisateur](#guide-utilisateur)
- [Rapport d'Analyse](#rapport-danalyse)


## Guide du dévelopeur

Langage : R 
                                                          
Framework : Shiny                                               
                                                             
IDE recommandé : RStudio

### Architecture du Code:

app.R : Point d'entrée principal de l'application.

sidebarPanelUI.R et mainPanelUI.R : UI pour les panneaux latéral et principal.

prepareData.R : Script de prétraitement des données.

Map.R : Contient les fonctions qui créent les graphes de l'onglet carte.

Caracteristique.R : Contient les fonctions qui créent les graphes de l'onglet caractéristique.

Statistique.R : Contient les fonctions qui créent les graphes de l'onglet statistiques.

Histo.R : Contient les fonctions qui créent les graphes de l'onglet histogramme.

![Texte alternatif](Image/ar.png)

![Texte alternatif](Image/archieeeeeee.png)

## Guide Utilisateur

Installation de R et RStudio

R : Fournissez un lien vers CRAN pour télécharger et installer la dernière version de R.

RStudio (optionnel mais recommandé) : Fournissez un lien vers RStudio Download pour télécharger et installer RStudio.

Pour le bon fonctionnement de l'application il faut telecaharger Rtools

Aller dans le terminal et effectuer la commande suivant:        

    git clone https://git.esiee.fr/renaulta/ufcproject_petris_renaultr.git

Une fois cela effectuer ouvrer R ou Rstudio on se placera dans le fichier ou ce trouve le code avec la commande suivant:

    setwd("chemin/d'acces au au fichier/clone")

Une fois dans ce fichier dans la console vous ecrirez les commande suivante

    packages <- readLines("requirements.txt")

Installer chaque package:

    for (pkg in packages) {
        if (pkg != "") {
        install.packages(pkg)
        }
    }
    library(shiny)

Lancement de l'application:

    runApp("app.R")




Cette application Shiny propose une analyse d'un dataset de l'UFC. Nous avons tenté d'identifier diverses caractéristiques des combattants susceptibles d'influencer les issues des combats. Un onglet dédié permet également de consulter les caractéristiques individuelles de chaque combattant.

Au sein de cette application, vous pouvez naviguer entre différents onglets tels que Carte, Data, Statistiques, etc. Chaque onglet propose différentes variables, chacune offrant un type d'information spécifique.

L'onglet Statistiques présente un graphique dynamique. Vous pouvez y sélectionner une allonge et, en fonction de celle-ci, le graphique affichera le pourcentage de victoires des combattants ayant cette allonge.

![Texte alternatif](Image/Reach_sup.png)

Un autre graphique dynamique se trouve dans l'onglet Caractéristiques. Vous pouvez y choisir un combattant pour afficher ses caractéristiques détaillées.

![Texte alternatif](Image/Carac_ufc.png)

Dans l'onglet Data, il est possible de visualiser les données, et un bouton permet de les télécharger.


## Rapport d'analyse

Analyse des données categorielle:

## Stance

La stance d'un combattant, ou sa posture de combat, joue un rôle crucial dans la stratégie et l'efficacité des attaques et défenses lors d'un combat. Par exemple, un combattant gaucher peut présenter des angles d'attaque inattendus pour un adversaire orthodoxe, tandis qu'une stance ouverte peut offrir des opportunités uniques pour des frappes croisées. 

Stance la variable Stance represente la posture de combat des different combattants:

Orthodoxe : Position standard pour un droitier, main droite en arrière, main gauche en avant.

Gaucher  : Inverse de l'orthodoxe, pour un gaucher, main gauche en arrière, main droite en avant.

Open Stance : Affrontement entre un orthodoxe et un gaucher, les mains et pieds avants sont du même côté.

Switch : Capacité à changer entre les positions orthodoxe et gaucher.

![Texte alternatif](Image/B_Stance.png)
![Texte alternatif](Image/R_Stance.png)

Ces deux histogrammes révèlent qu'il y a nettement plus de combattants Orthodoxes que de Southpaws, Switch ou Open Stance. Le nombre limité de combattants utilisant les styles Switch ou Open Stance rend difficile une étude approfondie sur ces variables. Cependant, cela soulève une question intéressante : les combattants Orthodoxes ont-ils un avantage ou non contre les Southpaws ?

![Texte alternatif](Image/Stat_Stance.png)

Théoriquement, on pourrait s'attendre à un taux de victoire élevé pour les combattants Southpaw, étant donné que la majorité des combattants sont Orthodoxes et n'ont pas l'habitude d'affronter des Southpaws. Ces derniers pourraient les surprendre avec des angles d'attaque différents. Cependant, nos observations montrent que ce n'est pas le cas. Les Southpaws ont une probabilité de victoire de 51,6 % contre des combattants Orthodoxes, ce qui n'est pas significativement élevé.


### Finish

![Texte](Image/Finish.png)

Les combats de MMA à l'UFC peuvent se terminer de différentes manières, chacune reflétant une stratégie et une performance distinctes des combattants. Cet histogramme offre une analyse détaillée de la manière dont se concluent la plupart des combats à l'UFC.

U-DEC (Unanimous Decision):
Description: Une décision unanime est rendue par les juges à la fin du combat. Cela signifie que tous les juges sont d'accord sur le vainqueur du combat.

KO/TKO (Knockout/Technical Knockout):
Description: Un combattant remporte le combat en mettant son adversaire KO (Knockout) ou en le forçant à abandonner en raison de l'incapacité de continuer (Technical Knockout).

SUB (Submission):
Description: La victoire est obtenue par soumission, c'est-à-dire qu'un combattant force son adversaire à abandonner en appliquant une prise de soumission.

S-DEC (Split Decision):
Description: Une décision partagée est rendue par les juges. Cela signifie qu'il y a un désaccord entre au moins deux des juges quant au vainqueur du combat.

M-DEC (Majority Decision):
Description: Une décision à la majorité est rendue par les juges. Cela signifie qu'une majorité des juges est d'accord sur le vainqueur, mais il peut y avoir un juge en désaccord.

DQ (Disqualification):
Description: Un combattant est disqualifié, entraînant la victoire de son adversaire. Cela peut être dû à des infractions graves aux règles ou à des comportements inappropriés pendant le combat.

![Texte alternatif](Image/finish.png)

On remarque que la majorité des combats se concluent par une décision, c'est-à-dire qu'il n'y a ni KO ni soumission dans le temps imparti, et que le vainqueur est déterminé par les juges. Ensuite, la deuxième cause la plus fréquente de fin de combat est le KO.

### Finish round

L'issue des rounds dans les combats de l'UFC varie en fonction de plusieurs facteurs, notamment la durée du match. 

![Texte alternatif](Image/finish_round.png)

Cet histogramme illustre la répartition des fins de rounds à l'UFC. Généralement, un match se déroule en 3 rounds, sauf pour les combats de championnat de catégorie, qui se jouent en 5 rounds. Il est donc cohérent de constater qu'il y a très peu de combats qui se terminent au 5ème round. La majorité des combats se concluent au 3ème round, ce qui est logique étant donné que, comme nous l'avons vu précédemment, la plupart des combats se terminent par une décision des juges.


### Gender

Cet histogramme illustre la grande disparité entre les hommes et les femmes dans ce sport de combat, le MMA. Ce n'est pas le seul sport de combat où l'on observe une grande disparité entre les hommes et les femmes, ce qui est vraiment dommage.

![Texte alternatif](Image/gender.png)


### Winner 

Cet histogramme représente le nombre de victoires des combattants du côté bleu (Blue side) et du côté rouge (Red side). Il est logique de constater que le Red side enregistre plus de victoires, car il inclut généralement les champions de chaque catégorie ainsi que les challengers principaux.

![Texte alternatif](Image/Winner.png)



Passons maintenant à l'onglet Statistiques :

### Allonge 
![Texte alternatif](Image/jon_jones_.png)


L'allonge en MMA est un élément clé qui peut offrir un avantage tactique notable, influençant considérablement la stratégie et l'issue des combats. Notre analyse explore comment une allonge supérieure modifie la dynamique du combat, en impactant la portée, la défense et l'efficacité des attaques des combattants.

![Texte alternatif](Image/Stat_Reach_full.png)
![Texte alternatif](Image/Stat_stancesup.png)

Nous avons décidé d'analyser l'impact de l'allonge sur l'issue des différents combats. L'allonge, ou envergure, désigne la distance entre les extrémités des deux bras tendus à l'horizontale, dans le prolongement de la poitrine. Cela peut représenter un avantage significatif. Notre premier graphique montre le pourcentage de victoires en fonction de l'allonge. Étant donné que de nombreux combattants partagent la même allonge, cette donnée n'est pas nécessairement pertinente. Nous avons donc décidé d'examiner le pourcentage de victoires pour les combattants ayant 10 cm d'allonge de plus que leurs adversaires. À notre grande surprise, les résultats sont plus serrés que prévu : les combattants avec 10 cm d'allonge supplémentaire gagnent plus souvent. Nous aurions pu réaliser la même étude avec une différence d'allonge de 20 cm, mais les combats présentant une telle différence sont trop rares.

### Coup significatif & décision

L'analyse de la relation entre le nombre de coups significatifs portés et les décisions des juges dans différentes catégories de poids en MMA offre des insights précieux sur les dynamiques de combat. En se concentrant sur differente catégories  de , notre étude vise à déchiffrer comment la fréquence et l'efficacité des coups influencent l'issue des combats. Cette approche nous permet d'examiner les nuances tactiques et techniques qui différencient ces catégories, révélant des tendances intéressantes dans les stratégies de combat.
Le poids important lors d'un combat est délimité en catégories pour chaques combattants. Ainsi on distingue :

Poids Mouche (Flyweight)
Limite de Poids: 56.7 kg (125 lb)
Description: La catégorie des poids mouches est la plus légère de l'UFC. Les combattants de cette catégorie sont agiles et rapides, offrant des combats dynamiques avec des techniques de frappe et de soumission.

Poids Coq (Bantamweight)
Limite de Poids: 61.2 kg (135 lb)
Description: Les combattants de la catégorie des poids coqs sont rapides et techniques. Les combats de cette catégorie sont souvent caractérisés par une combinaison de puissance et d'agilité.

Poids Plume (Featherweight)
Limite de Poids: 65.8 kg (145 lb)
Description: La catégorie des poids plumes présente des combattants légers mais puissants. Les combats dans cette catégorie sont connus pour leur énergie et leur intensité.

Poids Léger (Lightweight)
Limite de Poids: 70.3 kg (155 lb)
Description: Les combattants légers offrent une combinaison de vitesse, de puissance et d'endurance. La catégorie des poids légers est l'une des plus populaires, avec des combats souvent spectaculaires.

Poids Mi-Moyen (Welterweight)
Limite de Poids: 77.1 kg (170 lb)
Description: Les combattants de la catégorie des poids mi-moyens sont polyvalents, offrant une combinaison de puissance et d'habiletés techniques. Cette catégorie est connue pour sa compétitivité intense.

Poids Moyen (Middleweight)
Limite de Poids: 83.9 kg (185 lb)
Description: Les poids moyens présentent des combattants puissants et techniques. Les combats dans cette catégorie sont souvent marqués par des compétences de frappe et de grappling de haut niveau.

Poids Lourd Léger (Light Heavyweight)
Limite de Poids: 93.0 kg (205 lb)
Description: Les combattants de la catégorie des poids lourds légers sont puissants et agiles. Cette catégorie combine la force des poids lourds avec la vitesse des catégories plus légères.

Poids Lourd (Heavyweight)
Limite de Poids: Pas de limite supérieure
Description: Les poids lourds sont les combattants les plus massifs de l'UFC. Avec aucune limite de poids supérieure, cette catégorie présente souvent des combats explosifs mettant en jeu une puissance phénoménale.
Chaque catégorie de poids offre une dynamique unique, créant une diversité d'approches stratégiques et de styles de combat au sein de l'UFC. Ces catégories permettent aux combattants de trouver la classe de poids qui correspond le mieux à leurs compétences physiques et techniques, assurant des compétitions équitables et passionnantes.

![Texte alternatif](Image/Stat_cat.png)

Dans cet onglet, notre objectif était d'analyser la relation entre le nombre de coups significatifs portés et le pourcentage de décisions dans différentes catégories de poids. Nous avons observé que, dans la catégorie des poids légers, le pourcentage de coups significatifs est moins élevé (42 %) comparé à celui des catégories poids lourds (48,5 %). Les combattants de la catégorie poids légers, étant plus agiles, pourraient avoir plus de difficulté à toucher leurs adversaires, tandis que plus on monte en catégorie de poids, moins les combattants sont agiles, plus susceptibles de prendre des coups et moins endurants. De plus, il semble exister une corrélation entre le pourcentage de coups significatifs et les finitions par décision : plus ce pourcentage est élevé, moins le combat a tendance à se terminer par une décision, et vice-versa, ce qui est logique.


### Age & performence 

Dans le monde des sports de combats, l'age est au centre des préoccupation.Pendant que certains professionels du sport tiennent à préciser que cela ne se compare pas à l'experience, il est utile de noter que les performances physiques des combattants sont intimements liées à leurs ages.
Ainsi, l'ensemble des techniques pouvant être liés à la victoire par décisions ou par KOs/TKos a à voir de loin ou de près avec l'age de nos combattants.
On décide alors d'observer l'évolution de la moyenne des coups significatifs avec l'age de nos combattants.
On observe bel et bien une influence, avec le paramètre étant prédominant entre 25 et 30 ans.Si l'argument de "l'experience" intervient lors du striking (combat pieds-poings) .

![Texte alternatif](Image/Stat_TD.png)

Avec ce graphique, notre objectif était d'examiner l'influence de l'âge des combattants sur leur moyenne de take-downs. Il apparaît clairement qu'une tendance significative se dessine autour de l'âge de 30 ans.

![Texte alternatif](Image/Stat_STR.png)

Comme le graphique précédent, nous avons cherché à analyser l'influence de l'âge des combattants sur la moyenne des coups significatifs portés. Nous observons une tendance notable autour de 30 ans.

L'objectif de ces deux graphiques était de déterminer l'âge 'prime' d'un combattant. Étant donné que les statistiques de combat sont généralement meilleures vers 30 ans, on pourrait en déduire que c'est à cet âge que les combattants sont dans leur prime. Idéalement, nous aurions aimé calculer un pourcentage de victoires pour chaque tranche d'âge, mais par manque de temps, cette fonctionnalité n'a pas été implémentée.


### Carte 

Passons maintenant à l'onglet Carte :

Cette carte illustre la répartition des combattants de l'UFC dans différents pays du monde. Il est notable que la concentration la plus élevée de combattants se trouve sur le continent américain. En comparaison, le nombre de combattants européens est relativement faible, ce qui pourrait être attribué aux anciennes interdictions de ce sport de combat en Europe, où il était jugé trop violent.

![Texte alternatif](Image/Carte_nat.png)

Dans cette deuxième carte, nous présentons la répartition des événements de l'UFC. La majorité de ces événements se déroulent sur le continent américain, ce qui est cohérent étant donné que la plupart des combattants sont d'origine américaine.

![Texte alternatif](Image/Carte_rep.png)



### Caracteristique

Dans cet onglet, nous avons regroupé les différentes caractéristiques des combattants. Vous pouvez chercher votre combattant préféré et voir ses caractéristiques. De plus, vous avez un graphe qui vous informe de la manière dont il a fini la plupart de ses combats.

![Texte alternatif](Image/stat_ufc.png)



## Aller plus loin



A partir des analyses faite précedemment, il devient intéressant  de chercher une corrélation entre la différence de reach, de taille et la probabilité de victoire.
Ici pour être sûr de cette analyse, le calcul d'une matrice de corrélation ou de simples coefficients de corrélation, peut être approprié.
Il devient aussi censé d'analyser l'évolution de la répartition des origines à travers les années.La ligue n'ayant cessé d'évoluer et comptant de plus en plus de combattants d'origines diverses.
Ainsi un pie chart intéractif ici semblerait intéressant.
Une méthode d'executiion consisterai à calculer la fréquence des origines pour une date fixé.
Puis en faisant varier la date selon un curseur, il s'agira de rafraichir le pie chart selon les diverses valeurs temporelles dans notre dataframe.Par soucis de quantité de données le rafraichissement ne devrait être fait que pour des années entre 1-4 ans.
Le même raisonnement s'applique alors pour la répartition des lieux où se déroulent les combats UFC.
De plus, une analyse de la repartion des KOs selon les catégories de poids permettrait de confirmer l'adage fait par de nombreux adeptes de sports de combats selon lequel plus le poids est important plus la force de frappe l'est.
Ainsi l'on pourrait s'attendre tout comme pour la réparition de la moyenne du nombre de frappes significatives à avoir un nombre de KO plus important pour les catégories les plus lourdes.
La méthode d'execution de cette séquence pourrait se baser sur le calcul de la fréquence des KOs selon la colonne 'finish' pour chaque catégories de poids.
Il pourrait enfin s'agir de renvoyer un histogramme entre la dite fréquence et les catégories de poids.
Notons enfin qu'il serait valable visualiser les tendances de combat des combattants selon leurs origines. En effet, différentes origines impliquent diverses méthodes de combats, techniques et habitudes. Ainsi on pourrait analyser la prominence du takedown pour des combattants russes et américains, la lutte étant un sport dominant en ces territoires.
Il en est de même pour l'ensemble des soumissions réussis.Le rear naked choke étant une soumission centrale en jiu jitsu brésilien.
De nombreuses options sont possibles ici. Une idée serait d'implémenter l'ensemble des moyennes de soumissions/takedown réussies sur une carte à l'aide de scatter_geo.
Les bulles prendraient la taille et la couleur de la moyenne des soumissions/takedown réussis par territoires. D'autres variables pourraient aussi être intéréssant à analyser de cette manière telle que la moyenne des frappes significatives.



### Conclusion 

En conclusion, notre application Shiny UFC a permis de mettre en lumière des aspects cruciaux du MMA à l'UFC, offrant à la fois des confirmations de certaines hypothèses et des surprises. Ces analyses contribuent à une meilleure compréhension de ce sport complexe et dynamique, et ouvrent la voie à de futures recherches et explorations dans le domaine des arts martiaux mixtes.
### Copyright



Ce code a été traduit c'est l'un des codes de l'un des analayse qui as affectuer des nalyse sur le data set.

lien:
https://www.kaggle.com/code/dolynok1/eda-significant-strike-percentage

createSignificantStrikesHeatmap <- function(ufc_data, input) {
  if(input$stat_variable == 'Categorie') {
    # Traitement des données pour les combattants bleus et rouges
    df_b <- ufc_data %>%
      select(weight_class, date, B_avg_SIG_STR_pct) %>%
      drop_na() %>%
      rename(avg_SIG_STR_pct = B_avg_SIG_STR_pct)
    
    df_r <- ufc_data %>%
      select(weight_class, date, R_avg_SIG_STR_pct) %>%
      drop_na() %>%
      rename(avg_SIG_STR_pct = R_avg_SIG_STR_pct)
    
    # Fusion des données
    joined_data <- bind_rows(df_r, df_b)
    
    # Calcul de la moyenne par catégorie de poids
    avg_by_weight_class <- joined_data %>%
      group_by(weight_class) %>%
      summarise(avg_SIG_STR_pct = mean(avg_SIG_STR_pct, na.rm = TRUE))
    
    # Réorganisation des catégories de poids
    new_order <- c('Flyweight', 'Bantamweight', 'Featherweight', 'Lightweight', 'Welterweight', 
                   'Middleweight', 'Light Heavyweight', 'Heavyweight', "Women's Strawweight", 
                   "Women's Flyweight", "Women's Bantamweight", "Women's Featherweight", 'Catch Weight')
    
    # Suppression de la catégorie 'Catch Weight' et réorganisation
    avg_by_weight_class <- avg_by_weight_class %>%
      filter(weight_class != 'Catch Weight') %>%
      mutate(weight_class = factor(weight_class, levels = new_order))
    
    # Sélection des catégories de poids masculines
    mens <- avg_by_weight_class %>%
      filter(weight_class %in% c('Flyweight', 'Bantamweight', 'Featherweight', 'Lightweight',
                                 'Welterweight', 'Middleweight', 'Light Heavyweight', 'Heavyweight'))
    
    # Création de la heatmap
    ggplot(mens, aes(x = "", y = weight_class, fill = avg_SIG_STR_pct)) +
      geom_tile() +
      geom_text(aes(label = scales::percent(avg_SIG_STR_pct, accuracy = 0.1)), color = "white") +
      scale_fill_viridis(direction = -1) +
      theme_minimal() +
      labs(title = "Pourcentage de coups significatifs par catégorie de poids", fill = "Pourcentage") +
      theme(axis.title.x = element_blank())
    }
    }

Ce code de bouton de telechargement est issu d'un tutorial youtube :

lien: https://www.youtube.com/watch?v=4XGI_ye0y4M&t=8465s

  Téléchargement des données
  output$save_data <- downloadHandler(
    filename = function() {
      paste("data_ufc", Sys.Date(), ".csv", sep = ',')
    },
    content = function(file) {
      write.csv(ufc_data, file)
    }
    )
Ce bloc me permet de mettre a jour les données à chaque changement de données ce bloc m'a été expliqué par chat.gpt:

  observe({
    if (!is.null(input$stat_variable) && input$stat_variable %in% c('Reach', 'Categorie', 'TD_R_B', 'STR_R_B','Stance')) {
      # Mise à jour des choix de combattants
      fighter_choices <- sort(unique(c(ufc_data$R_fighter, ufc_data$B_fighter)))
      updatePickerInput(session, 'fighter_select', choices = fighter_choices)
      
      # Mise à jour des choix de variables pour 'Reach', 'Categorie'
      if (input$stat_variable %in% c('Reach', 'Categorie')) {
        ufc_data_categorielle <- select(ufc_data, B_Stance, R_Stance, finish, finish_round, gender, Winner)
        updateSelectInput(session, 'variable', choices = names(ufc_data_categorielle))
      }
    }
    })

ce bloc permet de faire un curseur dynamique si certaine condition sont remplit ce code a été inspiré de ce site:

lien: https://stackoverflow.com/questions/75582333/is-it-possible-to-exclude-one-value-from-r-shiny-sliderinput
https://www.youtube.com/watch?v=W75o97mabX0

  output$reach_slider_ui <- renderUI({
    if(input$tabs == 'stat' && input$stat_variable == 'Reach') {
      sliderInput("reach_slider", "Sélectionnez la portée (cm):",
                  min = min(ufc_data$B_Reach_cms, na.rm = TRUE),
                  max = max(ufc_data$B_Reach_cms, na.rm = TRUE),
                  value = median(ufc_data$B_Reach_cms, na.rm = TRUE),
                  step = 1)
    }
    })  



Ce code a ete insperer de ce code il permet de faire la recherche des Caracteristiquedes combattant en temps reel:

lien :https://stackoverflow.com/questions/76732649/shinywidgets-pickerinput-in-dt-datatable-with-livesearch

      pickerInput('fighter_select', 'Choisis un combattant', 
                  choices = NULL,  # Les choix seront définis côté serveur
                  options = list(`liveSearch` = TRUE))

Ce code a été modifié mais la base de celui ci provient de cette video:

lien:https://www.youtube.com/watch?v=4XGI_ye0y4M&t=8465s

createPlot <- function(data, input) {
  # Vérifie si la variable sélectionnée par l'utilisateur n'est pas nulle et fait partie des données
  if (!is.null(input$variable) && input$variable %in% names(data)) {
    # Filtrer les données pour supprimer les NA de la variable sélectionnée
    data <- data %>% filter(!is.na(.data[[input$variable]]))
    
    # Si la variable sélectionnée est numérique
    if (is.numeric(data[[input$variable]])) {
      # Crée un histogramme pour les données numériques
      ggplot(data, aes_string(x = input$variable)) +
        geom_histogram(binwidth = 1) +
        xlab(input$variable) +
        theme_minimal()
    } else {
      # Si la variable sélectionnée n'est pas numérique
      ggplot(data, aes_string(x = input$variable)) +
        geom_bar() +
        xlab(input$variable) +
        theme_minimal()
    }
  } else {
    # Si la variable sélectionnée est nulle ou n'est pas dans les données
    ggplot() +
      annotate("text", x = 0.5, y = 0.5, label = "Aucune donnée à afficher", vjust = 0.5)
  }
}
Ce code permet de créer une carte interactive. Nous nous sommes inspirés de cette vidéo pour le faire :



createUfcMap <- function(ufc_data, input) {
  # Vérifie si la variable sélectionnée pour la carte est 'Localisation'
  if (input$map_variable == 'Localisation') {
    leaflet(ufc_data) %>%  # Utilise le package leaflet pour créer une carte interactive
      addTiles() %>%  # Ajoute les tuiles de base de la carte (fond de carte)
      addCircleMarkers(
        lng = ~longitude,  # Définit la longitude pour le positionnement des marqueurs
        lat = ~latitude,  # Définit la latitude pour le positionnement des marqueurs
        color = "green",  # Couleur des marqueurs
        radius = 5,  # Taille des marqueurs
        popup = ~paste("Latitude:", latitude, "<br>", "Longitude:", longitude)  # Crée des popups affichant la latitude et la longitude
      )
  }
}

lien :https://www.youtube.com/watch?v=aBR9dIOjrMg

Nous avons parfois utilisé chatgpt pour corriger certaines erreurs.
