import numpy as np

class ParityBitDecoder(object):

    def __init__(self, size, bool_arr):
        self.Size = size
        self.decoded_arr = []
        self.Bool_arr = bool_arr

    def Decoding(self):
        for i in range(0, self.Size-6, 7):
            # Assigning expected value of parity bits 1, 2 and 3 to variables
            if self.Bool_arr[i] + self.Bool_arr[i + 1] + self.Bool_arr[i + 3] == 0 or self.Bool_arr[i] + \
                    self.Bool_arr[i + 1] + self.Bool_arr[i + 3] == 2:
                self.pb1 = 0
            else:
                self.pb1 = 1
            # Assigning value to second parity bit
            if self.Bool_arr[i + 1] + self.Bool_arr[i + 2] + self.Bool_arr[i + 3] == 0 or self.Bool_arr[i + 1] + \
                        self.Bool_arr[i + 2] + self.Bool_arr[i + 3] == 2:
                self.pb2 = 0
            else:
                self.pb2 = 1
            # Assigning value to third parity bit
            if self.Bool_arr[i] + self.Bool_arr[i + 2] + self.Bool_arr[i + 3] == 0 or self.Bool_arr[i] + \
                    self.Bool_arr[i + 2] + self.Bool_arr[i + 3] == 2:
                self.pb3 = 0
            else:
                self.pb3 = 1
            # Checking if parity bits match expected value, if not, correction will occur
            # Checking first bit
            if self.Bool_arr[i+4] != self.pb1 and self.Bool_arr[i+6] != self.pb3:
                self.decoded_arr.append(1 - self.Bool_arr[i])
            else:
                self.decoded_arr.append(self.Bool_arr[i])
            # Checking second bit
            if self.Bool_arr[i + 4] != self.pb1 and self.Bool_arr[i + 5] != self.pb2:
                self.decoded_arr.append(1 - self.Bool_arr[i+1])
            else:
                self.decoded_arr.append(self.Bool_arr[i+1])
            # Checking third bit
            if self.Bool_arr[i + 5] != self.pb2 and self.Bool_arr[i + 6] != self.pb3:
                self.decoded_arr.append(1 - self.Bool_arr[i+2])
            else:
                self.decoded_arr.append(self.Bool_arr[i+2])
            # Checking forth bit
            if self.Bool_arr[i + 4] != self.pb1 and self.Bool_arr[i + 5] != self.pb2 and self.Bool_arr[i+6] != self.pb3:
                self.decoded_arr.append(1 - self.Bool_arr[i+3])
            else:
                self.decoded_arr.append(self.Bool_arr[i+3])

    def returnArray(self):
        return self.decoded_arr