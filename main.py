import BitString as bs
import ParityBitDecoder as pbd
import RepetitionBitCoder as rbc
import ParityBitCoder as pbc
import RepetitionBitDecoder as rbd
import noise

size = 12

# bazowy ciąg bitów
bitstring = bs.BitString(size)
print("Bez kodowania:")
print(bitstring.returnArray())

#kod powtarzalny
repetition = rbc.RepetitionBitCoder(bitstring.bool_arr);
repetition.coding();
coded_array = repetition.coded_arr
print("Potrajanie bitów:")
print(repetition.return_array())

#kod powtarzalny - zaszumiony
repetition_noised = noise.Noise(coded_array)
repetition_noised.adding_noise_inc()
print("Potrajanie bitów z szumem:")
print(repetition_noised.new_array)

rep_dec = rbd.RepetitionBitDecoder(repetition.coded_arr)
rep_dec.decoding();
print("Potrajanie bitów - dekoder:")
print(rep_dec.return_array())

rep_n = rbd.RepetitionBitDecoder(repetition_noised.new_array)
rep_n.decoding();
print("Potrajanie bitów - dekoder z szumem:")
print(rep_n.return_array())

#kod kontroli parzystosci
parity = pbc.ParityBitCoder(bitstring.bool_arr)
parity.Coding();
print("Parzystoćś bitów:")
print(parity.returnArray())

parity_noised = noise.Noise(parity.coded_arr)
parity_noised.adding_noise_dec()
print("Parzystoćś bitów z szumem: ")
print(parity_noised.return_array())

parity_decoded = pbd.ParityBitDecoder(parity.coded_arr)
parity_decoded.decoding()
print("Parzystoćś bitów z szumem - zdekodowana: ")
print(parity_decoded.returnArray())

#kod CRC
crc

