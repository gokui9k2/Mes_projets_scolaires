createWinPercentageReachSupPlot <- function(ufc_data, reach_dif_threshold, tab, stat_variable) {
  if(tab == 'stat' && stat_variable == 'Reach'){
    # Filtrer pour les combats avec une grande différence de portée
    fighter_Reach_sup <- ufc_data %>%
      filter(reach_dif > reach_dif_threshold | reach_dif < -reach_dif_threshold)
    
    # Calculer les victoires en fonction de l'avantage de portée
    victory_counts <- fighter_Reach_sup %>%
      mutate(reach_advantage_winner = ifelse((reach_dif > 0 & Winner == "Blue") | (reach_dif < 0 & Winner == "Red"), "Advantage Winner", "No Advantage Winner")) %>%
      count(reach_advantage_winner) %>%
      mutate(percentage = n / sum(n) * 100)
    
    # Créer le diagramme en camembert
    ggplot(victory_counts, aes(x = "", y = percentage, fill = reach_advantage_winner)) +
      geom_bar(stat = "identity", width = 1) +
      coord_polar("y", start = 0) +
      theme_void() +
      labs(fill = "Victory Type", title = "Pourcentage de Victoires avec/sans Avantage de Portée") +
      scale_fill_brewer(palette = "Set3") +
      geom_text(aes(label = paste0(round(percentage, 1), "%")), position = position_stack(vjust = 0.5))
  }
}


createUfcDecisionsPlot <- function(ufc_data, input) {
  if(input$stat_variable == 'Categorie') {
    # Calculer les décisions par catégorie de poids
    summary_data <- ufc_data %>%
      filter(!is.na(weight_class) & !is.na(finish)) %>%
      group_by(weight_class) %>%
      summarise(
        total_fights = n(),
        decisions = sum(finish == "U-DEC" | finish == "S-DEC" | finish == "M-DEC"),
        .groups = 'drop'
      ) %>%
      mutate(decision_percentage = (decisions / total_fights) * 100)
    
    # Créer un scatter plot
    ggplot(summary_data, aes(x = reorder(weight_class, decision_percentage), y = decision_percentage)) +
      geom_point(size = 4, color = "steelblue") +
      coord_flip() +
      labs(title = "Pourcentage de victoires par décision par classe de poids",
           x = "Classe de poids",
           y = "Pourcentage de décisions") +
      theme_minimal()
  }
}


createWinPercentageReachPlot <- function(ufc_data, input) {
  if(input$stat_variable == 'Reach' && is.numeric(input$reach_slider)) {
    reach_rounded <- round(input$reach_slider)
    
    wins <- ufc_data %>%
      filter(B_Reach_cms >= reach_rounded & B_Reach_cms < reach_rounded + 1 | 
               R_Reach_cms >= reach_rounded & R_Reach_cms < reach_rounded + 1) %>%
      summarise(Total = n(),
                Wins = sum(Winner == "Red", na.rm = TRUE)) # Ou "Blue" selon le côté que vous analysez
    
    win_percentage <- ifelse(wins$Total > 0, wins$Wins / wins$Total * 100, 0)
    
    pie_data <- data.frame(
      Group = c("Victoires", "Défaites"),
      Value = c(win_percentage, 100 - win_percentage)
    )
    
    ggplot(pie_data, aes(x = "", y = Value, fill = Group)) +
      geom_bar(width = 1, stat = "identity") +
      coord_polar("y", start = 0) +
      theme_void() +
      scale_fill_manual(values = c("green", "red")) +
      geom_text(aes(label = sprintf("%0.1f%%", Value)), 
                position = position_stack(vjust = 0.5)) +
      labs(title = "Pourcentage de victoire par Reach en cm")
  }
}



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


createStanceWinPlot <- function(ufc_data, input) {
  if (input$stat_variable == 'Stance') {
    filtered_df <- ufc_data %>%
      filter((R_Stance == "Orthodox" & B_Stance == "Southpaw") | 
               (R_Stance == "Southpaw" & B_Stance == "Orthodox"))
    
    victoires_orthodox <- sum((filtered_df$R_Stance == "Orthodox" & filtered_df$Winner == "Red") | 
                                (filtered_df$B_Stance == "Orthodox" & filtered_df$Winner == "Blue"))
    
    total_combats <- nrow(filtered_df)
    pourcentage_victoires_orthodox <- (victoires_orthodox / total_combats) * 100
    pourcentage_victoires_southpaw <- 100 - pourcentage_victoires_orthodox
    
    data_pie <- data.frame(
      Category = c("Orthodox", "Southpaw"),
      Percentage = c(pourcentage_victoires_orthodox, pourcentage_victoires_southpaw)
    )
    
    ggplot(data_pie, aes(x = "", y = Percentage, fill = Category)) +
      geom_bar(stat = "identity", width = 1) +
      coord_polar("y", start = 0) +
      theme_void() +
      theme(legend.title = element_blank()) +
      scale_fill_brewer(palette = "Set3") +
      geom_text(aes(label = paste0(round(Percentage, 1), "%")), position = position_stack(vjust = 0.5)) +
      labs(title = "Pourcentage de victoire Orthodox vs Southpaw")
  }
}


# Fonction pour le graphique B_TD_Age
createB_TDAgePlot <- function(data) {
  data <- data %>% filter(!is.na(B_age) & !is.na(B_avg_TD_landed))
  suppressWarnings({
    ggplot(data, aes(x = B_age, y = B_avg_TD_landed)) +
      geom_point(color = "blue") +
      theme_minimal() +
      labs(title = "Relation entre l'âge et le nombre moyen de takedowns réussis (combattants B)",
           x = "Âge du combattant B",
           y = "Moyenne de takedowns réussis")
  })
}

# Fonction pour le graphique B_STR_Age
createB_STRAgePlot <- function(data) {
  data <- data %>% filter(!is.na(B_age) & !is.na(B_avg_SIG_STR_landed))
  suppressWarnings({
    ggplot(data, aes(x = B_age, y = B_avg_SIG_STR_landed)) +
      geom_point(color = "blue") +
      theme_minimal() +
      labs(title = "Relation entre l'âge et le nombre moyen de coups significatifs atterris (combattants B)",
           x = "Âge du combattant B",
           y = "Moyenne de coups significatifs atterris")
  })
}

# Fonction pour le graphique R_STR_Age
createR_STRAgePlot <- function(data) {
  data <- data %>% filter(!is.na(R_age) & !is.na(R_avg_SIG_STR_landed))
  suppressWarnings({
    ggplot(data, aes(x = R_age, y = R_avg_SIG_STR_landed)) +
      geom_point(color = "red") +
      theme_minimal() +
      labs(title = "Relation entre l'âge et le nombre moyen de coups significatifs atterris (combattants R)",
           x = "Âge du combattant R",
           y = "Moyenne de coups significatifs atterris")
  })
}

# Fonction pour le graphique R_TD_Age
createR_TDAgePlot <- function(data) {
  data <- data %>% filter(!is.na(R_age) & !is.na(R_avg_TD_landed))
  suppressWarnings({
    ggplot(data, aes(x = R_age, y = R_avg_TD_landed)) +
      geom_point(color = "red") +
      theme_minimal() +
      labs(title = "Relation entre l'âge et le nombre moyen de takedowns réussis (combattants R)",
           x = "Âge du combattant R",
           y = "Moyenne de takedowns réussis")
  })
}

