import hashlib


passwordList=["abcd","efgh","ijkl","mnop","qrst"]

m = hashlib.md5()
m.update("abcd")
print m.hexdigest()


url="http://scy-phy.net:8080/"
headers={'Content-Type':'application/json'}
r = requests.get(url+'solutions/pwdhash')
data=r.json()
