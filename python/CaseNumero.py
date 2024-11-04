# -*- coding: utf-8 -*-
from Case import Case

class CaseNumero(Case):
    def __init__(self, x, y, minesAdjacentes):
        """
        Initialise une instance de CaseNumero, représentant une case sans mine 
        mais avec un nombre de mines adjacentes.

        Parameters
        ----------
        x : int
            Coordonnée en x de la case sur la grille.
        y : int
            Coordonnée en y de la case sur la grille.
        minesAdjacentes : int
            Nombre de mines adjacentes à cette case.

        Attributes
        ----------
        isDecouvert : bool
            Indique si la case est découverte.
        minesAdjacentes : int
            Nombre de mines autour de cette case.
        drapeau : bool
            Indique si un drapeau est placé sur cette case.
        isMine : bool
            Toujours False pour CaseNumero, indique que la case ne contient pas de mine.
        """
        super().__init__(x, y, isDecouvert=False, minesAdjacentes=minesAdjacentes, drapeau=False, isMine=False)
    
    def clicGauche(self):
        """
        Action effectuée lors d'un clic gauche sur une case sans mine.
        
        Si la case n'est pas déjà découverte et n'a pas de drapeau, elle est découverte
        et son état `isDecouvert` passe à True.

        Returns
        -------
        None
        """
        if not self.isDecouvert and not self.drapeau:
            self.isDecouvert = True
            # print(f"{self.minesAdjacentes} découvert à la position ({self.x}, {self.y})")
        # else:
        #     print(f"Action impossible : {'drapeau présent' if self.drapeau else 'case déjà découverte'}")
