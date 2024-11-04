# -*- coding: utf-8 -*-
from Case import Case

class CaseVide(Case):
    def __init__(self, x, y):
        """
        Initialise une instance de CaseVide, représentant une case vide avec 0 mines adjacentes.

        Parameters
        ----------
        x : int
            Coordonnée en x de la case sur la grille.
        y : int
            Coordonnée en y de la case sur la grille.

        Attributes
        ----------
        isDecouvert : bool
            Indique si la case est découverte.
        minesAdjacentes : int
            Nombre de mines autour de cette case (0 pour CaseVide).
        drapeau : bool
            Indique si un drapeau est placé sur cette case.
        isMine : bool
            Toujours False pour CaseVide, indique que la case ne contient pas de mine.
        """
        super().__init__(x, y, isDecouvert=False, minesAdjacentes=0, drapeau=False, isMine=False)
    
    def clicGauche(self):
        """
        Action effectuée lors d'un clic gauche sur une case vide.
        
        Si la case n'est pas déjà découverte et n'a pas de drapeau, elle est découverte
        et son état `isDecouvert` passe à True.

        Returns
        -------
        None
        """
        if not self.isDecouvert and not self.drapeau:
            self.isDecouvert = True
            # print(f"Case vide découverte à la position ({self.x}, {self.y})")
        else:
            print(f"Action impossible : {'drapeau présent' if self.drapeau else 'case déjà découverte'}")
