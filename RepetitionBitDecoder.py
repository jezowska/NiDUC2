class RepetitionBitDecoder(object):

    def __init__(self, bool_arr):
        self.size = len(bool_arr)
        self._bool_arr = bool_arr
        self.decoded_arr = []
        self.wykryte = 0;



    def decoding(self):
        counter = 0
        zeros = 0
        ones = 0
        for i in range(0, self.size):
            if self._bool_arr[i] == 0 : zeros += 1
            if self._bool_arr[i] == 1 : ones += 1
            counter += 1

            if(counter == 3):
                if(zeros > ones) :
                    self.decoded_arr.append(0)
                else:
                    self.decoded_arr.append(1)
                if(zeros != 3 and zeros != 0) :
                    self.wykryte += 1
                counter = 0
                zeros   = 0
                ones    = 0






    def return_array(self):
        return self.decoded_arr
