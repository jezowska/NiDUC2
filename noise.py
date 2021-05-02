import numpy as np

class Noise(object):
    def __init__(self, bool_arr):
        self.size = len(bool_arr)
        self._bool_arr = bool_arr
        self.sample_arr = [0, 1]
        self.new_array = []

    def adding_noise_inc(self):
        prob = 0.5
        print(self._bool_arr)
        for i in range(self.size):
            x = np.random.choice(self.sample_arr)
            if( x > prob ):
                if(self._bool_arr[i] == 0):
                    self.new_array.append(1);
                    prob -= 0.01;
                else:
                    self.new_array.append(0);
            else:
                if(self._bool_arr[i] == 0):
                    self.new_array.append(0);
                else:
                    self.new_array.append(1);

        print(self._bool_arr)

    def adding_noise_dec(self):
        prob = 0.5
        for i in range(self.size):
            x = np.random.choice(self.sample_arr)
            if (x > prob):
                if (self._bool_arr[i] == 0):
                    self.new_array.append(1);
                    prob += 0.01;
                else:
                    self.new_array.append(0);
            else:
                if (self._bool_arr[i] == 0):
                    self.new_array.append(0);
                else:
                    self.new_array.append(1);

    def adding_noise(self):
        prob = 0.5
        for i in range(self.size):
            x = np.random.choice(self.sample_arr)
            if (x > prob):
                if (self._bool_arr[i] == 0):
                    self.new_array.append(1);
                    prob -= 0.01;
                else:
                    self.new_array.append(0);
            else:
                if (self._bool_arr[i] == 0):
                    self.new_array.append(0);
                else:
                    self.new_array.append(1);

    def return_array(self):
        return self.new_array;