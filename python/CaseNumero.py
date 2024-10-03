from Case import Case

class CaseVide(Case):
    def __init__(self):
        super().__init__(contenu="numero")  # Le contenu est vide (None)
    
    def afficher(self):
        return "Cette case est un numéro."