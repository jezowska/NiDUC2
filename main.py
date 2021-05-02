import BitString as bs
import RepetitionBitCoder as rbc
import ParityBitCoder as pbc
import RepetitionBitDecoder as rbd

size = 12
bitstring = bs.BitString(size)
print(bitstring.returnArray())

repetition = rbc.RepetitionBitCoder(bitstring.bool_arr);
repetition.coding();

rep_dec = rbd.RepetitionBitDecoder(repetition.coded_arr)
rep_dec.decoding();

parity = pbc.ParityBitCoder(size, bitstring.bool_arr)
parity.Coding();

print("Bez kodowania:")
print(bitstring.bool_arr)

print("Potrajanie bitów:")
print(repetition.return_array())

print("Potrajanie bitów - dekoder:")
print(rep_dec.return_array())

print("Parzystoćś bitów:")
print(parity.returnArray())