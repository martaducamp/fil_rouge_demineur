# -*- coding: utf-8 -*-
from PyQt5.QtCore import QTimer

class Timer:
    def __init__(self):
        """
        Initialise une instance de la classe Timer.
        
        Attributes
        ----------
        timer : QTimer
            Objet QTimer pour gérer le chronomètre.
        time_elapsed : int
            Temps écoulé en secondes.
        is_running : bool
            État du chronomètre (en cours d'exécution ou arrêté).
        """
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.time_elapsed = 0
        self.is_running = False

    def start(self):
        """
        Démarre le chronomètre si celui-ci n'est pas déjà en cours d'exécution.

        Returns
        -------
        None
        """
        if not self.is_running:
            self.timer.start(1000)  # Mise à jour chaque seconde
            self.is_running = True

    def stop(self):
        """
        Arrête le chronomètre s'il est en cours d'exécution.

        Returns
        -------
        None
        """
        if self.is_running:
            self.timer.stop()
            self.is_running = False

    def reset(self):
        """
        Réinitialise le chronomètre et arrête le décompte.

        Returns
        -------
        None
        """
        self.stop()
        self.time_elapsed = 0

    def update_time(self):
        """
        Incrémente le temps écoulé de 1 seconde. Appelée à chaque timeout du QTimer.

        Returns
        -------
        None
        """
        self.time_elapsed += 1

    def get_time(self):
        """
        Formate le temps écoulé en minutes et secondes.

        Returns
        -------
        str
            Temps écoulé au format "MM:SS".
        """
        minutes = self.time_elapsed // 60
        seconds = self.time_elapsed % 60
        return f"{minutes:02}:{seconds:02}"
