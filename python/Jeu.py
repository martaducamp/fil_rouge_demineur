from Grille import Grille
from Timer import Timer

class Jeu:
    
    
    def __init__(self, difficulte):
        """
        Initialisation du jeu avec un niveau de difficulté donné.

        Parameters
        ----------
        difficulte : str
            DESCRIPTION.

        Returns
        -------
        None.

        """
        
        self.difficulte = difficulte
        self.grille = None
        # self.timer = None 
        self.premiereAction = True  # Indique si la première action a été réalisée
        
    def initialiser_jeu(self):
        """
        Initialise la grille en fonction de la difficulté.
        """
        # Création de la grille selon la difficulté
        params = Grille.DIFFICULTE.get(self.difficulte)
        if not params:
            raise ValueError(f"Niveau de difficulté inconnu : {self.difficulte}")
        
        longueur, largeur = params["taille_grille"]
        self.grille = Grille(longueur, largeur)
        
        # Initialisation de la grille sans placer les mines au début
        self.grille.creerGrille(self.difficulte)

    def jouer(self):
        """
        Démarre la boucle principale du jeu, permet au joueur d'entrer des coordonnées pour découvrir des cases.
        """
        # Initialisation du jeu
        self.initialiser_jeu()
        
        # Boucle principale du jeu
        while True:
            try:
                x = int(input("Entrez la coordonnée x: "))
                y = int(input("Entrez la coordonnée y: "))
            except ValueError:
                print("Coordonnées invalides.")
                continue
            
            # Traiter le coup du joueur
            self.traiterCoup(x, y)
            
            # Condition de victoire ou de fin de jeu à gérer ici
            if self.finJeu():
                break

    def traiterCoup(self, x: int, y: int):
        """
        Traite le coup du joueur. Découvre la case et place les mines si c'est la première action.
        """
        if self.premiereAction:
            # Premier coup : on place les mines après le premier clic
            self.grille.placerMines(self.difficulte)
            self.premiereAction = False
        
        # Découvrir la case à la position donnée
        self.grille.decouvrirCase(x, y)
    
    def finJeu(self):
        """
        Vérifie si le jeu est terminé (victoire ou défaite).
        :return: True si le jeu est terminé, sinon False.
        """
        # Ici, tu pourrais ajouter une logique pour vérifier si toutes les cases non-mines ont été découvertes
        # Par exemple, pour vérifier si toutes les cases sans mines sont découvertes (victoire)
        # ou si une mine a été découverte (défaite).
        
        # Par exemple, condition pour quitter la boucle de jeu
        return False  # À ajuster selon tes conditions de fin de jeu

    
    