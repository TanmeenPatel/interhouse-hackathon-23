#vlr clrka jb! - you found me!

#DPS HACKATHON - NILE HOUSE

import random
import tkinter as tk
window = tk.Tk()
window.geometry("700x500")

FONT = "Helvetica 12"
FONT_BOLD = "Helvetica 13 bold"
HEADING = "Helvetica 20 bold"


def encrypt():
    string = nameEntry.get()
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
    ENCRYPTION = "The encrypted code is {encrypted}".format(encrypted=encrypted)
    ENTER = "\n"
    KEY = "Your key to decrypt is {key}".format(key = key)
    textarea = tk.Text(master = window, height = 5, width = 40, padx = 10)
    textarea.grid(column = 0, row = 6)
    textarea.insert(tk.END, ENCRYPTION)
    textarea.insert(tk.END, ENTER)
    textarea.insert(tk.END, KEY)
        
def decrypt():
    encrypted = nameEntry.get()
    key = keyEntry.get()
    decrypted = ""
    ord = ""
    if key[2].isdigit():
        randkey = int(key[2])
    else:
        randkey = int(key[3])
    print("randkey",randkey)
    for i in encrypted:
        if i.isdigit():
            ord += i
        elif i.isalpha():
            ord = int(ord)
            decrypted += chr(ord-randkey)
            ord = ""
    ANSWER = "Decrypted code is {decrypted}".format(decrypted=decrypted)
    textarea = tk.Text(master = window, height = 5, width = 40, padx = 10)
    textarea.grid(column = 0, row = 6)
    textarea.insert(tk.END, ANSWER)

lable1 = tk.Label(text="Welcome", font=HEADING, pady=10, width = 20, height=1).grid(row=0, column = 0)

name = tk.Label(text = "Enter string/encrypted text: ", font = FONT_BOLD, pady = 20)
name.grid(column = 0, row = 1)

nameEntry = tk.Entry()
nameEntry.grid(column = 1, row = 1)

key = tk.Label(text = "Enter key if you wish to decrypt:", font = FONT_BOLD, pady = 10)
key.grid(column = 0, row = 2)

keyEntry = tk.Entry()
keyEntry.grid(column = 1, row = 2)

button = tk.Button(window, text="Encrypt", command = encrypt, bg="pink").grid(column = 1, row = 4)
button = tk.Button(window, text="Decrypt", command = decrypt, bg="#bbb2e9").grid(column = 2, row = 4)

result = tk.Label(text = "Result: ",font = FONT_BOLD, pady = 20)
result.grid(column = 0, row = 4)

window.mainloop()