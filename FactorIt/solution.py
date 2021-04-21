#!/usr/bin/python3

from Crypto.PublicKey import RSA 
from Crypto.Cipher import PKCS1_OAEP 
from base64 import b64decode 

def decrypt_RSA(private_key_loc, package):
    key = open(private_key_loc, "r").read() 
    rsakey = RSA.importKey(key) 
    rsakey = PKCS1_OAEP.new(rsakey) 
    decrypted = rsakey.decrypt(b64decode(package)) 
    return decrypted

flag = "X9vJweMbxdXeee5CrxxlwAMW+tN5iSufA+CBmdXdk3WkwNTi5e3Mn9e9Dop7TU6YKwYz1XL78XeNPJMh/dxD7D6l/j3IsM786bdKQsKbkSc6Wmylsfl7eF7nEDCTPQTUATLOpMvFrixtHrQRmARS+izX0MoLgibRCPkUzL5K/x8="
print(decrypt_RSA('private.pem', flag))

# output: b'fact0r1ngK3y5'


