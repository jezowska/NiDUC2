import BitString as bs
import ParityBitDecoder as pbd
import RepetitionBitCoder as rbc
import ParityBitCoder as pbc
import RepetitionBitDecoder as rbd
import noise

niewykryte = 0
nienaprawialne = 0
bledy = 0

size = 10

# bazowy ciąg bitów
bitstring = bs.BitString(size)
#print("Bez kodowania:")
print(bitstring.returnArray())

#kod powtarzalny
repetition = rbc.RepetitionBitCoder(bitstring.bool_arr);
repetition.coding();
coded_array = repetition.coded_arr
#print("Potrajanie bitów:")
#print(repetition.return_array())

#kod powtarzalny - zaszumiony
repetition_noised = noise.Noise(coded_array)
repetition_noised.adding_noise()
#print("Potrajanie bitów z szumem:")
print(repetition_noised.new_array)

rep_n = rbd.RepetitionBitDecoder(repetition_noised.new_array)
rep_n.decoding();
#print("Potrajanie bitów - dekoder:")
#print(rep_n.return_array())
index = 0
for i in range(0, size):
    for j in range(0, 3):
        if bitstring.bool_arr[i] != repetition_noised.new_array[i+j]:
           index += 1
        print("-------------------")
        print(bitstring.bool_arr[i])
        print(repetition_noised.new_array[i + j])

    if(index > 0):
        bledy += 1

print(rep_n.wykryte)
print("bledy ")
print(bledy)