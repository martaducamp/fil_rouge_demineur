# -*- coding: utf-8 -*-
from PyQt5.QtCore import QTimer

class Timer:
    def __init__(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.time_elapsed = 0
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.timer.start(1000)  # Mise à jour chaque seconde
            self.is_running = True

    def stop(self):
        if self.is_running:
            self.timer.stop()
            self.is_running = False

    def reset(self):
        self.stop()
        self.time_elapsed = 0

    def update_time(self):
        self.time_elapsed += 1

    def get_time(self):
        minutes = self.time_elapsed // 60
        seconds = self.time_elapsed % 60
        return f"{minutes:02}:{seconds:02}"