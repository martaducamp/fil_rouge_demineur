# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QMessageBox, QLabel
from PyQt5.QtCore import Qt, QTimer

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
        
        #Initialisation du timer
        self.interface_timer = QTimer()
        self.interface_timer.timeout.connect(self.update_timer_display)
        self.interface_timer.start(1000)
        
    def initUI(self):
        widget_central = QWidget(self)
        self.setCentralWidget(widget_central)
        
        self.layout_principal = QVBoxLayout(widget_central)

        # Affichage du chronomètre
        self.timer_label = QLabel("00:00", self)
        self.layout_principal.addWidget(self.timer_label)

        # Boutons de contrôle
        layout_boutons = QHBoxLayout()
        bouton_redemarrer = QPushButton("Redémarrer", self)
        bouton_redemarrer.clicked.connect(self.redemarrer)
        layout_boutons.addWidget(bouton_redemarrer)
        
        for niveau in ["facile", "moyen", "difficile"]:
            bouton_difficulte = QPushButton(niveau.capitalize(), self)
            bouton_difficulte.clicked.connect(lambda _, n=niveau: self.changer_difficulte(n))
            layout_boutons.addWidget(bouton_difficulte)
        
        self.layout_principal.addLayout(layout_boutons)

        # Grille de jeu
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
            QMessageBox.information(self, "Victoire", f"Vous avez gagné !\nTemps : {self.jeu.timer.get_time()}")
            self.interface_timer.stop()
        elif self.jeu.grille.defaite(x, y):
            QMessageBox.critical(self, "Défaite", f"Vous avez perdu.\nTemps : {self.jeu.timer.get_time()}")
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

    def update_timer_display(self):
        self.timer_label.setText(self.jeu.timer.get_time())

    def redemarrer(self):
        self.interface_timer.stop()
        for i in reversed(range(self.grille_layout.count())): 
            widget_to_remove = self.grille_layout.itemAt(i).widget()
            self.grille_layout.removeWidget(widget_to_remove)
            widget_to_remove.deleteLater()

        self.jeu = Jeu(self.difficulte)
        self.jeu.initialiser_jeu()
        self.creer_grille()
        self.interface_timer.start()

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
