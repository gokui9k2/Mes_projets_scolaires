createFinishCamPlot <- function(ufc_data, fighter_selected) {
  # Filtrer les données pour le combattant sélectionné
  fighter_finish_data <- ufc_data %>%
    filter(R_fighter == fighter_selected | B_fighter == fighter_selected)
  
  # Calculer le nombre total de combats et le nombre de victoires
  total_combats <- nrow(fighter_finish_data)
  total_wins <- nrow(fighter_finish_data %>% filter((R_fighter == fighter_selected & Winner == "Red") | (B_fighter == fighter_selected & Winner == "Blue")))
  
  # Vérifier si le combattant a des victoires
  if (total_wins > 0) {
    # Calculer les occurrences de chaque type de finition
    finish_occurrences <- table(fighter_finish_data$finish)
    
    # Créer un DataFrame pour le graphique
    finish_data_for_plot <- data.frame(
      Finish_Type = names(finish_occurrences),
      Count = as.numeric(finish_occurrences)
    )
    
    # Calculer les pourcentages
    finish_data_for_plot$Percentage <- finish_data_for_plot$Count / sum(finish_data_for_plot$Count) * 100
    
    # Créer un graphique en camembert
    ggplot(finish_data_for_plot, aes(x = "", y = Percentage, fill = Finish_Type)) +
      geom_bar(stat = "identity", width = 1) +
      coord_polar("y", start = 0) +
      theme_void() +
      scale_fill_manual(values = c("green", "red", "blue", "yellow", "orange", "purple", "pink", "brown", "grey", "cyan")) +
      geom_text(aes(label = sprintf("%0.1f%%", Percentage)), position = position_stack(vjust = 0.5)) +
      ggtitle("Finition des combattants en pourcentage")
  } else {
    # Afficher un message ou un graphique vide si le combattant n'a pas de victoires
    plot.new()
    title(main = "Aucune victoire pour ce combattant", sub = "Graphique non disponible")
  }
}



createFighterDetails <- function(ufc_data, selected_fighter) {
  req(selected_fighter) # s'assurer qu'un combattant est sélectionné
  
  # Filtrer les données pour obtenir les combats du combattant sélectionné
  fighter_data <- ufc_data %>%
    filter(R_fighter == selected_fighter | B_fighter == selected_fighter)
  
  # Calculer le nombre total de combats et le nombre de victoires
  total_combats <- nrow(fighter_data)
  total_wins <- nrow(fighter_data %>% filter((R_fighter == selected_fighter & Winner == "Red") | (B_fighter == selected_fighter & Winner == "Blue")))
  
  # Calculer le taux de victoire
  win_rate <- if (total_combats > 0) total_wins / total_combats else 0
  
  # Ajouter le taux de victoire aux détails du combattant
  fighter_data <- fighter_data %>%
    arrange(desc(date)) %>%
    slice(1) %>%
    mutate(Win_Rate = win_rate)
  
  # Sélectionner les colonnes appropriées
  if (fighter_data$R_fighter[1] == selected_fighter) {
    fighter_data %>%
      select(fighter = R_fighter, age = R_age, weight_lbs = R_Weight_lbs, stance = R_Stance, Nationalite = R_nat, weight_class, gender, Win_Rate)
  } else {
    fighter_data %>%
      select(fighter = B_fighter, age = B_age, weight_lbs = B_Weight_lbs, stance = B_Stance, Nationalite = B_nat, weight_class, gender, Win_Rate)
  }
}

