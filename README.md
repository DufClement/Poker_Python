# Poker_Python
Simple Poker Game in Python

# Sujet
Règles du jeu: Le poker éléctronique est un jeu de type machine à sous, le joueur choisi sa mise, appui sur le bouton "jouer" et la machine lui propose un jeu de 5 cartes tirés d'un jeu de 52 cartes. Le jouer peut alors choisir des cartes à garder, il peut choisir d'en garder 0, 1, 2, 3 ou 4, puis rappuie sur le bouton. Selon le choix du joueur, la machine tire de nouveaux le nombre de carte qu'il faut pour constituer le tirage final. Enfin le joueur récupère ses gains qui correspondent au montant de sa mise multiplié par le gain correspondant à la combinaison obtenue sur le tirage final. Si il n'a aucune combinaison il perd sa mise.

# Combinaison
- <strong> Paire </strong>: 2 cartes identiques => 1 fois la mise <br>
- <strong> Double Paire </strong>: deux fois 2 cartes identiques => 2 fois la mise <br>
- <strong> Brelan </strong>: 3 cartes identiques => 3 fois la mise <br>
- <strong> Quinte </strong>: 5 cartes consécutives => 4 fois la mise <br>
- <strong> Flush </strong>: 5 cartes de la même couleur => 6 fois la mise <br>
- <strong> Full </strong>: 1 paire + 1 brelan => 9 fois la mise <br>
- <strong> Carré </strong>: 4 cartes identiques => 25 fois la mise <br>
- <strong> Quinte Flush </strong>: 1 quinte de la même couleur => 50 fois la mise <br>
- <strong> Quinte Flush Royale </strong>: 1 quinte flush avec as, roi, dame, valet, 10 => 250 fois la mise <br>

# Installation 
- Installer python : https://www.python.org/
- Dans le dossier du projet : 
    - pip install flask
    - pip install pandas
    
# Lancement
- py app.py
