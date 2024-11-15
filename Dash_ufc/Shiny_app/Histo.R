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
