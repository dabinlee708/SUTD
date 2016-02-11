#Dabin Lee
#1000727

import requests
import json
import operator

# # Part 1: Brute Force Attack
# # ------------------------start-of-part-1-----------------
def shifter(encodedstring,key):
    outputString=""
    for a in encodedstring:
        outputString+=chr((ord(a)+key)%256)
    return outputString
url="http://scy-phy.net:8080/"
headers={'Content-Type':'application/json'}
r=requests.get(url+'challenges/caesar')
data=r.json()
# print("Obtained challenge (in hex): %s"%data['challenge'])

m = data['challenge'].replace("0x","").decode("hex")
for i in range (0,255):
	m=shifter(m,1)
	try:
		payload={'cookie':data['cookie'],'solution':m}
		r = requests.post(url+'solutions/caesar', headers=headers,data=json.dumps(payload))
		# print r.status_code
		if r.text=="Your answer is correct... of course!\n":
			print "part 1:", r.text
			break
		else:
			pass
	except:
		pass

# # Decrypted text
# # 235  Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice 'without pictures or conversations?'
# # So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.
# # There was nothing so very remarkable in that; nor did Alice think it so very much out of the way to hear the Rabbit say to itself, 'Oh dear! Oh dear! I shall be late!' (when she thought it over afterwards, it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural); but when the Rabbit actually took a watch out of its waistcoat-pocket, and looked at it, and
# # -------------------------end-of-part-1--------------------


# # Part 2: Frequency Analysis
# # --------------------------start-of-part-2-----------------
url="http://scy-phy.net:8080/"
headers={'Content-Type':'application/json'}
try:
	fout = open("part2_cookie")
	finp = open("part2_encryp")
	cookie=fout.read()
	m=finp.read()
except:
	print ("Calling the API now...")
	r=requests.get(url+'challenges/substitution')
	data=r.json()
	cookie=data['cookie']
	# print("Obtained challenge (in hex): %s"%data['challenge'])
	m = data['challenge'].replace("0x","")
	fout = open("part2_cookie",'w')
	finp = open("part2_encryp",'w')
	fout.write(cookie)
	finp.write(m)

m= open("part2_encryp").read()
cookie = open("part2_cookie").read()
parseList=[m[i:i+2] for i in range(0, len(m), 2)]
frequencyDictionary={}

for a in parseList:
	if a in frequencyDictionary:
		frequencyDictionary[a]+=1
	else:
		frequencyDictionary[a]=1
frequencyList=sorted(frequencyDictionary.items(), key=lambda x: (-x[1], x[0]))
translationList=[' ', 'e', 't', 'a', 'n', 'h', 'o', 'r', 's', 'd', 'i','l','g','w','p','u','c','m','f',',','b','k','y','.','v',';',"'","j",':']
translationDictionary={}
for a in frequencyList:
	translationDictionary[a[0][0:3]]=translationList[frequencyList.index(a)]
DecryptedString=""
for a in parseList:
	# print translationDictionary[a]
	DecryptedString+=translationDictionary[a]

# print DecryptedString
payload={'cookie':cookie,'solution':DecryptedString} 		
r = requests.post(url+'solutions/substitution', headers=headers,data=json.dumps(payload))
print "part 2:", r.text
# # -----------------------end-of-part-2------------------------------
# part3
url="http://scy-phy.net:8080/"
headers={'Content-Type':'application/json'}
r=requests.get(url+'challenges/otp')
data=r.json()
encrypted_data=data['challenge']
# print encrypted_data, len(encrypted_data), len("Submitted student ID: 1000727 and grade 4.")
alteredText = encrypted_data[:24]+hex(int(encrypted_data[24:38],16)^0x01000000000000^0x01000000070207)[2:-1] +\
      encrypted_data[38:50]+hex(int(encrypted_data[50:52],16)^0x00^0x04)[2:]+encrypted_data[52:]
# Figure out which ones to XOR by trying out different digits

payload={'cookie':data['cookie'],'solution':alteredText}
r = requests.post(url+'solutions/otp', headers=headers,data=json.dumps(payload))
print "Part 3:",r.text