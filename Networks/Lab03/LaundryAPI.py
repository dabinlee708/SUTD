from flask import Flask, url_for, json, request, Response, jsonify
from functools import wraps

app = Flask(__name__)


class machines:
    
    machineCount=0
    
    def __init__(self, blk, state, number):
        self.blk=blk
        self.state=state
        self.number=number
        machines.machineCount+=1
    
    
    def displayState(self):
        return self.state
    
        
    def displayBlk(self):
        return self.blk
    
    
    def displayNumber(self):
        return self.number
    
    def changeStateUse(self):
        self.state=True
        automaticUpdate(self)
        
    def automaticUpdate(self):
        thread.sleep(1800)
        self.state=False

class washingMachine(machines):
    
    washerCount=0
    
    def __init__(self, blk, state, number):
        self.blk=blk
        self.state=state
        self.number=number
        washingMachine.washerCount+=1
    
    def totalWasher():
        return washerCount
    
class dryingMachine(machines):

    drierCount=0
    
    def __init__(self, blk, state, number):
        self.blk=blk
        self.state=state
        self.number=number
        dryingMachine.drierCount+=1
        
    def totalDrier():
        return drierCount



def check_auth(username, pw):
    
    return username
    
def availableMachine(machineDic):

    count=0
    for e in machineDic.keys():
        if machineDic[e].displayState()==False:
            count+=1 
    return count


washerAvail={}
drierAvail={}

def updateAvailable():
    washerAvail[55]=availableMachine(washer[55])
    washerAvail[57]=availableMachine(washer[57])
    washerAvail[59]=availableMachine(washer[59])
    washerAvail[00]=washerAvail[55]+washerAvail[57]+washerAvail[59]
    drierAvail[55]=availableMachine(drier[55])
    drierAvail[57]=availableMachine(drier[57])
    drierAvail[59]=availableMachine(drier[59])
    drierAvail[00]=drierAvail[55]+drierAvail[57]+drierAvail[59]

#Initial setup for driers and washers.
#Register each of them to the block using dictionaries.
washer={}
drier={}
washer55={}
washer57={}
washer59={}
drier55={}
drier57={}
drier59={}
tempWashersList=[]
tempDriersList=[]
tempWashersList.append(washer55)
tempWashersList.append(washer57)
tempWashersList.append(washer59)
tempDriersList.append(drier55)
tempDriersList.append(drier57)
tempDriersList.append(drier59)
blk=55
dicIndx=0
while blk<60:
    for x in range(0,10):
        was=washingMachine(blk,False,x)
        dri=dryingMachine(blk,False,x)
        tempWashersList[dicIndx][x]=was
        tempDriersList[dicIndx][x]=dri
    washer[blk]=tempWashersList[dicIndx]
    drier[blk]=tempDriersList[dicIndx]
    blk+=2
    dicIndx+=1
updateAvailable()


UserDB={}
UserDB['hatib']=0511
UserDB['huihui']=0531
UserDB['admin']=1228


def check_auth(username, pw):
    if UserDb[string(username)]==pw:
        return True
    else:
        return False
    
def authenticate():
    message = {'message': "Authenticate."}
    resp = jsonify(message)
    
    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'
    
def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return authenticate()
        
        elif not check_auth(auth.username, auth.password):
            return authenticate()
        
        return f(*args, **kwargs)
    return decorated

@app.route('/')
def api_root():
    return 'Welcome to SUTD Laundry\n'

@app.route('/hello', methods = ['GET'])
def api_hello():
    data = {
            'hello' : 'world',
            'number': 3
            }
    js=json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://127.0.0.1'
    
    return resp
#     if 'name' in request.args:
#         return json.dumps('Hello ' + request.args['name'])
#     else:
#         return json.dumps('Hello anonymous user')



@app.route('/wash')
def api_washers():
    return json.dumps(washerAvail[00])

@app.route('/dry')
def api_driers():
    return json.dumps(drierAvail[00])

@app.route('/wash/<int:blk>')
def api_washer(blk):
    return json.dumps(washerAvail[blk])

@app.route('/dry/<int:blk>')
def api_drier(blk):
    return json.dumps(drierAvail[blk])

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"

# @app.route('/update/<Boolean:newState>')
# def api_update(newState):
#     
    


if __name__ == '__main__':
    app.run()



