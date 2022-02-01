import pygame

from libs.button import Button
from constants import *


class ButtonObj():
    BUTTON_STYLE = {
        "hover_color": modRED,
        "clicked_color": modBLUE_1,
        "clicked_font_color":modBLACK,
        "hover_font_color": ORANGE,
    }

    def __init__(self, x, y, width, height, color, function, text, font=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.function = function
        self.text = text
        self.rect = pygame.rect.Rect(x, y, width, height)
        self.style = self.BUTTON_STYLE
        self.style['font'] = font
        self.button = Button((x, y, width, height), color, function, text=text, **self.style)

    def process_event(self, event):
        self.button.check_event(event)

    def process_draw(self, screen):
        self.button.update(screen)

    def update(self):
        self.button = Button((self.x, self.y, self.width, self.height), self.color, self.function, text=self.text,
                             **self.style)

    def reset_text(self, new_text):
        self.button = Button((self.x, self.y, self.width, self.height), self.color, self.function, text=new_text,
                             **self.style)
