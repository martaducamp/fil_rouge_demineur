from Case import Case

class Grille:
    
    DIFFICULTE = {
        "facile": {"taille_grille": (9, 9), "mines": 10},
        "intermediaire": {"taille_grille": (16, 16), "mines": 40},
        "avance": {"taille_grille": (30, 16), "mines": 99}
    }
    
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur =  largeur
        self.grille = []
        
    def creerGrille(self, difficulte):
        """
        Crée la grille en fonction de la difficulté choisie.
        :param difficulte: Le niveau de difficulté ("facile", "intermediaire", "avance")
        """
        if difficulte not in self.DIFFICULTE:
            raise ValueError(f"Difficulté inconnue : {difficulte}")
        
        # Récupération des paramètres de la difficulté
        params = self.DIFFICULTE[difficulte]
        taille_grille = params["taille_grille"]  # (longueur, largeur)
        nombre_mines = params["mines"]  # Nombre de mines

        # Redimensionner la grille en fonction de la difficulté
        self.longueur, self.largeur = taille_grille

        # Initialisation d'une grille vide (avec des instances de Case, CaseVide, etc.)
        self.grille = [[Case(x, y, False, 0, False) for y in range(self.largeur)] for x in range(self.longueur)]
        
        print(f"Grille créée avec la difficulté {difficulte}: {self.longueur}x{self.largeur} avec {nombre_mines} mines.")