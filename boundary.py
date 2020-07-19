import pygame
import fill_block


class Boundary:
    """ A class to create a boudary to add complexity to A* Path finding Program"""

    def __init__(self, main, mouse_pos):
        # initialize main Settings
        self.screen = main.screen
        self.settings = main.settings
        # initialize line settings
        self.color = 'black'

        # self.start = (20, 2)

        #self.line_coords = []
        self.coords = mouse_pos
        self.block = fill_block.FillBlock(main, self.color, self.coords, 0, 0)
        # for i in range(self.start[1], self.end[1]+1):
        #     self.line_coords.append((self.start[0], i))

        # for coord in self.line_coords:
        #     block = fill_block.FillBlock(main, 'black', coord, 0, 0)
        #     self.box_group.append(block)

    def draw_boundary(self):
        self.block.draw_fill()
