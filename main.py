from sys import exit
import pygame
from settings import Settings


class SortAi:
    def __init__(self):
        """Initialize Sort Visualization"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Sort Visualization')

    def mainLoop(self):
        while True:
            self._checkEvents()

    def _checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                self._checkKeyDownEvents(event)

    def _checkKeyDownEvents(self, event):
        if event.key == pygame.K_q:
            pygame.quit()
            exit()


if __name__ == "__main__":
    s = SortAi()
    s.mainLoop()
