import pygame


class FillBlock:
    def __init__(self, main, color, coords, g, h):
        # initialize main settings
        self.screen = main.screen
        self.settings = main.settings
        self.h = h
        self.g = g
        self.f = self.g + self.h

        # initialize block
        self.color_map = {
            'red': (255, 0, 0),
            'black': (0, 0, 0),
            'green': (0, 255, 0),
            'blue': (0, 0, 255),
        }
        self.color = self.color_map[color]
        self.height = self.settings.grid_height
        self.width = self.settings.grid_width
        self.coords = coords
        self.center = self._grid_location(self.coords)

        # initialize fill
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.center

    def draw_fill(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def _grid_location(self, coords):
        x = self.settings.grid_width/2 * (coords[0]*2+1)
        y = self.settings.grid_height/2 * (coords[1]*2+1)
        new = (x, y)
        return new

    def change_color(self, color):
        self.color = self.color_map[color]
