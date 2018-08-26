from shapes import drawable
import math


class Point(drawable.Drawable):
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    def draw(self, fig, ax):
        ax.plot([self._x], [self._y], '.', color=self._color)

    def shift(self, x, y):
        self._x += x
        self._y += y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def get_color(self):
        return self._color

    def shift(self, shift_x, shift_y):
        self._x = self._x + shift_x
        self._y = self._y + shift_y

    def rotate(self, origin, angle):
        """
        Rotate a point counterclockwise by a given angle around a given origin.

        The angle should be given in radians.
        """
        angle = math.radians(angle)
        ox, oy = origin.x, origin.y
        px, py = self._x, self._y

        self._x = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        self._y  = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
