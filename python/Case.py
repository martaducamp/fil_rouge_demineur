from abc import ABC, abstractmethod

class Case(ABC):

    def __init__(self):
        pass
    
    @abstractmethod
    def afficher(self):
        """Méthode abstraite qui doit être implémentée dans les classes dérivées"""
        pass