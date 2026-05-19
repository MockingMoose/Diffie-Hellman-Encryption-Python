import streamlit as st
import math as math


st.title("Diffie-Hellman Visualization")


secret = "Hello"

##Takes in a message and encrypts it with Caesar Cyper using the shared key
def encrypt(message, key):
    encryptMessage = ''
    for i in range(len(message)):
        charNum = ord(message[i])
        encryptMessage += (chr(charNum + key))
    return encryptMessage



##Takes in an encrypted message and decrypts using Caesar Cyper using the shared key
def decrypt(message, key):
    decryptMessage = ''
    for i in range(len(message)):
        charNum = ord(message[i])
        decryptMessage += (chr(charNum - key))
    return decryptMessage

print(encrypt(secret, 5))
print(decrypt(encrypt(secret, 5), 5))
