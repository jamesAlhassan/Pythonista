#!/usr/bin/python3

from art import logo


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
        "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", 
        "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q",
        "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print(logo)

again = True

while again:
    direction = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n")

    text = input("Type your message: \n").lower()

    shift = int(input("Type your shift number:\n"))

    if shift > 26:
        shift %= 26
    
    def caesar(message, shifts, direction_):
        cipher = ""
        for letter in message:
            if letter in alphabet:
                position = alphabet.index(letter)
                if direction == "encode":
                    cipher += alphabet[position + shifts]
                elif direction == "decode":
                    cipher += alphabet[position - shifts]
                else:
                    print("Unkown Direction Entered\n(Please enter either 'encode' or 'decode'!)")
            else:
                cipher += letter
        print(cipher)
    
    
    caesar(message=text, shifts=shift, direction_=direction)
    
    if_again = input("Type 'yes' if you want to again. Otherwise type 'no'.").lower()
    if if_again == 'no':
        again = False
        print("GOODBYE!!!")
