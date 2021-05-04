import numpy as np
import BitString as bs


class CRCstring(object):
    def __init__(self, size, bool_arr):
        self.Bool_arr = bool_arr
        self.Split_arr = []

    def split_string(self): # podzial ciagu bitów na 2 bajtowe fragmenty
        self.Split_arr = [self.Bool_arr[i:i + 16] for i in range(0, len(self.Bool_arr), 16)]
        return self.Split_arr

    def xor(a, b):  # funckja wykonujaca xor

        xor_result = []

        for i in range(0, len(b)):
            if a[i] == b[i]:
                xor_result.append(0)
            else:
                xor_result.append(1)

        return xor_result

    def mod2(bit_str, key): # funkcja wykoniujaca dzielenie mod2 (z uzyciem xor)
        key_len = len(key)

        temp = bit_str[1: key_len]  # dostosowanie wielkosci tablicy do dlugosci klucza

        while key_len < len(bit_str):
            if temp[0] == 1:
                temp = CRCstring.xor(list(key), temp) + bit_str[key_len] # wykonanie xor na danym bicie i przesuniecie
            else:
                listofzeros = [0] * len(temp)   
                temp = CRCstring.xor(listofzeros, temp) + bit_str[key_len] # xor z tablica 0 i przesuniecie
            key_len += 1

        if temp[0] == 1: # operacje dla ostatnich bitow
            temp = CRCstring.xor(list(key), temp)
        else:
            listofzeros = [0] * len(temp)
            temp = CRCstring.xor(listofzeros, temp)

        output = temp
        return output

    def decode(data, key):  # funkcja dekodujaca fragment ciagu

        key_len = len(key)

        remainder = CRCstring.mod2(data, key)   # wynik to reszta 

        return remainder
