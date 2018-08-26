import shapes.grid as grid
import shapes.point as point

import numpy as np
from matplotlib import pyplot as plt
from shapes import circle, grid, point

import timeit



def side(a, b, c):
    """ Returns a position of the point c relative to the line going through a and b
        Points a, b are expected to be different
    """
    d = (c.y - a.y) * (b.x - a.x) - (b.y - a.y) * (c.x - a.x)
    return 1 if d > 0 else (-1 if d < 0 else 0)


def is_point_in_closed_segment(a, b, c):
    """ Returns True if c is inside closed segment, False otherwise.
        a, b, c are expected to be collinear
    """
    if a.x < b.x:
        return a.x <= c.x and c.x <= b.x
    if b.x < a.x:
        return b.x <= c.x and c.x <= a.x

    if a.y < b.y:
        return a.y <= c.y and c.y <= b.y
    if b.y < a.y:
        return b.y <= c.y and c.y <= a.y

    return a.x == c.x and a.y == c.y


#
def closed_segment_intersect(a, b, c, d):
    """ Verifies if closed segments a, b, c, d do intersect.
    """
    if a == b:
        return a == c or a == d
    if c == d:
        return c == a or c == b

    s1 = side(a, b, c)
    s2 = side(a, b, d)

    # All points are collinear
    if s1 == 0 and s2 == 0:
        return \
            is_point_in_closed_segment(a, b, c) or is_point_in_closed_segment(a, b, d) or \
            is_point_in_closed_segment(c, d, a) or is_point_in_closed_segment(c, d, b)

    # No touching and on the same side
    if s1 and s1 == s2:
        return False

    s1 = side(c, d, a)
    s2 = side(c, d, b)

    # No touching and on the same side
    if s1 and s1 == s2:
        return False

    return True


def do_cubes_intersect(a, b, c, d, e, f, g, h):
    return closed_segment_intersect(e, f, a, b) or closed_segment_intersect(e, g, a, b) or closed_segment_intersect(h,
                                                                                                                    g,
                                                                                                                    a,
                                                                                                                    b) or closed_segment_intersect(
        h, f, a, b) or \
           closed_segment_intersect(e, f, a, c) or closed_segment_intersect(e, g, a, c) or closed_segment_intersect(h,
                                                                                                                    g,
                                                                                                                    a,
                                                                                                                    c) or closed_segment_intersect(
        h, f, a, c) or \
           closed_segment_intersect(e, f, d, c) or closed_segment_intersect(e, g, d, c) or closed_segment_intersect(h,
                                                                                                                    g,
                                                                                                                    d,
                                                                                                                    c) or closed_segment_intersect(
        h, f, d, c) or \
           closed_segment_intersect(e, f, d, b) or closed_segment_intersect(e, g, d, b) or closed_segment_intersect(h,
                                                                                                                    g,
                                                                                                                    d,
                                                                                                                    b) or closed_segment_intersect(
        h, f, d, b)


def draw_line_between_2_points(a, b, fig, ax, color='red'):
    ax.plot([a.x, b.x], [a.y, b.y], color, linewidth=1.2)


def draw_square(a, b, c, d, fig, ax, color='red'):
    draw_line_between_2_points(a, b, fig, ax, color)
    draw_line_between_2_points(a, c, fig, ax, color)
    draw_line_between_2_points(d, c, fig, ax, color)
    draw_line_between_2_points(d, b, fig, ax, color)


def is_square_near(e, max_x, min_x, max_y, min_y, scaling_param):
    mid_x = (max_x + min_x) / 2
    mid_y = (max_y + min_y) / 2

    return abs(mid_x - e.x) < scaling_param and abs(mid_y - e.y) < scaling_param
    # return (( e.x > max_x and e.x - max_x <= 3) or (e.x < min_x and min_x - e.x <= 3)) and \
    #        ((e.y > max_y and e.y - max_y <= 3) or (e.y < min_y and min_y - e.y <= 3))


def draw_rect(a, b, c, d, grid_length, grid_width, grid_spacing, title):
    fig, ax = plt.subplots()
    plt.axis('equal')
    ax.set_xticks(np.arange(0, grid_length, grid_spacing))
    ax.set_yticks(np.arange(0, grid_width, grid_spacing))

    ax.set_ylim((0, grid_width))
    ax.set_xlim((0, grid_length))
    plt.grid()

    draw_square(a, b, c, d, fig, ax, 'red')
    plt.title(title)
    plt.show()


