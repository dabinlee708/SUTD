import requests






print "Check Block 55 Driers"
r = requests.get(url='http://127.0.0.1:5000/dry?blk=55')
r.text