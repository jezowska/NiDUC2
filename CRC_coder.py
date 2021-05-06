import numpy as np
import BitString as bs

class CRCstring(object):

    def split_string(arr): # podzial ciagu bitów na 4-bitowe fragmenty
        arr = [arr[i:i + 4] for i in range (0, len(arr), 4)]
        return arr

    def xor(a, b):  # funckja wykonujaca xor
        
        xor_result = []
   
        for i in range(1, len(b)):
            if  a[i] == b[i]:
                xor_result.append(0)
            else:
                xor_result.append(1)
   
        return xor_result

    def mod2(bit_str, key): # funkcja wykoniujaca dzielenie mod2 (z uzyciem xor)
        key_len=len(key)

        temp = bit_str[0 : key_len]  # dostosowanie wielkosci tablicy do dlugosci klucza

        while key_len < len(bit_str):
            if temp[0] == 1:
                temp = CRCstring.xor(key, temp)    # wykonanie xor na danym bicie i przesuniecie
                temp = np.append(temp, bit_str[key_len])
            else:   # if temp[0] = 1
                listofzeros = [0] * key_len
                temp = CRCstring.xor(listofzeros, temp)  # xor z tablica 0 i przesuniecie
                temp = np.append(temp, bit_str[key_len])
            key_len += 1

        if temp[0] == 1:    # operacje dla ostatnich bitow
            temp = CRCstring.xor(key, temp)
        else:   # if temp[0] = 1
            listofzeros = [0] * key_len
            temp = CRCstring.xor(listofzeros, temp)
            
        return temp

    def encode(data, key): # funkcja kodujaca fragment ciagu
   
        key_len = len(key)
   
        appended_data = np.append(data, list([0]*(key_len-1)))  # dodanie zer do fragmentu
        #print(data)
        #print([0]*(key_len-1))
        #print(appended_data)
        remainder = CRCstring.mod2(appended_data, key)
        remainder = np.array(remainder)
        #print("---")
        #print(remainder)
        codeword = np.append(data, remainder)   # wynik to oryginalny fragment + reszta 
        return codeword

        