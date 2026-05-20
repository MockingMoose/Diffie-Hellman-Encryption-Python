import streamlit as st
import math 
import random 

st.title("Diffie-Hellman Visualization")

pubPrime = 17
pubBase = 3
sendKey = 4
receiveKey = 15
sendPub = generate_public_key(pubBase, pubPrime, sendKey)
receivePub = generate_public_key(pubBase, pubPrime, receiveKey)

##Generates a public key 
def generate_public_key(base, prime, secret):
    return pow(base, secret, prime)

##Generates shared secret key
def generate_shared_key(public, prime, secret):
    return pow(public, secret, prime)


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

print(generate_public_key(pubBase, pubPrime, sendKey))
print(generate_shared_key(pubBase, pubPrime, receiveKey))
