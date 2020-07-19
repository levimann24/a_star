import pygame
import sys
import settings
import grid
import fill_block
import open_set_block
import math
import boundary


class AStar:
    def __init__(self):
        pygame.init()
        self.settings = settings.Settings()

        # initialize the screen
        self.screen = pygame.display.set_mode(
            (self.settings.WIDTH, self.settings.HEIGHT))
        pygame.display.set_caption("A * Search Algorithm")

        # start variable
        self.start = False

        # initialize the grid
        self.grid_lines = []
        self._create_grid()

        # initialize start and end for testing
        start_center = (2, 2)
        end_center = (self.settings.WIDTH/self.settings.grid_width-2,
                      self.settings.HEIGHT/self.settings.grid_height-2)
        start_h = self._find_distance(start_center, end_center)
        self.start_location = fill_block.FillBlock(
            self, 'black', start_center, 0, start_h)
        self.end_location = fill_block.FillBlock(
            self, 'red', end_center, start_h, 0)
        self.end_coords = self.end_location.coords

        # Initialize start and end with mouse
        #self.start_center = None
        #self.end_center = None

        # initialize boundary testing
        #self.boundaries = boundary.Boundary(self)

        # initialize boundaries with mouse
        self.boundaries = []
        self.boundary_coords = []

        # initialize queue
        self.queue = []
        self.coords = []
        self.short_path = []
        self.horiz_verti = True
        self.diagonal = True
        self._create_queue(start_center, self.start_location.g)

    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    self.start = True
        self.mouse_press()

    def on_loop(self):
        if self.start:
            if self.queue:
                if self.short_path:
                    if self.short_path[-1].coords == self.end_coords:
                        pass
                    else:
                        self.check_lowest_f()
                        self._create_queue(
                            self.short_path[-1].coords, self.short_path[-1].g)
                else:
                    self.check_lowest_f()
                    self._create_queue(
                        self.short_path[-1].coords, self.short_path[-1].g)

    def on_render(self):
        self.screen.fill(self.settings.bg_color)
        for line in self.grid_lines:
            line.draw_line()
        self.start_location.draw_fill()
        self.end_location.draw_fill()
        for element in self.queue:
            element.draw_open()
        for element in self.short_path:
            element.draw_fill()
        for boundary in self.boundaries:
            boundary.draw_boundary()
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):

        while True:
            self.on_event()
            self.on_loop()
            self.on_render()
        self.on_cleanup()
# --------------------------------

    def check_lowest_f(self):
        lowest_f = None
        lowest_i = None
        for i in range(0, len(self.queue)):
            current_f = self.queue[i].f
            if i == 0:
                lowest_f = current_f
                lowest_i = i
            elif current_f < lowest_f:
                lowest_f = current_f
                lowest_i = i
        lowest_h = self.queue[lowest_i].h
        lowest_g = self.queue[lowest_i].g
        lowest_coords = self.queue[lowest_i].coords
        self._create_short_path(lowest_coords, lowest_g, lowest_h)
        del self.queue[lowest_i]

# ---------------------------------------------------------------------

    def _create_grid(self):
        # create x - axis lines
        n_x = int(self.settings.HEIGHT/self.settings.grid_height) + 1
        for i in range(0, n_x):
            start = (-1, i*self.settings.grid_height)
            end = (self.settings.WIDTH, i*self.settings.grid_height)
            line = grid.Grid(self, start, end)
            self.grid_lines.append(line)
        n_y = int(self.settings.WIDTH/self.settings.grid_width) + 1
        for j in range(0, n_y):
            start = (j*self.settings.grid_width, -1)
            end = (j*self.settings.grid_width, self.settings.HEIGHT)
            line = grid.Grid(self, start, end)
            self.grid_lines.append(line)

# ---------------------------------------------------------------------

    def _find_distance(self, start, end):
        x1 = start[0]
        x2 = end[0]
        y1 = start[1]
        y2 = end[1]
        d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        return d

# -------------------------------------------------------------------
    def _create_queue(self, node_coords, g):
        # if self.boundaries:
        #     self._create_boundary_coords()
        x = node_coords[0]
        y = node_coords[1]
        x_r = x + 1
        x_l = x - 1
        y_u = y - 1
        y_d = y + 1
        one = (x_l, y_u)
        two = (x, y_u)
        three = (x_r, y_u)
        four = (x_r, y)
        five = (x_r, y_d)
        six = (x, y_d)
        seven = (x_l, y_d)
        eight = (x_l, y)
        if self.horiz_verti and self.diagonal:
            coords = [one, two, three, four, five, six, seven, eight]
        elif self.horiz_verti:
            coords = [two, four, six, eight]
        else:
            coords = [one, three, five, seven]
        for node in coords:
            if node[0] < 0 or node[0] >= self.settings.WIDTH/self.settings.grid_width-1 or node[1] < 0 or node[1] >= self.settings.HEIGHT/self.settings.grid_height:
                continue
            elif node in self.coords:
                continue
            elif self.boundary_coords:
                if node in self.boundary_coords:
                    continue
            else:
                new = open_set_block.OpenBlock(
                    self, 'blue', node, g, node_coords)
                self.queue.append(new)
                self.coords.append(node)

    def _delete_queue(self, node):
        self.queue.remove(node)

    def _add_queue_coord(self, coord):
        self.coords.append(coord)

    def _del_queue_coord(self, coord):
        self.coords.remove(coord)

# ----------------------------------
    def _create_short_path(self, coords, g, h):
        new = fill_block.FillBlock(self, 'green', coords, g, h)
        self.short_path.append(new)

# TODO: MAKE IT EITHER HORIZONTAL/VERTICAL OR DIAGANAL OR BOTH
# TODO: MAKE IT TO WHERE YOU CAN DRAW SOME BOUNDARIES
# TODO: MAKE IT EASIER FOR THE COLORS TO CHANGE TO FILL AND NOT
    def mouse_press(self):
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            mouse_coord = (pos[0]//self.settings.grid_width,
                           pos[1]//self.settings.grid_height)
            bound = boundary.Boundary(self, mouse_coord)
            self.boundaries.append(bound)
            self.coords.append(mouse_coord)

        elif pygame.mouse.get_pressed()[2]:
            pass

    # def _create_boundary_coords(self):
    #     for boundary in self.boundaries:
    #         if boundary.coords not in self.boundary_coords:
    #             self.boundary_coords.append(boundary.coords)


if __name__ == "__main__":
    game = AStar()
    game.on_execute()
