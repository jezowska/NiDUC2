import BitString as bs
import RepetitionBitCoder as rbc
import ParityBitCoder as pbc
import RepetitionBitDecoder as rbd
import noise

size = 12
bitstring = bs.BitString(size)
print(bitstring.returnArray())

repetition = rbc.RepetitionBitCoder(bitstring.bool_arr);
repetition.coding();
coded_array = repetition.coded_arr

rep_noised = noise.Noise(coded_array)
rep_noised.adding_noise_inc()

rep_dec = rbd.RepetitionBitDecoder(repetition.coded_arr)
rep_dec.decoding();

rep_n = rbd.RepetitionBitDecoder(rep_noised.new_array)
rep_n.decoding();

parity = pbc.ParityBitCoder(size, bitstring.bool_arr)
parity.Coding();

print("Bez kodowania:")
print(bitstring.bool_arr)

print("Potrajanie bitów:")
print(repetition.return_array())

print("Potrajanie bitów z szumem:")
print(rep_noised.new_array)

print("Potrajanie bitów - dekoder:")
print(rep_dec.return_array())

print("Potrajanie bitów - dekoder z szumem:")
print(rep_n.return_array())

print("Parzystoćś bitów:")
print(parity.returnArray())