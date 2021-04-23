
import numpy as np

class BitString(object):
    def __init__ (self, size):
        self.Size = size
        sample_arr = [1, 0]
        self.bool_arr = np.random.choice(sample_arr, self.Size)

    def returnArray (self):
        return self.bool_arr