def find_space_between_ones(arr):
    for i in range(len(arr) - 1):
        sum_adjacent_elem = arr[i + 1] - arr[i]
        if sum_adjacent_elem > 1:
            return sum_adjacent_elem - 1
    return 0
    # for i in range(len(arr)):
    #     if arr[i] == 1 and arr[i + 1] == 0:
    #         first_i = i
    #     if arr[i] == 0 and arr[i + 1] == 1 and first_i != 0:
    #         last_i = i +1


def find_num_of_squares_touching(a, b, c, d, grid, grid_spacing, prod_length, prod_width, to_plot=False):
    spacing = grid.getSpacing()
    (xs, ys) = grid.get_lattice()
    xs = set(xs)
    ys = set(ys)

    square_count = 0
    min_x = min(a.x, b.x, c.x, d.x)
    max_x = max(a.x, b.x, c.x, d.x)
    min_y = min(a.y, b.y, c.y, d.y)
    max_y = max(a.y, b.y, c.y, d.y)
    (x_cent, y_cent) = grid.get_point_in_center()
    scaling_param = max(prod_length, prod_width)
    on_bit = 1

    light_matrix = np.zeros(shape=(grid.get_dimensions()))

    for x in xs:
        # print(x)
        for y in ys:
            e = point.Point(x, y, 'black')
            f = point.Point(x, y + spacing, 'black')
            g = point.Point(x + spacing, y, 'black')
            h = point.Point(x + spacing, y + spacing, 'black')

            if is_square_near(e, max_x, min_x, max_y, min_y, scaling_param):
                # print(x,y)
                if do_cubes_intersect(a, b, c, d, e, f, g, h):
                    square_count += 1
                    light_matrix[int(x / grid_spacing)][int(y / grid_spacing)] = on_bit

    for column in light_matrix:
        one_indexes = np.where(column == on_bit)
        if one_indexes[0].any():
            # print(one_indexes[0])
            square_count += find_space_between_ones(one_indexes[0])

    if to_plot:
        plt.show()

    return square_count


def find_max_min_square_count(grid_length, grid_width, grid_spacing, prod_length, prod_width, to_plot=False):
    min_num_of_squares = 100
    max_num_of_squares = -100
    max_pnts = []
    min_pnts = []

    g = grid.Grid(grid_length, grid_width, grid_spacing)
    (x_cent, y_cent) = g.get_point_in_center()

    shifts = np.arange(0, 3.1, 0.1)
    angles = np.arange(0, 46, 0.5)
    for shift_x in shifts:

        for shift_y in shifts:
            a = point.Point(x_cent - prod_length / 2, y_cent - prod_width / 2, 'black')
            b = point.Point(x_cent + prod_length / 2, y_cent - prod_width / 2, 'black')
            c = point.Point(x_cent - prod_length / 2, y_cent + prod_width / 2, 'black')
            d = point.Point(x_cent + prod_length / 2, y_cent + prod_width / 2, 'black')

            a.shift(shift_x, shift_y)
            b.shift(shift_x, shift_y)
            c.shift(shift_x, shift_y)
            d.shift(shift_x, shift_y)
            for angle in angles:

                a.rotate(a, angle)
                b.rotate(a, angle)
                c.rotate(a, angle)
                d.rotate(a, angle)
                if to_plot:
                    draw_rect(a, b, c, d, grid_length, grid_width, grid_spacing,
                              'shift x = {0}, shift y = {1}, angle rotation = {2}'.format(shift_x, shift_y, angle))

                num_of_squares_touched = find_num_of_squares_touching(a, b, c, d, g, grid_spacing, prod_width, to_plot)
                if num_of_squares_touched > max_num_of_squares:
                    max_num_of_squares = num_of_squares_touched
                    max_a = point.Point(a.x, a.y, 'black')
                    max_b = point.Point(b.x, b.y, 'black')
                    max_c = point.Point(c.x, c.y, 'black')
                    max_d = point.Point(d.x, d.y, 'black')
                    max_pnts = [max_a, max_b, max_c, max_d]
                elif num_of_squares_touched < min_num_of_squares:
                    min_num_of_squares = num_of_squares_touched
                    min_a = point.Point(a.x, a.y, 'black')
                    min_b = point.Point(b.x, b.y, 'black')
                    min_c = point.Point(c.x, c.y, 'black')
                    min_d = point.Point(d.x, d.y, 'black')
                    min_pnts = [min_a, min_b, min_c, min_d]

    return min_num_of_squares, max_num_of_squares, min_pnts, max_pnts

