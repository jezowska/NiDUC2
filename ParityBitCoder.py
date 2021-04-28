import numpy as np


class ParityBitCoder(object):

    def __init__(self, size, bool_arr):
        self.Size = np.round_(1.75 * size)
        self.Size = int(self.Size)
        self.coded_arr = []
        self.Bool_arr = bool_arr

    def Coding(self):
        count = 0
        for i in range(0, self.Size, 7):
            if count < (self.Size / 1.75) - 3:
                # Coding bits in a pack of four
                self.coded_arr.append(self.Bool_arr[count])
                self.coded_arr.append(self.Bool_arr[count + 1])
                self.coded_arr.append(self.Bool_arr[count + 2])
                self.coded_arr.append(self.Bool_arr[count + 3])
                # Assigning value to first parity bit
                if self.coded_arr[i] + self.coded_arr[i + 1] + self.coded_arr[i + 3] == 0 or self.coded_arr[i] + \
                        self.coded_arr[i + 1] + self.coded_arr[i + 3] == 2:
                    self.coded_arr.append(0)
                else:
                    self.coded_arr.append(1)
                # Assigning value to second parity bit
                if self.coded_arr[i + 1] + self.coded_arr[i + 2] + self.coded_arr[i + 3] == 0 or self.coded_arr[i + 1] + \
                        self.coded_arr[i + 2] + self.coded_arr[i + 3] == 2:
                    self.coded_arr.append(0)
                else:
                    self.coded_arr.append(1)
                # Assigning value to third parity bit
                if self.coded_arr[i] + self.coded_arr[i + 2] + self.coded_arr[i + 3] == 0 or self.coded_arr[i] + \
                        self.coded_arr[i + 2] + self.coded_arr[i + 3] == 2:
                    self.coded_arr.append(0)
                else:
                    self.coded_arr.append(1)
                count += 4

    def returnArray(self):
        return self.coded_arr

