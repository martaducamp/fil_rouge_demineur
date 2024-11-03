# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QPushButton, QApplication
import sys
class CaseBouton(QPushButton):
    """
    Classe personnalisée de QPushButton qui permet de stocker les coordonnées de la case.
    """
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y




