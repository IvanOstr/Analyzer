import collections

from shapes import circle, grid
from shapes import point
from constants import RADIUS
import numpy as np
from matplotlib import pyplot as plt


class Analyzer():
    def __init__(self, product, shelf, grid):
        product = product
        num_of_products = 0



    # returns data from the detectors in an easy to work with way
    def parse_data(self):
        pass

    # finds number of products on the shelf using data from parse_data.
    def find_number_of_products(self):
        self.exclude_products()
        self.count_products()


    # deletes unwanted detector points using product_obj.height.
    # products not corresponding to the product_obj.height are to be excluded, unless we identify it as the type
    # of product obj with different angle.
    def exclude_products(self):
        pass

    # counts the number of products using a clever algorithm.
    def count_products(self):
        pass