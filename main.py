import streamlit as st
import math 
import random 

st.title("Diffie-Hellman Visualization")
primesList = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
#Public Prime and Base
pubPrime = random.choice(primesList)
pubBase = 3

#Private Keys
sendKey = 4
receiveKey = 6

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


#Public Keys
sendPub = generate_public_key(pubBase, pubPrime, sendKey)
receivePub = generate_public_key(pubBase, pubPrime, receiveKey)

#Shared Keys
sendShared = generate_shared_key(receivePub, pubPrime, sendKey)
receiveShared = generate_shared_key(sendPub, pubPrime, receiveKey)




col1, col2, col3 = st.columns(3)

with col1:
    st.header("Sender A (Alice)")
    st.write(f"Private Key: {sendKey}")
    st.write(f"Calculated Public Key: {sendPub}")
with col2:
    st.header("The Public Space")
    st.write(f"Shared Prime (p): {pubPrime}")
    st.write(f"Shared Base (g): {pubBase}")
with col3:
    st.header("Receiver B (Bob)")
    st.write(f"Private Key: {receiveKey}")
    st.write(f"Calculated Public Key: {receivePub}")
st.divider()

st.subheader("Sender A sends a message encrypted with shared key")
secretMessage = encrypt(st.text_input("Enter your message to be encrypted"), sendShared)
st.divider()

st.subheader("Intercepted Data on the Network")
st.write("What the hacker sees:")
st.write(f"Intercepted Message: {secretMessage}")
st.write(f"Intercepted Public Keys: A={sendPub}, B= {receivePub}")

st.divider()

st.subheader("Receiver B gets message and decrypts it using shared key")
st.success(f"Decrypted successfully by Receiver B: {decrypt(secretMessage, receiveShared)}")