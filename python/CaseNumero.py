from Case import Case

class CaseNumero(Case):
    def __init__(self, x, y, minesAdjacentes):
        super().__init__(x, y, isDecouvert=False, minesAdjacentes=minesAdjacentes, drapeau=False, isMine = False)
    
    def clicGauche(self):
        """
        Action effectuée lors d'un clic gauche sur une case vide.
        Dévoile la case si elle n'a pas de drapeau et qu'elle n'est pas déjà découverte.
        """
        if not self.isDecouvert and not self.drapeau:
            self.isDecouvert = True
            print(f"{self.minesAdjacentes} découvert à la position ({self.x}, {self.y})")
        else:
            print(f"Action impossible : {'drapeau présent' if self.drapeau else 'case déjà découverte'}")