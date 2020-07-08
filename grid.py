import pygame


class Grid:
    def __init__(self, main, start, end):
        # initialize main settings
        self.screen = main.screen
        self.settings = main.settings

        # initialize lines
        self.start = start
        self.end = end
        self.color = self.settings.grid_color

    def draw_line(self):
        pygame.draw.line(self.screen, self.color,
                         self.start, self.end)
