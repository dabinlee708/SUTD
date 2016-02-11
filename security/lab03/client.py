#!/usr/bin/env python
# Skeleton code to communicate with challenge server
# Nils, SUTD, 2016

import binascii
import requests
import json
import hashlib
from pprint import pprint
import itertools
from itertools import product
# XOR two strings with each other, return string
def xorString(s1,s2):
    rval = [ord(a) ^ ord(b) for a,b in zip(s1,s2)]
    return ''.join([chr(r) for r in rval])


url="http://scy-phy.net:8080/"
#url="http://localhost:5000/"
headers={'Content-Type':'application/json'}

# # Lab 3 skeleton part
# r = requests.get(url+'challenges/otpcrc')
# data=r.json()
# print("Obtained challenge ciphertext: %s with len %d"%(data['challenge'],len(data['challenge'])))

# # translate from hex to ascii range
# s = data['challenge'].replace('0x',"")
# s = binascii.unhexlify(s)

# # we know that the last 32 bit are the CRC checksum
# # in ascii, that are 4 characters
# encrypted_m=s[:-4]
# encrypted_crc=s[-4:]

# # apply the masks (these do nothing actually)
# mask = "\x00"*(len(encrypted_m))
# crcmask = "\x00"*(len(encrypted_crc))
# # to check a failed crc manipulation:
# #crcmask = "\x01"*(len(encrypted_crc))

# manipulated_encrypted_m = xorString(encrypted_m,mask)
# manipulated_encrypted_crc = xorString(encrypted_crc,crcmask)
# solution = manipulated_encrypted_m + manipulated_encrypted_crc

# # ascii hex encode them
# solutionHex = '0x'+''.join(['%x'%ord(i) for i in solution])

# payload = {'cookie':data['cookie'],'solution':solutionHex}
# r = requests.post(url+'solutions/otpcrc', headers=headers,data=json.dumps(payload))
# print("Obtained response: %s"%r.text)

# Demo of the hash part
# Dabin and Ivan
# Part 4
# passwordList=["asdd","efgh","ijkl","mnop","qrst"]
# solution="test"
# for a in passwordList:
# 	m=hashlib.md5()
# 	m.update(a)
# 	payload = {'hash':"0x"+m.hexdigest(),'solution':a}
# 	r = requests.post(url+'solutions/pwdhash', headers=headers,data=json.dumps(payload))
# 	print("Obtained response: %s"%r.text)

gen4 = itertools.product("abcdefghijklmnopqrstuvwxyz",repeat=4)
hashList=[]
for a in range(15):
	r = requests.get(url+'challenges/pwdhash')
	data=r.json()
	hashList.append(data['challenge'])
foundCount=0
for password in gen4:  
    m4=hashlib.md5()
    digit4=''.join(password[0]+password[1]+password[2]+password[3])
    m4.update(digit4)
    # print digit4
    if "0x"+m4.hexdigest() in hashList:
        foundCount+=1
        print  digit4," matches ", m4.hexdigest()
print foundCount," matches were found!"



# print hashList
# print (hex(97))
# 97-122



# r = requests.get(url+'challenges/pwdhash')
# data=r.json()
# print("Received hash challenge %s"%data['challenge'])