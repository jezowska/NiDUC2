
import BitString as bs
import ParityBitDecoder as pbd
import RepetitionBitCoder as rbc
import ParityBitCoder as pbc
import RepetitionBitDecoder as rbd
import noise

niewykryte = 0
nienaprawialne = 0
bledy = 0

size = 1000

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
pom = 0

for i in range(0, (size * 3), 1):
    pom += 1
    if bitstring.bool_arr[int(i/3)] != repetition_noised.new_array[i]:
           index += 1
    if index == 3:
        niewykryte += 1

    if index > 0 and pom % 3 == 0:
        bledy += 1
        index = 0

print("wykryte")
print(rep_n.wykryte)
print("niewykryte")
print(niewykryte)
print("bledy ")
print(bledy)