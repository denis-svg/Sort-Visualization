import pygame.font


def fontSize():
    pygame.font.init()
    size = None
    for i in range(30):
        font = pygame.font.SysFont("norasi", i, True)
        text_width, text_height = font.size("0")
        print(text_width, text_height)
        if

fontSize()


class Button:
    def __init__(self, screen, settings, position, color, text):
        pygame.font.init()
        self.x = position[0]
        self.y = position[1]
        self.width = 0
        self.height = 0
        self.color = color
        self.text = text
        self.screen = screen
        self.settings = settings

