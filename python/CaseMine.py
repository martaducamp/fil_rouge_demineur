from Case import Case

class CaseMine(Case):
    def __init__(self, x, y):
        """
        Initialise une case vide avec 0 mines adjacentes.
        
        :param x: Position x de la case
        :param y: Position y de la case
        :param minesAdjacentes : nombre de mines dans les 8 cases autour de la case
        """
        super().__init__(x, y,minesAdjacentes=0, isDecouvert=False, drapeau=False, isMine = True)
        
    def clicGauche(self):
        if not self.drapeau:
            self.isDecouvert = True
            print(f"Mine découverte à la position ({self.x}, {self.y}). Jeu perdu")