#Dabin Lee
#1000727

import requests
import json
import operator

# Part 1: Brute Force Attack

# def shifter(encodedstring,key):
#     outputString=""
#     for a in encodedstring:
#         outputString+=chr((ord(a)+key)%256)
#     return outputString

# print ("Calling the API now...")
# url="http://scy-phy.net:8080/"
# headers={'Content-Type':'application/json'}
# r=requests.get(url+'challenges/caesar')
# data=r.json()
# print("Obtained challenge (in hex): %s"%data['challenge'])

# m = data['challenge'].replace("0x","").decode("hex")
# for i in range (0,255):
# 	m=shifter(m,1)
# 	try:
# 		payload={'cookie':data['cookie'],'solution':m}
# 		r = requests.post(url+'solutions/caesar', headers=headers,data=json.dumps(payload))
# 		# print r.status_code
# 		if r.text=="Your answer is correct... of course!\n":
# 			print "Key: ",i+1, r.text
# 		else:
# 			pass
# 	except:
# 		pass

# Decrypted text
# 235  Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice 'without pictures or conversations?'
# So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.
# There was nothing so very remarkable in that; nor did Alice think it so very much out of the way to hear the Rabbit say to itself, 'Oh dear! Oh dear! I shall be late!' (when she thought it over afterwards, it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural); but when the Rabbit actually took a watch out of its waistcoat-pocket, and looked at it, and

# Part 2: Frequency Analysis
print ("Calling the API now...")
url="http://scy-phy.net:8080/"
headers={'Content-Type':'application/json'}
r=requests.get(url+'challenges/substitution')
data=r.json()
print("Obtained challenge (in hex): %s"%data['challenge'])

m = data['challenge'].replace("0x","")
parseList=[m[i:i+2] for i in range(0, len(m), 2)]
# print parseList
frequencyDictionary={}

for a in parseList:
	if a in frequencyDictionary:
		frequencyDictionary[a]+=1
	else:
		frequencyDictionary[a]=1
# print frequencyDictionary

frequencyList=sorted(frequencyDictionary.items(), key=lambda x: (-x[1], x[0]))

print len(frequencyList)

translationList=[' ', 'e', 't', 'a', 'n', 'h', 'o', 'r', 's', 'd', 'i','l','g','w','p','u','c','m','f',',','b','k','y','.','v',';',"'",":",'j']
translationDictionary={}
for a in frequencyList:
	print a
	translationDictionary[a[0][0:3]]=translationList[frequencyList.index(a)]
print translationDictionary


DecryptedString=""
for a in parseList:
	print translationDictionary[a]
	DecryptedString+=translationDictionary[a]

print DecryptedString
