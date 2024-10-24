from abc import ABC, abstractmethod

class Case(ABC):

    def __init__(self, x, y, isDecouvert, minesAdjacentes, drapeau, isMine):
        self.x = x
        self.y = y
        self.isDecouvert = False
        self.minesAdjacentes = minesAdjacentes
        self.drapeau = False
        self.isMine
    
    @abstractmethod
    def clicGauche(self):
        """Méthode abstraite qui doit être implémentée dans les classes dérivées"""
        
        raise NotImplementedError
    
    def clicDroit(self, drapeau):
        drapeau = not drapeau
        print(f"Drapeau {'placé' if self.drapeau else 'retiré'} sur la case vide ({self.x}, {self.y})")
        

        
        