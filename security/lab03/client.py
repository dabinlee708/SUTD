#!/usr/bin/env python
# Skeleton code to communicate with challenge server
# Nils, SUTD, 2016

import binascii
import requests
import json
import hashlib
import os
from pprint import pprint
import itertools
from itertools import product
import time
import random



# XOR two strings with each other, return string
def xorString(s1,s2):
    rval = [ord(a) ^ ord(b) for a,b in zip(s1,s2)]
    return ''.join([chr(r) for r in rval])


url="http://scy-phy.net:8080/"
#url="http://localhost:5000/"
headers={'Content-Type':'application/json'}

# # Lab 3 skeleton part
r = requests.get(url+'challenges/otpcrc')
data=r.json()
print("Obtained challenge ciphertext: %s with len %d"%(data['challenge'],len(data['challenge'])))

# translate from hex to ascii range
s = data['challenge'].replace('0x',"")
s = binascii.unhexlify(s)

# we know that the last 32 bit are the CRC checksum
# in ascii, that are 4 characters
encrypted_m=s[:-4]
encrypted_crc=s[-4:]

# apply the masks (these do nothing actually)
# Done with help of Hatib
OriginalString='               000      0       '
Altered_String='               727      4       '
xored_String=xorString(OriginalString, Altered_String)
mask = xored_String
crcmask = "\x00"*(len(encrypted_crc))
magic = 0xFFFFFFFF
crcmask =(binascii.crc32(mask,magic) & magic) ^ magic
crcmask = binascii.unhexlify('%08x'%crcmask)
# to check a failed crc manipulation:
#crcmask = "\x01"*(len(encrypted_crc))

manipulated_encrypted_m = xorString(encrypted_m,mask)
manipulated_encrypted_crc = xorString(encrypted_crc,crcmask)
solution = manipulated_encrypted_m + manipulated_encrypted_crc

# ascii hex encode them
solutionHex = '0x'+''.join(['%02x'%ord(i) for i in solution])

payload = {'cookie':data['cookie'],'solution':solutionHex}
r = requests.post(url+'solutions/otpcrc', headers=headers,data=json.dumps(payload))
print("Obtained response: %s"%r.text)

# Demo of the hash part
# Dabin
# Part 4
# passwordList=["asdd","efgh","ijkl","mnop","qrst"]
# solution="test"
# for a in passwordList:
# 	m=hashlib.md5()
# 	m.update(a)
# 	payload = {'hash':"0x"+m.hexdigest(),'solution':a}
# 	r = requests.post(url+'solutions/pwdhash', headers=headers,data=json.dumps(payload))
# 	print("Obtained response: %s"%r.text)

print "Part 5: MD5 Hash being retrieved from scy-phy.net"
gen4 = itertools.product("abcdefghijklmnopqrstuvwxyz",repeat=4)
hashList=[]
password_list=[]
for a in range(15):
	r = requests.get(url+'challenges/pwdhash')
	data=r.json()
	hashList.append(data['challenge'])

bruteForce_start=time.time()
foundCount=0
for password in gen4:  
    m4=hashlib.md5()
    digit4=''.join(password[0]+password[1]+password[2]+password[3])
    m4.update(digit4)
    if "0x"+m4.hexdigest() in hashList:
        foundCount+=1   
        password_list.append(digit4)
        print  digit4," matches ", m4.hexdigest()
print foundCount," matches were found within "+"--- %s seconds ---"% (time.time()-bruteForce_start)

# # Part 6
filetime=time.time()
try:
    fout = open("hashList"+str(filetime)+".txt")
    hashListFile=fout.read()
except:
    fout = open("hashList.txt",'w')
for a in hashList:
    fout.write(a.replace('0x',"")+'\n')
fout.close()


rainbow_generate_start=time.time()
os.system("./rtgen md5 loweralpha 1 4 0 3800 475254 0")
print "Rainbow table generation took "+"--- %s seconds ---"% (time.time()-rainbow_generate_start)

rainbow_sort_start=time.time()
os.system("./rtsort md5_loweralpha#1-4_0_3800x475254_0.rt")
print "Rainbow table sorting took "+"--- %s seconds ---"% (time.time()-rainbow_sort_start)

rainbow_lookup_start=time.time()
os.system("./rcrack md5_loweralpha#1-4_0_3800x475254_0.rt -l hashList.txt")
print "Rainbow table scanning took "+"--- %s seconds ---"% (time.time()-rainbow_lookup_start)


# fout.close()
# part 7
# salt=chr(random.randint(0,25)+97)
# salted_hash_list=[]
# for a in password_list:
#     a=salt+a
#     m=hashlib.md5()
#     m.update(a)
#     salted_hash_list.append(m.hexdigest())
# fout = open("salted_hash_list.txt",'w')
# for a in salted_hash_list:  
#     fout.write(a.replace('0x',"")+'\n')

# salted_rainbow_generate_start=time.time()
# os.system("./rtgen md5 loweralpha 5 5 0 3800 475254 0")
# print "salted_rainbow table generation took "+"--- %s seconds ---"% (time.time()-salted_rainbow_generate_start)

# salted_rainbow_sort_start=time.time()
# os.system("./rtsort md5_loweralpha#5-5_0_3800x475254_0.rt")
# print "salted_rainbow table sorting took "+"--- %s seconds ---"% (time.time()-salted_rainbow_sort_start)

# salted_rainbow_lookup_start=time.time()
# os.system("./rcrack md5_loweralpha#5-5_0_3800x475254_0.rt -l salted_hash_list.txt")
# print "salted_rainbow table scanning took "+"--- %s seconds ---"% (time.time()-salted_rainbow_lookup_start)
# the code only works on terminal and it took 6.79 seconds to crack all 15 passwords.
# Brute forcing took 1.92 seconds
# Rainbow table generation took 101.55 seconds
# Rainbow table lookup took 6.42 seconds
# Salted rainbow table generation took 106.70 seconds
# Salted rainbow table lookup took 6.92 seconds


