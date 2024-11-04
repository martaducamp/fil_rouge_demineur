# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class Case(ABC):
    def __init__(self, x, y, isDecouvert, minesAdjacentes, drapeau, isMine):
        """
        Initialise une case générique pour le jeu de démineur avec ses coordonnées et son état.

        Parameters
        ----------
        x : int
            Coordonnée en x de la case sur la grille.
        y : int
            Coordonnée en y de la case sur la grille.
        isDecouvert : bool
            Indique si la case est découverte.
        minesAdjacentes : int
            Nombre de mines adjacentes à cette case.
        drapeau : bool
            Indique si un drapeau est placé sur la case.
        isMine : bool
            Indique si la case contient une mine.

        Attributes
        ----------
        x : int
            Coordonnée en x de la case.
        y : int
            Coordonnée en y de la case.
        isDecouvert : bool
            État de découverte de la case.
        minesAdjacentes : int
            Nombre de mines autour de cette case.
        drapeau : bool
            État de drapeau de la case.
        isMine : bool
            Type de la case (mine ou non).
        """
        self.x = x
        self.y = y
        self.isDecouvert = isDecouvert
        self.minesAdjacentes = minesAdjacentes
        self.drapeau = drapeau
        self.isMine = isMine
    
    @abstractmethod
    def clicGauche(self):
        """
        Méthode abstraite qui doit être implémentée dans les classes dérivées.

        Cette méthode définit l'action à effectuer lors d'un clic gauche sur une case.
        """
        raise NotImplementedError
    
    def clicDroit(self):
        """
        Action effectuée lors d'un clic droit sur la case.

        Si la case n'est pas encore découverte, elle bascule l'état du drapeau.

        Returns
        -------
        None
        """
        if not self.isDecouvert:
            self.drapeau = not self.drapeau
        #     print(f"Drapeau {'placé' if self.drapeau else 'retiré'} sur la case ({self.x}, {self.y})")
        # else:
        #     print(f"Case ({self.x}, {self.y}) découverte. Impossible de placer un drapeau.")
