# -*- coding: utf-8 -*-
from Case import Case
from CaseNumero import CaseNumero
from CaseVide import CaseVide
from CaseMine import CaseMine

from collections import deque
import numpy as np
import random

class Grille:
    
    DIFFICULTE = {
        "facile": {"taille_grille": (9, 9), "mines": 10},
        "intermediaire": {"taille_grille": (16, 16), "mines": 40},
        "avance": {"taille_grille": (16, 30), "mines": 99}
    }
    
    def __init__(self, longueur, largeur, difficulte):
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
        self.difficulte =  difficulte
        self.grille = []
        
    def creerGrille(self):
        """
        Crée la grille ne fonction de la fiddigulté choisie.

        Raises
        ------
        ValueError
            Si la difficulté rentrée n'est pas dans le dictionnaire.
            Utile pour le débugage en console.

        Returns
        -------
        None.

        """
        if self.difficulte not in self.DIFFICULTE:
            raise ValueError(f"Difficulté inconnue : {self.difficulte}")
        
        # Récupération des paramètres de la difficulté
        params = self.DIFFICULTE[self.difficulte]
        taille_grille = params["taille_grille"]  # (longueur, largeur)
        # nombre_mines = params["mines"]  # Nombre de mines

        # Redimensionner la grille en fonction de la difficulté
        self.longueur, self.largeur = taille_grille

        # Initialisation d'une grille vide
        self.grille = [[CaseVide(x, y) for y in range(self.largeur)] for x in range(self.longueur)]
        
    def decouvrirCase(self, x, y):
        """
        Découvre la case aux coordonnées (x,y) et effectue l'action correspondante
        selon le type de case.

        Parameters
        ----------
        x : int
            Coordonnée x de la case à découvrir.
        y : int
            Coordonnée y de la case à découvrir.

        Returns
        -------
        None.

        """
        if x < 0 or x >= self.longueur or y < 0 or y >= self.largeur:
            return
        
        case = self.grille[x][y]
        case.clicGauche()
        
    def propagation(self, x, y):
        """
        Découvre toutes les cases vides connectées à la case (x, y) ainsi que les cases numérotées adjacentes.

        Parameters
        ----------
         x : int
            Coordonnée x de la case à découvrir.
        y : int
            Coordonnée y de la case à découvrir.

        Returns
        -------
        None.

        """

        file_a_traiter = deque([(x, y)])
        while file_a_traiter:
            cx, cy = file_a_traiter.popleft()
            case_actuelle = self.grille[cx][cy]

            # Découvrir la case si elle ne l'est pas déjà
            if not case_actuelle.isDecouvert:
                case_actuelle.clicGauche()
            
            # Si c'est une case numérotée, on s'arrête là (on ne continue pas la propagation)
            if isinstance(case_actuelle, CaseNumero):
                continue

            # Si c'est une case vide, on explore ses voisins
            for nx, ny in self.get_voisins(cx, cy):
                voisin = self.grille[nx][ny]

                # Si le voisin n'est pas découvert et n'est pas une mine, on l'ajoute à la file d'attente
                if not voisin.isDecouvert and not isinstance(voisin, CaseMine):
                    file_a_traiter.append((nx, ny))
    
    def get_voisins(self, x, y):
        """
        Retourne une liste des coordonnées des voisins valides (dans les limites de la grille) autour de la case (x, y).

        Parameters
        ----------
        x : int
            Coordonnée x de la case dont on cherche les vosins.
        y : int
            Coordonnée y de la case dont on cherche les vosins.

        Returns
        -------
        voisins : list
            liste des coordonnées des voisins.

        """
        voisins = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  # Ne pas ajouter la case elle-même
                nx, ny = x + dx, y + dy
                # Vérifier si les nouvelles coordonnées sont dans les limites de la grille
                if 0 <= nx < self.longueur and 0 <= ny < self.largeur:
                    voisins.append((nx, ny))
        return voisins
    
    def changeDrapeau(self, x, y):
        """
        Ajoute ou enlève un drapeau sur une case.

        Parameters
        ----------
        x : int
            coordonnée x de la case.
        y : int
            Coordonnée y de la case.

        Returns
        -------
        None.

        """
        if x < 0 or x >= self.longueur or y < 0 or y >= self.largeur:
            return
        
        case = self.grille[x][y]
        case.clicDroit()

    def chercherMinesAdjacentes(self, x, y):
        """
        Cherche le nombre de mines dans les cases adjacentes à la case (x, y).

        Parameters
        ----------
        x : int
            coordonnée x de la case.
        y : int
            Coordonnée y de la case.

        Returns
        -------
        mines_adjacentes : int
            Nombre de mines autour de la case.

        """
        mines_adjacentes = 0
        
        # Parcourir les cases dans une couronne autour de (x, y)
        for i in range(max(0, x - 1), min(self.longueur, x + 2)):  # De x-1 à x+1, sans dépasser les limites
            for j in range(max(0, y - 1), min(self.largeur, y + 2)):  # De y-1 à y+1, sans dépasser les limites
                if i == x and j == y:
                    # Ne pas compter la case elle-même
                    continue
                # Vérifier si la case adjacente est une mine
                if isinstance(self.grille[i][j], CaseMine):
                    mines_adjacentes += 1
        
        return mines_adjacentes
    
    def placerNumeros(self):
        """
        Initialise les cases numérotées après avoir placé les mines.

        Returns
        -------
        None.

        """
        for x in range(self.longueur):
            for y in range(self.largeur):
                if not isinstance(self.grille[x][y], CaseMine):
                    # Chercher les mines adjacentes pour cette case
                    nombre_mines = self.chercherMinesAdjacentes(x, y)
                    if nombre_mines > 0:
                        # Si des mines sont adjacentes, transformer la case en CaseNumero
                        self.grille[x][y] = CaseNumero(x, y, nombre_mines)
        
    def placerMines(self):
        """
        Place les mines aléatoirement sur la grille en fonction de la difficulté,
        en s'assurant que les mines ne sont pas placées sur les cases découvertes.



        Returns
        -------
        None.

        """
        
        if self.difficulte not in self.DIFFICULTE:
            raise ValueError(f"Difficulté inconnue : {self.difficulte}")
        
        # Récupération des paramètres de la difficulté
        params = self.DIFFICULTE[self.difficulte]
        nombre_mines = params["mines"]
        
        mines_placees = 0
        
        while mines_placees < nombre_mines:
            x = random.randint(0,self.longueur-1)
            y = random.randint(0, self.largeur-1)
            
            if not isinstance(self.grille[x][y], CaseMine) and not self.grille[x][y].isDecouvert:
                self.grille[x][y] = CaseMine(x,y)
                mines_placees +=1
        
    def afficherGrille(self):
        """
        Affiche la grille.
        """
        
        for x in range(self.longueur):
            for y in range(self.largeur):
                case = self.grille[x][y]
                
                # Conditions pour afficher les cases (cela peut dépendre de ton implémentation de la classe Case)
                if case.drapeau:
                    print("⚑", end =" ")
                elif not case.isDecouvert:
                    print("■", end=" ")  
                elif isinstance(case, CaseMine):
                    print("X", end =" ")
                elif case.minesAdjacentes > 0:
                    print(case.minesAdjacentes, end=" ") 
                else:
                    print(" ", end=" ")

            #print()
        
    def defaite(self, x, y):
        """
        Instancie les conditions de défaite pour chaque case cliquée

        Parameters
        ----------
        x : int
            coordonnée x de la case.
        y : int
            Coordonnée y de la case.

        Returns
        -------
        bool
            True si la case découverte est une mine.
            False sinon.

        """
        case = self.grille[x][y]
        if isinstance(case, CaseMine) and case.isDecouvert:
            return True
        return False
    
    def victoire(self):
        """
        Vérifie si le jeu est gagné.

        Returns
        -------
        bool
            True si le jeu est gagné, False sinon.

        """
        for ligne in self.grille:
            for case in ligne:
                if not isinstance(case, CaseMine) and not case.isDecouvert:
                    return False  
        
        return True  
        
    
    