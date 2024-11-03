# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

from Jeu import Jeu
from CaseBouton import CaseBouton
import sys

class InterfaceJeu(QMainWindow):
    def __init__(self, difficulte):
        super().__init__()
        self.setWindowTitle("Démineur")
        
        # Initialise la difficulté et le jeu
        self.difficulte = difficulte
        self.jeu = Jeu(difficulte)
        self.jeu.initialiser_jeu()
        
        # Crée la grille dans l'interface
        self.boutons_grille = []
        self.initUI()
        
    def initUI(self):
        # Création d'un widget central et d'un layout principal vertical
        widget_central = QWidget(self)
        self.setCentralWidget(widget_central)
        
        # Layout principal
        self.layout_principal = QVBoxLayout(widget_central)

        # Création d'un layout pour les boutons de contrôle
        layout_boutons = QHBoxLayout()
        
        # Bouton pour redémarrer la partie
        bouton_redemarrer = QPushButton("Redémarrer", self)
        bouton_redemarrer.clicked.connect(self.redemarrer)
        layout_boutons.addWidget(bouton_redemarrer)
        
        # Boutons pour changer la difficulté
        for niveau in ["facile", "intermediaire", "avance"]:
            bouton_difficulte = QPushButton(niveau.capitalize(), self)
            bouton_difficulte.clicked.connect(lambda _, n=niveau: self.changer_difficulte(n))
            layout_boutons.addWidget(bouton_difficulte)
        
        # Ajouter le layout des boutons au layout principal
        self.layout_principal.addLayout(layout_boutons)

        # Création initiale du layout de la grille
        self.grille_layout = QGridLayout()
        self.layout_principal.addLayout(self.grille_layout)
        
        self.creer_grille()
        self.show()

    def creer_grille(self):
        """
        Crée la grille de jeu dans l'interface.
        """
        self.boutons_grille.clear()
        
        for x in range(self.jeu.grille.longueur):
            ligne_boutons = []
            for y in range(self.jeu.grille.largeur):
                bouton = CaseBouton(x, y)
                bouton.setFixedSize(30, 30)
                bouton.mousePressEvent = lambda event, bx=bouton: self.gestion_clic(bx, event)
                
                self.grille_layout.addWidget(bouton, x, y)
                ligne_boutons.append(bouton)
            self.boutons_grille.append(ligne_boutons)

    def gestion_clic(self, bouton, event):
        x, y = bouton.x, bouton.y
        action_type = 'd' if event.button() == Qt.LeftButton else 'f'
        
        self.jeu.traiterCoup(x, y, action_type)
        self.mettre_a_jour_grille()
        
        if self.jeu.grille.victoire():
            QMessageBox.information(self, "Victoire", "Vous avez gagné !")
            self.close()
        elif self.jeu.grille.defaite(x, y):
            QMessageBox.critical(self, "Défaite", "Vous avez perdu.")
            self.afficher_mines()
    
    def mettre_a_jour_grille(self):
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
                    bouton.setText("🚩")
                else:
                    bouton.setText("")

    def afficher_mines(self):
        for x in range(self.jeu.grille.longueur):
            for y in range(self.jeu.grille.largeur):
                case = self.jeu.grille.grille[x][y]
                bouton = self.boutons_grille[x][y]
                if case.isMine:
                    bouton.setText("💣")
                    bouton.setStyleSheet("color: red")
                bouton.setEnabled(False)

    def redemarrer(self):
        """
        Redémarre le jeu avec la difficulté actuelle.
        """
        # Supprime la grille actuelle
        for i in reversed(range(self.grille_layout.count())): 
            widget_to_remove = self.grille_layout.itemAt(i).widget()
            self.grille_layout.removeWidget(widget_to_remove)
            widget_to_remove.deleteLater()

        # Redémarre le jeu avec la même difficulté
        self.jeu = Jeu(self.difficulte)
        self.jeu.initialiser_jeu()
        
        # Recrée la grille graphique
        self.creer_grille()

    def changer_difficulte(self, difficulte):
        self.difficulte = difficulte
        self.redemarrer()

    @staticmethod
    def lancer_interface(difficulte):
        app = QApplication(sys.argv)
        interface = InterfaceJeu(difficulte)
        sys.exit(app.exec_())


if __name__ == "__main__":
    difficulte = "facile"  # Choisir la difficulté initiale ici
    InterfaceJeu.lancer_interface(difficulte)
