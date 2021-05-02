class RepetitionBitDecoder(object):

    def __init__(self, bool_arr):
        self.size = len(bool_arr)
        self._bool_arr = bool_arr
        self.decoded_arr = []

    def decoding(self):
        for i in range(0, self.size - 1, 3):

            if (self._bool_arr[i] == self._bool_arr[i + 1] or self._bool_arr[i] == self._bool_arr[i + 2]):
                self.decoded_arr.append(self._bool_arr[i])

            elif (self._bool_arr[i + 1] == self._bool_arr[i + 2]):
                self.decoded_arr.append(self._bool_arr[i + 1])
            print(i)

    def return_array(self):
        return self.decoded_arr
