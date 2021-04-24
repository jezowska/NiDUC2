import numpy as np
import BitString as bs
import ParityBitCoder as pbc

def test():
    size = 12
    bitstring = bs.BitString(size)
    paritybitcoder = pbc.ParityBitCoder(size, bitstring.bool_arr)
    paritybitcoder.Coding()
    print(bitstring.returnArray())
    print(paritybitcoder.returnArray())
test()