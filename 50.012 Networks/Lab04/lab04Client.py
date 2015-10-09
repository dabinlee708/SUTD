import requests

r=requests.get('http://127.0.0.1:5000/drier?blk=55')
print r.status_code