import pygame as pg
import random
from Script.Interface.Interface import * 
from Script.Interface.Button import Button
from Script.Module import * 

couleur = [(81,91,212),(129,52,175),(221,42,123),(245,133,41),(254,218,119)]
couleur2 = [(81,91,212),(129,52,175),(221,42,123),(245,133,41)]

class TimerFrame:
    def __init__(self,x,y,width, height, bouttons,bouttonController,interface):
        self.md = Module()
        self.rect = pg.Rect(x, y, width, height)
        self.couleur_aleatoire =random.choice(couleur2)
        self.buttons_list = bouttons
        self.interface = interface
        self.bouttonController = bouttonController

    def draw(self,surface):
        pg.draw.rect(surface, self.couleur_aleatoire, self.rect)
        milliemeseconde_show,second_show, minute_show, hours_show = self.md.time_counter()
        
        timer_text = f"{hours_show}:{minute_show}:{second_show}:{milliemeseconde_show}"

        font = pg.font.Font(None, 36)
        text_surface = font.render(timer_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.rect.centerx, self.rect.centery))
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        for button in self.buttons_list:
            if isinstance(button, Button):
                button.handle_event(event)
        if self.bouttonController: 
            for i, button in enumerate(self.buttons_list):
                
                if i == 2 and button.is_clicked:
                    if self.md.is_playing:
                        self.md.stop()
                    elif self.md.is_paused:
                        self.md.stop()
                        self.pause_time = 0
                    button.is_clicked = False

                elif i == 1 and button.is_clicked:
                    if not self.md.is_paused and self.md.is_playing:
                        self.md.pause()
                        self.pause_time = self.md.pause_time
                    button.is_clicked = False

                elif i == 0 and button.is_clicked:
                    if not self.md.is_playing:
                        if self.md.is_paused:
                            self.md.resume()
                        else:
                            self.md.play()
                    button.is_clicked = False