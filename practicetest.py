# string = input("Enter a string: ")
# key = input("Enter a key: ")

import random
string = "HelLo6jf"

encrypted = ""
key = ""
randomkey = random.randint(1,9)
number = 0
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in string:
    oldord = ord(i)
    neword = oldord + randomkey
    char = str(neword)
    encrypted += char
    encrypted += L[random.randint(0,len(L)-1)]
    number += 1


key = str(len(string)) + L[random.randint(0,len(L)-1)] + str(randomkey) + L[random.randint(0,len(L)-1)] + L[random.randint(0,len(L)-1)]
print("Key",key)
print("Encrypted",encrypted)

decrypted = ""
ord = ""
randkey = int(key[2])
print("randkey",randkey)
for i in encrypted:
    if i.isdigit():
        ord += i
    elif i.isalpha():
        ord = int(ord)
        decrypted += chr(ord-randkey)
        ord = ""
print("Decrypted",decrypted)
        