from Script.Interface.Button import *
from Script.Interface.Interface import * 
import pygame as pg
import time


class Frame:
    def __init__(self, x, y, width, height, buttons, interface):
        self.rect = pg.Rect(x, y, width, height)
        self.start_time = time.time()

        self.x = x
        self.y = y
        self.largeur_BTN = 120
        hauteur_BTN = 30
        button_spacing = 1

        self.buttons_list = buttons
        self.buttons = [Button(x + 10 + i * (self.largeur_BTN + button_spacing), y + 10, self.largeur_BTN, hauteur_BTN, text, callback) for i, (text, callback) in enumerate(buttons)]
        self.pause_time = 0 

    def draw(self, surface):
        pg.draw.rect(surface, couleur[3], self.rect)

        for button in self.buttons:
            button.draw(surface)

    def handle_event(self, event,interface):
            for button in self.buttons:
                button.handle_event(event)
            for time_frame in interface.BaseFrame.liste_timer : 
                time_frame.handle_event(event)
            self.condition_handle_event(interface.bouttonController,interface)

    def bouttonCouleur(self,button):
        if button.is_clicked:
            button.set_color((255, 0, 0))
        else:
            button.set_color((0, 0, 255))

    def condition_handle_event(self,bouttonController,interface):
        for i in range(4):
            self.bouttonCouleur(self.buttons[i])

        if self.buttons[3].is_clicked:
            interface.BaseFrame.add_timer_container(interface)

            self.buttons[3].is_clicked = False

        elif self.buttons[2].is_clicked:
            if bouttonController.is_playing:
                bouttonController.stop()
                self.buttons[2].is_clicked = False
            elif bouttonController.is_paused:
                bouttonController.stop()
                self.pause_time = 0
                self.buttons[2].is_clicked = False
            else:
                self.buttons[2].is_clicked = False

        elif self.buttons[1].is_clicked: 
            if not bouttonController.is_paused and bouttonController.is_playing:
                bouttonController.pause()
                self.pause_time = bouttonController.pause_time
                self.buttons[1].is_clicked = False
            else:
                self.buttons[1].is_clicked = False
        
        elif self.buttons[0].is_clicked:
            if not bouttonController.is_playing:
                if bouttonController.is_paused:
                    bouttonController.resume()
                    self.buttons[0].is_clicked = False
                else:
                    bouttonController.play()
                    self.buttons[0].is_clicked = False
                self.bouttonCouleur(self.buttons[0])
            else:
                self.buttons[0].is_clicked = False
        