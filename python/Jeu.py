from Grille import Grille
from Timer import Timer

class Jeu:
    
    DIFFICULTE = {
        "facile": {"taille_grille": (9, 9), "mines": 10},
        "intermediaire": {"taille_grille": (16, 16), "mines": 40},
        "avance": {"taille_grille": (30, 16), "mines": 99},
        "surhomme": {"taille_grille": (50 ,50), "mines": 500},
        "extraterrestre": {"taille_grille": (100, 100), "mines": 1000}
    }
    
    def __init__(self):
        pass