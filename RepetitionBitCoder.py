class RepetitionBitCoder(object):

    def __init__(self, bool_arr):
        self.size = len(bool_arr)
        self._bool_arr = bool_arr
        self.coded_arr = []

    def coding(self):
        for i in range(0, self.size):
            for j in range(3):
                self.coded_arr.append(self._bool_arr[i])


    def return_array(self):
        return self.coded_arr
    