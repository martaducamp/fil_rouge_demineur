from Grille import Grille
from Timer import Timer

class Jeu:
    
    DIFFICULTE = {
        "facile": {"taille_grille": (10, 10), "mines": 10},
        "intermediaire": {"taille_grille": (16, 16), "mines": 40},
        "avance": {"taille_grille": (30, 16), "mines": 99}
    }
    
    def __init__(self):
        pass