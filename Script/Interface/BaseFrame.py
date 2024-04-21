import pygame as pg
from Script.Interface.TimerFrame import TimerFrame
from Script.Module import *

couleur = [(81, 91, 212), (129, 52, 175), (221, 42, 123), (245, 133, 41), (254, 218, 119)]


class BaseFrame:
    def __init__(self, x, y, width, height, liste_bouton, bouttonFrame, *timerContainerList):
        self.rect = pg.Rect(x, y, width, height)
        self.start_time = time.time()
        self.boutton_frame = bouttonFrame
        self.liste_bouton = liste_bouton
        self.liste_timer = list(timerContainerList)

    def draw(self, surface):
        pg.draw.rect(surface, couleur[4], self.rect)
        self.boutton_frame.draw(surface)
        for timer_container in self.liste_timer:
            timer_container.draw(surface)

    def add_timer_container(self, interface):
        x = 20
        y = 70 + len(self.liste_timer) * 60
        width = interface.width - 40
        height = 50
        depart = time.time()
        new_timer_container = TimerFrame(x, y, width, height, self.liste_bouton, interface.bouttonController, interface)
        if interface.timerContainer.md.is_playing:
            new_timer_container.md.play()
        self.liste_timer.append(new_timer_container)
