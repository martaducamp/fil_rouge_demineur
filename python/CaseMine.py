# -*- coding: utf-8 -*-
from Case import Case

class CaseMine(Case):
    def __init__(self, x, y):
        """
        Initialise une instance de CaseMine, représentant une case mine.

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
            Nombre de mines autour de cette case (0 ici car information pas pertinente).
        drapeau : bool
            Indique si un drapeau est placé sur cette case.
        isMine : bool
            Toujours True pour CaseMine, indique que la case est une mine.
        """
        super().__init__(x, y,minesAdjacentes=0, isDecouvert=False, drapeau=False, isMine=True)
        
    def clicGauche(self):
        """
        Action effectuée lors d'un clic gauche sur une case vide.
        
        Si la case n'est pas déjà découverte et n'a pas de drapeau, elle est découverte
        et son état `isDecouvert` passe à True.

        Returns
        -------
        None
        """
        if not self.drapeau and not self.isDecouvert:
            self.isDecouvert = True
            # print(f"Mine découverte à la position ({self.x}, {self.y}). Jeu perdu")
        # else:
        #     print(f"Action impossible : {'drapeau présent' if self.drapeau else 'case déjà découverte'}")