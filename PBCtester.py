import numpy as np
import random as rd
import BitString as bs
import ParityBitCoder as pbc
import ParityBitDecoder as pbd

def test():
    size = 100000
    bitstring = bs.BitString(size)
    paritybitcoder = pbc.ParityBitCoder(size, bitstring.bool_arr)
    paritybitcoder.Coding()
    print(bitstring.returnArray())
    print(paritybitcoder.returnArray())
    for i in range(int(np.round_(size*1.75))):
        if rd.random() > 0.999:
            paritybitcoder.coded_arr[i] = 1 - paritybitcoder.coded_arr[i]
    print(paritybitcoder.returnArray())
    paritybitdecoder = pbd.ParityBitDecoder(int(np.round_(size*1.75)), paritybitcoder.coded_arr)
    paritybitdecoder.Decoding()
    tester = 0
    print(paritybitdecoder.returnArray())
    for i in range(size-size % 4):
        if paritybitdecoder.decoded_arr[i] == bitstring.bool_arr[i]:
            tester += 1
    print(tester)

test()