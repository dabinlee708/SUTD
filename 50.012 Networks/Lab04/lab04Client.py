import requests 
import json

def displayResponse(r):
    print 'Header  :',r.headers['content-type'],'\nEncoding:',r.encoding,'\nResponse:',r.json()

def register(base2, base3, x):
    url=base+base2+base3
    for a in range(0,x):
        r = requests.post(url,headers=text)

def checkAvail(base2, base3):
    url=base+base2+base3
    print url
    r=requests.get(url,headers=text)
    print "Updated Available Washers: \n",r.text

base = 'http://127.0.0.1:5000/'

url1 =base+'drier?blk=55&id=2'
json={'content-type':"application/json"}
text={'content-type':"text/plain"}

ra="Available"
response="Available"
for washDry in range(0,2):
    if washDry==0:
        base2='washer?'
    elif washDry==1:
        base2='drier?'
    response='Available'
#     print "washDry", washDry
    for block in range(0,3):
        if block==0:
            base3='blk=55'
        elif block==1:
            base3='blk=57'
        elif block==2:
            base3='blk=59'
        response='Available'
        print "Block", base3[-2:]
        id=0
        while response==ra:
            printout=''
            response=''
#             if washDry==0:
#                 base2='washer?'
#             elif washDry==1:
#                 base2='drier?'
#             if block==0:
#                 base3='blk=55'
#             elif block==1:
#                 base3='blk=57'
#             elif block==2:
#                 base3='blk=59'
            base4='&id='+str(id)
            r=requests.get(base+base2+base3+base4,headers=text)
            if r.status_code==500 or r.status_code==404:
                break
            else:
                response=r.text
            print 'Block',base3[-2:],base2[0:-1],id,'is',response
            id+=1
        x = input("End of block "+base3[-2:]+' '+base2[0:-1]+'. How many machines do you wish to register ?\n')
        register(base2,base3,x)
        checkAvail(base2,base3)