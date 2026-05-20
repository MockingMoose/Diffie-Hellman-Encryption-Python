import streamlit as st
import random 

st.title("Diffie-Hellman Visualization")

## g = base, p = prime
## a = Alice private key, b = Bob private key

##Alice public key: A = g^a mod p
##Bob public key: B = g^b mod p


#Public Prime and Base
primesList = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
pubPrime = random.choice(primesList)
pubBase = 3

#Private Keys
aliceKey = 4
bobKey = 6


##Generates a public key 
def generate_public_key(base, prime, private):
    #Formula: (base ^ private) % prime
    return pow(base, private, prime)

##Generates shared secret key
def generate_shared_key(public, prime, private):
    #Formula: (public ^ private) % prime
    #Each person uses their own private key in combination with
    #  the others public key to arrive at the same number
    return pow(public, private, prime)


##Takes in a message and encrypts it with Caesar Cyper using the shared key
def encrypt(message, key):
    encryptMessage = ''
    for i in range(len(message)):
        charNum = ord(message[i])
        #Shifts character by the value of the shared key
        encryptMessage += (chr(charNum + key))
    return encryptMessage

##Takes in an encrypted message and decrypts using Caesar Cyper using the shared key
def decrypt(message, key):
    decryptMessage = ''
    for i in range(len(message)):
        charNum = ord(message[i])
        #Shifts character by the value of the shared key
        decryptMessage += (chr(charNum - key))
    return decryptMessage


#Public Keys
alicePub = generate_public_key(pubBase, pubPrime, aliceKey)
bobPub = generate_public_key(pubBase, pubPrime, bobKey)

#Shared Keys
aliceShared = generate_shared_key(bobPub, pubPrime, aliceKey)
bobShared = generate_shared_key(alicePub, pubPrime, bobKey)




col1, col2, col3 = st.columns(3)

with col1:
    st.header("Sender (Alice)")
    st.write(f"Private Key: {aliceKey}")
    st.write(f"Calculated Public Key: {alicePub}")
with col2:
    st.header("The Public Space")
    st.write(f"Shared Prime (p): {pubPrime}")
    st.write(f"Shared Base (g): {pubBase}")
with col3:
    st.header("Receiver (Bob)")
    st.write(f"Private Key: {bobKey}")
    st.write(f"Calculated Public Key: {bobPub}")
st.divider()

st.subheader("Alice sends a message encrypted with shared key")
secretMessage = encrypt(st.text_input("Enter your message to be encrypted"), aliceShared)
st.divider()

st.subheader("Intercepted Data on the Network")
st.write("What the hacker sees:")
st.write(f"Intercepted Message: {secretMessage}")
st.write(f"Intercepted Public Keys: Alice={alicePub}, Bob= {bobPub}")
st.divider()

st.subheader("Receiver Bob gets message and decrypts it using shared key")
st.success(f"Decrypted successfully by Bob: {decrypt(secretMessage, bobShared)}")