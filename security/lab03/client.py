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

gen4 = itertools.product([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z],[4])
gen3 = itertools.product("abcdefghijklmnopqrstuvwxyz",[3])
gen2 = itertools.product("abcdefghijklmnopqrstuvwxyz",[2])
gen1 = itertools.product("abcdefghijklmnopqrstuvwxyz",[1])
hashList=[]
for a in range(15):
	r = requests.get(url+'challenges/pwdhash')
	data=r.json()
	hashList.append(data['challenge'])

print hashList

for password in gen4:   
    m4=hashlib.md5()
    digit4=''.join(password[0]+password[1]+password[2]+password[3])
    m4.update(digit4)
    # print digit4
    if "0x"+m4.hexdigest() in hashList:
        print  digit4," matches ", m4.hexdigest()

for password in gen3:  
    m3=hashlib.md5()
    digit3=''.join(password[0]+password[1]+password[2])
    m3.update(digit3)
    if "0x"+m3.hexdigest() in hashList:
        print  digit3," matches ", m3.hexdigest()

for password in gen2: 
    m2=hashlib.md5()
    digit2=''.join(password[0]+password[1])
    m2.update(digit2)
    if "0x"+m2.hexdigest() in hashList:
        print  digit2," matches ", m2.hexdigest()

for password in gen1:                                                     
    m1=hashlib.md5()
    digit1=''.join(password[0])
    m1.update(digit1)
    if "0x"+m1.hexdigest() in hashList:
    	print  digit1," matches ", m1.hexdigest()



# print hashList
# print (hex(97))
# 97-122



# r = requests.get(url+'challenges/pwdhash')
# data=r.json()
# print("Received hash challenge %s"%data['challenge'])