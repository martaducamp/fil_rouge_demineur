from Case import Case

class CaseNumero(Case):
    def __init__(self):
        super().__init__(contenu="numero")  # Le contenu est vide (None)
    
    def clicGauche(self):
        """
        Action effectuée lors d'un clic gauche sur une case vide.
        Dévoile la case si elle n'a pas de drapeau et qu'elle n'est pas déjà découverte.
        """
        if not self.isDecouvert and not self.drapeau:
            self.isDecouvert = True
            print(f"Case vide découverte à la position ({self.x}, {self.y})")
        else:
            print(f"Action impossible : {'drapeau présent' if self.drapeau else 'case déjà découverte'}")