from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from Jeu import Jeu  # Importe ta classe Jeu
import sys

class InterfaceJeu(QMainWindow):
    def __init__(self, difficulte):
        super().__init__()
        self.setWindowTitle("Démineur")
        
        # Initialise le jeu
        self.jeu = Jeu(difficulte)
        self.jeu.initialiser_jeu()
        
        # Crée la grille dans l'interface
        self.boutons_grille = []
        self.initUI()
        
    def initUI(self):
        # Création d'un widget central et d'un layout de grille
        widget_central = QWidget(self)
        self.setCentralWidget(widget_central)
        
        grille_layout = QGridLayout(widget_central)
        
        for x in range(self.jeu.grille.longueur):
            ligne_boutons = []
            for y in range(self.jeu.grille.largeur):
                bouton = CaseBouton(x, y)
                bouton.setFixedSize(30, 30)
                bouton.mousePressEvent = lambda event, bx=bouton: self.gestion_clic(bx, event)
                
                grille_layout.addWidget(bouton, x, y)
                ligne_boutons.append(bouton)
            self.boutons_grille.append(ligne_boutons)
        
        self.show()
    
    def gestion_clic(self, bouton, event):
        """
        Gère le clic souris sur une case pour découvrir ou placer un drapeau.
        
        Parameters
        ----------
        bouton : CaseBouton
            Le bouton représentant la case cliquée.
        event : QMouseEvent
            L'événement de clic de souris pour déterminer si le clic est gauche ou droit.
        """
        x, y = bouton.x, bouton.y
        action_type = 'd' if event.button() == Qt.LeftButton else 'f'
        
        # Traite le coup du joueur dans la logique du jeu
        self.jeu.traiterCoup(x, y, action_type)
        
        # Met à jour l'affichage de la grille
        self.mettre_a_jour_grille()
        
        # Vérifie les conditions de fin de jeu
        if self.jeu.grille.victoire():
            QMessageBox.information(self, "Victoire", "Vous avez gagné !")
            self.close()
        elif self.jeu.grille.defaite(x, y):
            QMessageBox.critical(self, "Défaite", "Vous avez perdu.")
            self.afficher_mines()
    
    def mettre_a_jour_grille(self):
        """
        Met à jour l'affichage des boutons selon l'état de la grille de jeu.
        """
        for x in range(self.jeu.grille.longueur):
            for y in range(self.jeu.grille.largeur):
                case = self.jeu.grille.grille[x][y]
                bouton = self.boutons_grille[x][y]
                
                if case.isDecouvert:
                    if case.isMine:
                        bouton.setText("💣")
                        bouton.setStyleSheet("color: red")
                    elif case.minesAdjacentes > 0:
                        bouton.setText(str(case.minesAdjacentes))
                    else:
                        bouton.setText("")
                    bouton.setEnabled(False)
                elif case.drapeau:
                    bouton.setText("⚑")
                else:
                    bouton.setText("")
    
    def afficher_mines(self):
        """
        Affiche toutes les mines en cas de défaite.
        """
        for x in range(self.jeu.grille.longueur):
            for y in range(self.jeu.grille.largeur):
                case = self.jeu.grille.grille[x][y]
                bouton = self.boutons_grille[x][y]
                if case.isMine:
                    bouton.setText("💣")
                    bouton.setStyleSheet("color: red")
                bouton.setEnabled(False)

class CaseBouton(QPushButton):
    """
    Classe personnalisée de QPushButton qui permet de stocker les coordonnées de la case.
    """
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

def lancer_interface(difficulte):
    """
    Fonction principale pour lancer l'interface graphique avec le niveau de difficulté.
    """
    app = QApplication(sys.argv)
    interface = InterfaceJeu(difficulte)
    sys.exit(app.exec_())

# Pour lancer l'interface
if __name__ == "__main__":
    difficulte = "facile"  # Choisir la difficulté ici
    lancer_interface(difficulte)
