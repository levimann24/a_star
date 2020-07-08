import pygame
import sys
import settings
import grid
import fill_block


class AStar:
    def __init__(self):
        self.settings = settings.Settings()

        # initialize the screen
        self.screen = pygame.display.set_mode(
            (self.settings.WIDTH, self.settings.HEIGHT))
        pygame.display.set_caption("A * Search Algorithm")

        # initialize the grid
        self.grid_lines = []
        self._create_grid()

        # initialize start
        start_center = self._grid_location((4, 4))
        self.start_location = fill_block.FillBlock(self, 'black', start_center)
        end_center = (self.settings.WIDTH - self.settings.grid_width/2,
                      self.settings.HEIGHT - self.settings.grid_height/2)
        self.end_location = fill_block.FillBlock(self, 'red', end_center)

    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def on_loop(self):
        pass

    def on_render(self):
        self.screen.fill(self.settings.bg_color)
        for line in self.grid_lines:
            line.draw_line()
        self.start_location.draw_fill()
        self.end_location.draw_fill()
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):

        while True:
            self.on_event()
            self.on_loop()
            self.on_render()
        self.on_cleanup()

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

    def _grid_location(self, coords):
        x = self.settings.grid_width/2 * (coords[0]*2+1)
        y = self.settings.grid_height/2 * (coords[1]*2+1)
        new = (x, y)
        return new


if __name__ == "__main__":
    game = AStar()
    game.on_execute()
