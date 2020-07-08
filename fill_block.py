import pygame


class FillBlock:
    def __init__(self, main, color, center):
        # initialize main settings
        self.screen = main.screen
        self.settings = main.settings

        # initialize block
        color_map = {
            'red': (255, 0, 0),
            'black': (0, 0, 0),
            'green': (0, 255, 0),
            'blue': (0, 0, 255),
        }
        self.color = color_map[color]
        self.height = self.settings.grid_height
        self.width = self.settings.grid_width
        self.center = center

        # initialize fill
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.center

    def draw_fill(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
