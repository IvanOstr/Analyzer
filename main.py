import collections
import analyzer
from products import product, rectprod, hotpop
from shelf import shelf
import time

from listener import listener
import numpy as np

from matplotlib import pyplot as plt

def is_height_same(mat_diff):
    # find if height is the same in the matrix
    values_in_mat = np.unique(mat_diff)
    return len(values_in_mat) > 2

def is_from_wanted_type(mat_diff, product):
    unique, counts = np.unique(mat_diff, return_counts = True)
    counts_dict = dict(zip(unique, counts))
    product_height = unique(1)
    (min_allowed_pnts, max_allowed_pnts) = product.get_allowed_range(product_height)
    lit_bits = counts_dict[product_height]
    return lit_bits >= min_allowed_pnts and lit_bits <= max_allowed_pnts


def get_sensor_config():
    pass

def plot_mat(mat):
    fig = plt.figure(figsize=(6, 3.2))

    ax = fig.add_subplot(111)
    ax.set_title('colorMap')
    plt.imshow(mat)
    ax.set_aspect('equal')

    cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
    cax.get_xaxis().set_visible(False)
    cax.get_yaxis().set_visible(False)
    cax.patch.set_alpha(0)
    cax.set_frame_on(False)
    plt.colorbar(orientation='vertical')
    plt.show()

def main():
    products_num = 1
    plot_mat_diff = True
    # time for the system to be stable
    stable_time = 0.5

    product = hotpop.HotPop()

    # shelf_height = 50
    # shelf_width = 40
    # shelf_length = 100
    # test_shelf = shelf.Shelf(shelf_height, shelf_length, shelf_width)

    mat_before = np.matrix([[4, 4, 1, 1, 0, 0], [4, 4, 1, 1, 0, 0], [5, 5, 5, 5, 0, 0], [5, 5, 5, 5, 0, 0]])
    mat_after = np.matrix([[4, 4, 1, 1, 0, 0], [4, 4, 1, 1, 0, 0], [5, 5, 5, 5, 1, 1], [5, 5, 5, 5, 1, 1]])

    # mat_before = get_sensor_config()
    # time.sleep(10)
    # mat_after = get_sensor_config()

    mat_diff = np.subtract(mat_before, mat_after)

    # listener_obj = listener.Listener(stable_time, mat_before)
    # listener_obj.listen()

    if not (mat_before == mat_after).all():
        print('Change Occured')

        if plot_mat_diff:
            plot_mat(mat_diff)

        if mat_diff.all() >= 0 or mat_diff.all() <= 0:
            print('All values are positive or negative')
            if is_height_same(mat_diff):
                if is_from_wanted_type(mat_diff, product):
                    if mat_diff.all() >= 0:
                        print("Product added")
                        products_num += 1
                    else:
                        print("Product removed")
                        products_num -= 1
            else:
                print('Product may be in a diagonal placement')
        else:
            print('Some negative some positive')
            if is_height_same(mat_diff):
                print('Product rotated or translated')
            else:
                print('Product moved on other product')




    print("hello2")


if __name__ == '__main__':
    main()