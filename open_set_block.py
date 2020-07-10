import pygame
import math


class OpenBlock:
    def __init__(self, main, color, coords, prev_g, prev_coords):
        # initialize main settings
        self.screen = main.screen
        self.settings = main.settings
        self.coords = coords
        self.prev_coords = prev_coords
        self.prev_g = prev_g
        self.end_coords = main.end_coords
        self.h = self._calculate_h()
        self.g = self._calculate_g()
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
        self.center = self._grid_location(self.coords)

        # initialize fill
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.center

    def draw_open(self):
        pygame.draw.rect(self.screen, self.color, self.rect, width=2)

    def _grid_location(self, coords):
        x = self.settings.grid_width/2 * (coords[0]*2+1)
        y = self.settings.grid_height/2 * (coords[1]*2+1)
        new = (x, y)
        return new

    def _calculate_g(self):
        x1 = self.coords[0]
        x2 = self.prev_coords[0]
        y1 = self.coords[1]
        y2 = self.prev_coords[1]
        d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        return d

    def _calculate_h(self):
        x1 = self.coords[0]
        x2 = self.end_coords[0]
        y1 = self.coords[1]
        y2 = self.end_coords[1]
        d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        return d

    def change_color(self, color):
        self.color = self.color_map[color]
