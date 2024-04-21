import time
import pygame as pg
import sys
import os
import random

from Script.Interface.TimerFrame import TimerFrame
from Script.Module import *
from Script.Interface.Frame import Frame
from Script.Interface.Button import *
from Script.Interface.TimerFrame import *
from Script.Interface.BaseFrame import *

couleur = [(81, 91, 212), (129, 52, 175), (221, 42, 123), (245, 133, 41), (254, 218, 119)]
couleur2 = [(81, 91, 212), (129, 52, 175), (221, 42, 123), (245, 133, 41)]


class Interface:
    def __init__(self, width, height):
        pg.init()
        boutton_liste = [("Play", Module.play), ("Pause", Module.pause), ("Stop", Module.stop), ("+", Module.plus)]
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption("Chronomètre")
        self.clock = pg.time.Clock()
        heightFrame = 50
        self.is_running = True
        self.bouttonController = Controller()
        self.frame = Frame(10, 10, width - 20, heightFrame, boutton_liste, self)
        self.timerContainer = TimerFrame(20, heightFrame + 20, width - 40, heightFrame, self.frame.buttons,
                                         self.bouttonController, self)
        self.BaseFrame = BaseFrame(10, 10, width - 20, height - 20, self.frame.buttons, self.frame, self.timerContainer)
        icon = pg.image.load("icon.png")
        pg.display.set_icon(icon)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.is_running = False
            self.frame.handle_event(event, self)

    def update(self):
        pass

    def render(self):
        self.screen.fill(couleur[3])
        self.BaseFrame.draw(self.screen)
        pg.display.flip()

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

        pg.quit()
        sys.exit()


if __name__ == "__main__":
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(os.path.join(parent_dir, "../.."))
    os.system("python main.py")
