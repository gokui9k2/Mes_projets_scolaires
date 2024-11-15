# Définition de la fonction 'prepareData'
prepareData <- function(csv_file) {
  # La fonction prend un chemin de fichier CSV en entrée
  
  read_csv(csv_file, show_col_types = FALSE) %>%
    # Lit le fichier CSV spécifié.
    # 'show_col_types = FALSE' empêche l'affichage des types de colonnes lors du chargement des données.
    
    filter(B_Reach_cms > 0) %>%
    # Filtre les données pour ne conserver que les lignes où la valeur de 'B_Reach_cms' est supérieure à 0.
    # 'B_Reach_cms' pourrait représenter une mesure spécifique, comme la portée d'un combattant en centimètres.
    
    filter(!is.na(B_Stance))
  # Filtre les données pour exclure les lignes où la valeur de 'B_Stance' est NA (non disponible).
  # 'B_Stance' pourrait représenter la position de combat d'un combattant (par exemple, orthodoxe, southpaw).
}
