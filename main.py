

import numpy as np
import BitString as bs
import ParityBitCoder as pbc

def main():
    size = 12
    bitstring = bs.BitString(size)
    print(bitstring.returnArray())
main()