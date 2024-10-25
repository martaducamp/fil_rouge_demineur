# -*- coding: utf-8 -*-
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
        self.grille = Grille(longueur, largeur, self.difficulte)
        
        # Initialisation de la grille sans placer les mines au début
        self.grille.creerGrille()
        self.grille.afficherGrille()

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
                action = str(input("Entrez le type d'action (f pour drapeau et d pour découvrir): "))
            except ValueError:
                print("Coordonnées invalides.")
                continue
            
            # Traiter le coup du joueur
            self.traiterCoup(x, y, action)
            self.grille.afficherGrille()
            
            # Condition de victoire ou de fin de jeu à gérer ici
            if self.grille.victoire():
                print("Vous avez gagné !")
                break
            if self.grille.defaite(x,y):
                print("Vous avez perdu :(")
                break

    def traiterCoup(self, x: int, y: int, action: str):
        """
        Traite le coup du joueur. Découvre la case et place les mines si c'est la première action.
        """
        if self.premiereAction:
            if action == "d":
                self.grille.decouvrirCase(x,y)
                self.grille.placerMines()
                self.grille.placerNumeros()
                self.grille.propagation(x,y)
                self.premiereAction = False
            elif action == "f":
                self.grille.changeDrapeau(x,y)
            else:
                print("Action non existante.")
        else :
            if action == "d":
                if self.grille.grille[x][y].isMine:
                    self.grille.decouvrirCase(x,y)
                else :
                    self.grille.propagation(x, y)
            elif action == "f":
                self.grille.changeDrapeau(x,y)
            else:
                print("Action non existante.")
    


    
    