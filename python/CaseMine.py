# -*- coding: utf-8 -*-
from Case import Case

class CaseMine(Case):
    def __init__(self, x, y):
        """
        Initialise une mine vide avec 0 mines adjacentes.
        
        :param x: Position x de la case
        :param y: Position y de la case
        """
        super().__init__(x, y,minesAdjacentes=0, isDecouvert=False, drapeau=False, isMine=True)
        
    def clicGauche(self):
        if not self.drapeau and not self.isDecouvert:
            self.isDecouvert = True
            # print(f"Mine découverte à la position ({self.x}, {self.y}). Jeu perdu")
        else:
            print(f"Action impossible : {'drapeau présent' if self.drapeau else 'case déjà découverte'}")