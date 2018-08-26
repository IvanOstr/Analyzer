import numpy as np
from matplotlib import pyplot as plt
from shapes import drawable, point


class Grid(drawable.Drawable):
    def __init__(self, width, height, spacing):
        self._width = width
        self._height = height
        self._offset = (0, 0)
        self._space = spacing
        self._create_lattice()

    def getSpacing(self):
        return self._space

    def draw(self, fig, ax):
        xs, ys = self.get_lattice()
        ax.plot(xs, ys, '.', color='black')

    def _create_lattice(self):
        x = np.arange(self._offset[0], self._width, self._space)
        y = np.arange(self._offset[1], self._height, self._space)
        self._xs = np.tile(x, len(y))
        self._ys = np.repeat(y, len(x))

    def shift(self, x, y):
        self._offset = (self._offset[0] + x, self._offset[1] + y)

    def get_lattice(self):
        return self._xs, self._ys

    def get_point_in_center(self):
        x_center = self._width/2
        y_center = self._height/2
        return (x_center,y_center)

    def get_dimensions(self):
        return len(self._xs), len(self._ys)