import numpy as np
import time

class Listener():
    def __init__(self, stable_time, init_mat):
        self.mat_before = init_mat
        self.stable_time = stable_time

    def get_data_from_sensors(self):
        return np.zeros([2,2])

    def listen(self):

        mat1 = self.get_data_from_sensors()
        time.sleep(self.stable_time)
        mat2 = self.get_data_from_sensors()

        # mat_diff = np.subtract(self.mat_before, new_mat)
        while True:
            if (mat1 == mat2).all() and not (self.mat_before - mat2).all():
                self.update_products()
                self.mat_before = mat2

            mat1 = self.get_data_from_sensors()
            time.sleep(self.stable_time)
            mat2 = self.get_data_from_sensors()

            time.sleep(1)


    def update_products(self):
        pass