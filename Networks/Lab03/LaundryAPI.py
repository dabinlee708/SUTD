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

print drierAvail
print washerAvail


UserDB={}
UserDB['hatib']=0511
UserDB['huihui']=0531
UserDB['admin']=1228


def deregister_Machine(machineType, blk, id):
    if machineType=='drier':
        tempNum=drier[blk][id].displayNumber
        del drier[blk][(drierAvail[blk]-1)]
        updateAvailable()
        return 
    
    elif machineType=='washer':
        del washer[blk][(washerAvail[blk]-1)]
        updateAvailable()

def register_Machine(machineType, blk):
    if machineType=='drier':
        drier[blk][(drierAvail[blk])]=dryingMachine(blk,False,(drierAvail[blk]))
        updateAvailable()
    elif machineType=='washer':
        washer[blk][(washerAvail[blk])]=washingMachine(blk,False,(washerAvail[blk]))
        updateAvailable()


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
    
def requires_auth(f):
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
    
print drier[55][1].displayNumber()

@app.route('/dry', methods = ['GET','PUT','DELETE'])
def api_drier():
    print 3
    blk=int(request.args['blk'])
    print blk, type(blk)
    if blk==55 or blk==57 or blk==59: 
        if request.headers['Content-Type']=='text/plain':  
            if request.method == 'GET':
                availableDrier='Available Driers'
                print type(blk)
                for e in drier[blk]:
                    availableDrier+=('Drier '+str(blk)+'-'+str(drier[blk][e].displayNumber())+'\n')
                return availableDrier
                    
            elif request.method == 'DELETE':
                number=deregister_Machine('drier', blk)
                return 'deregistered a drier'+number+'at blk '+blk
            elif request.method == 'PUT':
                register_Machine('drier', blk)
                return 'Added a new drier'+number+ 'at blk '+blk
            else:
                pass
        
        elif request.headers['Content-Type']=='application/json':
            if request.method == 'GET':
                for e in drier[blk]:
                    availableDrier.append('Drier ',blk,'-',e.displayNumber())
                return json.dumps(availableDrier)
            elif request.method == 'PUT':
                register_Machine('drier', blk)
                retString="Added a new drier at block "+str(blk)
                return json.dumps(retString)
            elif request.method == 'DELETE':
                print drierAvail
                deregister_Machine('drier', blk)
                print blk
                print drierAvail
                deregister_Machine('drier', blk)
                retString="deregistered a drier at block "+str(blk)
                return json.dumps(retString)
            else:
                pass
        else:          
            pass
    else:
        if request.headers['Content-Type']=='text/plain':
            return request.data(drierAvail[00])
        elif request.headers['Content-Type']=='application/json':
            return json.dumps(drierAvail[00])
        else:
            pass
    
@app.route('/wash', methods = ['GET','PUT','DELETE'])
def api_washer():
    indx=0
    blk=00
    if request.data=='{"block":"55"}':
        indx=1
        blk=55
    elif request.data=='{"block":"57"}':
        indx=2
        blk=57
    elif request.data=='{"block":"59"}':
        indx=3
        blk=59
    else:
        pass
    if request.data=='{"block":"55"}' or request.data=='{"block":"57"}' or request.data=='{"block":"59"}': 
        if request.headers['Content-Type']=='text/plain':  
            if request.method == 'GET':
                return washerAvail[indx]
            elif request.method == 'DELETE':
                deregister_Machine('washer', blk)
                return 'deregistered a washer at blk '+blk
            elif request.method == 'PUT':
                register_Machine('washer', blk)
                return 'Added a new washer at blk '+blk
            else:
                pass
        
        elif request.headers['Content-Type']=='application/json':
            if request.method == 'GET':
                return json.dumps(washerAvail[blk])
            elif request.method == 'PUT':
                register_Machine('washer', blk)
                retString="Added a new washer at block "+str(blk)
                return json.dumps(retString)
            elif request.method == 'DELETE':
                deregister_Machine('washer', blk)
                retString="deregistered a washer at block "+str(blk)
                return json.dumps(retString)
            else:
                pass
        else:          
            pass
    else:
        if request.headers['Content-Type']=='text/plain':
            return request.data(washerAvail[00])
        elif request.headers['Content-Type']=='application/json':
            return json.dumps(waherAvail[00])
        else:
            pass


if __name__ == '__main__':
    app.run(debug=True)


# curl -H "Content-type: application/json" -X PUT  http://127.0.0.1:5000/dry -d '{"block":"55"}'



