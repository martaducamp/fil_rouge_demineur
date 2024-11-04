# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QMessageBox, QLabel
from PyQt5.QtCore import Qt, QTimer

from Jeu import Jeu
from CaseBouton import CaseBouton
import sys

class InterfaceJeu(QMainWindow):
    
    def __init__(self, difficulte):
        """
        Initialise l'interface du jeu Démineur avec la difficulté spécifiée.

        Parameters
        ----------
        difficulte : str
            Le niveau de difficulté sélectionné (facile, intermediaire, avance).

        """
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
        """
        Initialise l'interface utilisateur en créant le layout principal, les boutons de contrôle, 
        la grille de jeu, et le chronomètre.
        """
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
        
        for niveau in ["facile", "intermediaire", "avance"]:
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
        Crée et initialise la grille de jeu dans l'interface en générant des boutons pour chaque case.
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
        """
        Gère les clics de la souris sur les boutons de la grille, effectue l'action appropriée
        en fonction du bouton de la souris (découverte ou drapeau) et vérifie les conditions de victoire et de défaite.

        Parameters
        ----------
        bouton : CaseBouton
            Le bouton qui a été cliqué.
        event : QMouseEvent
            L'événement de clic de la souris contenant le type de clic.
        """
        x, y = bouton.x, bouton.y
        action_type = 'd' if event.button() == Qt.LeftButton else 'f'
        
        self.jeu.traiterCoup(x, y, action_type)
        self.mettre_a_jour_grille()
        
        if self.jeu.grille.victoire():
            QMessageBox.information(self, "Victoire", f"Vous avez gagné !\nTemps : {self.jeu.timer.get_time()}")
            self.interface_timer.stop()
        elif self.jeu.grille.defaite(x, y):
            QMessageBox.critical(self, "Défaite", "Vous avez perdu.")
            self.afficher_mines()
    
    def mettre_a_jour_grille(self):
        """
        Met à jour l'affichage de la grille de jeu en fonction de l'état actuel des cases,
        affichant les mines, les drapeaux, et les nombres de mines adjacentes.
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
                    bouton.setText("🚩")
                    bouton.setStyleSheet("color: red")
                else:
                    bouton.setText("")

    def afficher_mines(self):
        """
        Affiche toutes les mines présentes sur la grille lorsque le joueur perd la partie.
        """
        for x in range(self.jeu.grille.longueur):
            for y in range(self.jeu.grille.largeur):
                case = self.jeu.grille.grille[x][y]
                bouton = self.boutons_grille[x][y]
                if case.isMine:
                    bouton.setText("💣")
                    bouton.setStyleSheet("color: red")
                bouton.setEnabled(False)

    def update_timer_display(self):
        """
        Met à jour l'affichage du chronomètre dans l'interface en utilisant le temps actuel du jeu.
        """
        self.timer_label.setText(self.jeu.timer.get_time())

    def redemarrer(self):
        """
        Redémarre le jeu en réinitialisant la grille, le chronomètre, et le niveau de difficulté actuel.
        """
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
        """
        Change la difficulté du jeu et redémarre la partie avec le nouveau niveau.

        Parameters
        ----------
        difficulte : str
            Le nouveau niveau de difficulté choisi (facile, intermediaire, avance).
        """
        self.difficulte = difficulte
        self.redemarrer()

    @staticmethod
    def lancer_interface(difficulte):
        """
        Lance l'application graphique du jeu avec le niveau de difficulté spécifié.

        Parameters
        ----------
        difficulte : str
            Le niveau de difficulté initial (facile, intermediaire, avance).
        """
        app = QApplication(sys.argv)
        interface = InterfaceJeu(difficulte)
        sys.exit(app.exec_())


if __name__ == "__main__":
    difficulte = "facile"  # Choisir la difficulté initiale ici
    InterfaceJeu.lancer_interface(difficulte)
