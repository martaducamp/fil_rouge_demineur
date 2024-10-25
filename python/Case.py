from abc import ABC, abstractmethod

class Case(ABC):

    def __init__(self, x, y, isDecouvert, minesAdjacentes, drapeau):
        self.x = x
        self.y = y
        self.isDecouvert = isDecouvert
        self.minesAdjacentes = minesAdjacentes
        self.drapeau = drapeau
    
    @abstractmethod
    def clicGauche(self):
        """Méthode abstraite qui doit être implémentée dans les classes dérivées"""
        
        raise NotImplementedError
    
    def clicDroit(self):
        if not self.isDecouvert:
            self.drapeau = not self.drapeau
            print(f"Drapeau {'placé' if self.drapeau else 'retiré'} sur la case ({self.x}, {self.y})")
        else:
            print(f"Case ({self.x}, {self.y}) découverte. Impossible de placer un drapeau")
        

        
        