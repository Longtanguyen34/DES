from Crypto.Cipher import DES
import os

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def encrypt(plain_text, key):
    des = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted_text = des.encrypt(padded_text.encode('utf-8'))
    return encrypted_text

def decrypt(cipher_text, key):
    des = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    decrypted_text = des.decrypt(cipher_text).decode('utf-8')
    return decrypted_text.strip()