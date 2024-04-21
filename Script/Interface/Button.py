from Script.Interface.Interface import *

couleur = [(81, 91, 212), (129, 52, 175), (221, 42, 123), (245, 133, 41), (254, 218, 119)]


class Button:
    def __init__(self, x, y, width, height, text, fonction):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.font = pg.font.Font(None, 36)
        self.is_clicked = False
        self.callback = fonction
        self.color = couleur[0]

    def draw(self, surface):
        pg.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.is_clicked = True

    def set_color(self, color):
        self.color = color
