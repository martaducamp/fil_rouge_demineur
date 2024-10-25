from Case import Case

class CaseVide(Case):
    def __init__(self, x, y):
        """
        Initialise une case vide avec 0 mines adjacentes.
        
        :param x: Position x de la case
        :param y: Position y de la case
        """
        super().__init__(x, y, isDecouvert=False, minesAdjacentes=0, drapeau=False)
    

    def clicGauche(self):
        """
        Action effectuée lors d'un clic gauche sur une case vide.
        Dévoile la case si elle n'a pas de drapeau et qu'elle n'est pas déjà découverte.
        """
        if not self.isDecouvert and not self.drapeau:
            self.isDecouvert = True
            # print(f"Case vide découverte à la position ({self.x}, {self.y})")
        else:
            print(f"Action impossible : {'drapeau présent' if self.drapeau else 'case déjà découverte'}")