from Case import Case
from CaseNumero import CaseNumero
from CaseVide import CaseVide
from CaseMine import CaseMine

import numpy as np
import random

class Grille:
    
    DIFFICULTE = {
        "facile": {"taille_grille": (9, 9), "mines": 10},
        "intermediaire": {"taille_grille": (16, 16), "mines": 40},
        "avance": {"taille_grille": (16, 30), "mines": 99},
        "surhomme": {"taille_grille": (50 ,50), "mines": 500},
        "extraterrestre": {"taille_grille": (100, 100), "mines": 1000}
    }
    
    def __init__(self, longueur, largeur):
        """
        Initialisation de la classe

        Parameters
        ----------
        longueur : int
            nombre de cases dans la largeur de la grille
        largeur : int
            nombre de cases dans la longueur de la grille

        Returns
        -------
        None.

        """
        self.longueur = longueur
        self.largeur =  largeur
        self.grille = []
        
    def creerGrille(self, difficulte):
        """
        Crée la grille en fonction de la difficulté choisie.
        :param difficulte: Le niveau de difficulté ("facile", "intermediaire", "avance")
        """
        if difficulte not in self.DIFFICULTE:
            raise ValueError(f"Difficulté inconnue : {difficulte}")
        
        # Récupération des paramètres de la difficulté
        params = self.DIFFICULTE[difficulte]
        taille_grille = params["taille_grille"]  # (longueur, largeur)
        nombre_mines = params["mines"]  # Nombre de mines

        # Redimensionner la grille en fonction de la difficulté
        self.longueur, self.largeur = taille_grille

        # Initialisation d'une grille vide
        self.grille = [[CaseVide(x, y) for y in range(self.largeur)] for x in range(self.longueur)]
        
        print(f"Grille créée avec la difficulté {difficulte}: {self.longueur}x{self.largeur}.")
        
    def placerMines(self, difficulte):
        """
        Place les mines aléatoirement sur la grille en fonction de la difficulté,
        en s'assurant que les mines ne sont pas placées sur les cases découvertes.

        Parameters
        ----------
        difficulte : str
            Le niveau de difficulté de la grille.

        Returns
        -------
        None.

        """
        
        if difficulte not in self.DIFFICULTE:
            raise ValueError(f"Difficulté inconnue : {difficulte}")
        
        # Récupération des paramètres de la difficulté
        params = self.DIFFICULTE[difficulte]
        nombre_mines = params["mines"]
        
        mines_placees = 0
        
        while mines_placees < nombre_mines:
            
            x = random.randit(0,self.longueur-1)
            y = random.randit(0, self.largeur-1)
            
            if not isinstance(self.grille[x][y], CaseMine) and not self.grille[x][y].isDecouvert:
                self.grille[x][y] = CaseMine(x,y)
                mines_placees +=1
        print(f"{nombre_mines} mines placées aléatoirement sur la grille.")
        
    def afficherGrille(self):
        """
        Affiche la grille dans la console.
        """
        
        for x in range(self.longueur):
            for y in range(self.largeur):
                case = self.grille[x][y]
                
                # Conditions pour afficher les cases (cela peut dépendre de ton implémentation de la classe Case)
                if not case.isDecouvert:
                    print("■", end=" ")  # Symbole pour une case non découverte
                elif case.minesAdjascentes > 0:
                    print(case.minesAdjascentes, end=" ")  # Nombre de mines adjacentes
                else:
                    print(" ", end=" ")  # Case vide découverte

            print()
    
    