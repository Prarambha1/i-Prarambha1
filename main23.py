import random
import string

chars =  " " + string.punctuation + string.ascii_letters 

chars =  list(chars)
key = chars.copy()
random.shuffle(key)

print(f"chars: {chars}")
print(f"key: {key}")

#encrypt
plain_text = input("Enter the plain text: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Cipher text: {plain_text}")
print(f"encryted message: {cipher_text}")

#decrypt
cipher_text = input("Enter the cipher text: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encryted message: {cipher_text}")
print(f"Cipher text: {plain_text}")
