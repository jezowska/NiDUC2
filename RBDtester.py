import pandas as pd
import BitString as bs
import ParityBitDecoder as pbd
import RepetitionBitCoder as rbc
import ParityBitCoder as pbc
import RepetitionBitDecoder as rbd
import noise


size = 25000
time = 1000
wynik = []
for i in range(time):
    print(i)
    niewykryte = 0
    nienaprawialne = 0
    bledy = 0

    # bazowy ciąg bitów
    bitstring = bs.BitString(size)
    #print("Bez kodowania:")
    #print(bitstring.returnArray())

    #kod powtarzalny
    repetition = rbc.RepetitionBitCoder(bitstring.bool_arr)
    repetition.coding()
    coded_array = repetition.coded_arr
    #print("Potrajanie bitów:")
    #print(repetition.return_array())

    #kod powtarzalny - zaszumiony
    repetition_noised = noise.Noise(coded_array)
    repetition_noised.adding_noise()
    #print("Potrajanie bitów z szumem:")
    #print(repetition_noised.new_array)

    rep_n = rbd.RepetitionBitDecoder(repetition_noised.new_array)
    rep_n.decoding()
    #print("Potrajanie bitów - dekoder:")
    #print(rep_n.return_array())
    indeks = 0
    pom = 0


    for i in range(0, (size * 3), 1):
        pom += 1
        if bitstring.bool_arr[int(i/3)] != repetition_noised.new_array[i]:
           indeks += 1
        if indeks == 3:
            niewykryte += 1

        if indeks > 0 and pom % 3 == 0:
            bledy += 1
            indeks = 0

    for i in range(0, size, 1):
        if(rep_n.decoded_arr[i] != bitstring.bool_arr[i]):
            nienaprawialne += 1
    wynik.append([rep_n.wykryte, nienaprawialne, niewykryte, bledy])

dane = (pd.DataFrame(wynik, columns= ["wykryte", "nienaprawialne", "niewykryte", "bledy"]))
dane.to_csv('Dane_szum01.csv', index=True, sep=';')