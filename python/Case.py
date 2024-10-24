from abc import ABC, abstractmethod

class Case(ABC):

    def __init__(self, x, y, isDecouvert, minesAdjascentes, drapeau):
        self.x = x
        self.y = y
        self.isDecouvert = False
        self.minesAdjascentes = minesAdjascentes
        self.drapeau = False
    
    @abstractmethod
    def clicGauche(self):
        """Méthode abstraite qui doit être implémentée dans les classes dérivées"""
        
        raise NotImplementedError
    
    def clicDroit(self, drapeau):
        drapeau = not drapeau
        print(f"Drapeau {'placé' if self.drapeau else 'retiré'} sur la case vide ({self.x}, {self.y})")
        

        
        