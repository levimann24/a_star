import pygame
import fill_block


class Boundary:
    """ A class to create a boudary to add complexity to A* Path finding Program"""

    def __init__(self, main):
        # initialize main Settings
        self.screen = main.screen
        self.settings = main.settings

        # initialize line settings
        self.color = 'black'

        self.start = (20, 2)
        self.end = (20, 40)

        self.line_coords = []
        self.box_group = []

        for i in range(self.start[1], self.end[1]+1):
            self.line_coords.append((self.start[0], i))

        for coord in self.line_coords:
            block = fill_block.FillBlock(main, 'black', coord, 0, 0)
            self.box_group.append(block)

        print(self.line_coords)

    def draw_boundary(self):
        for box in self.box_group:
            box.draw_fill()
