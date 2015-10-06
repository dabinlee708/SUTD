from flask import Flask, url_for, json, request, Response, jsonify
from functools import wraps
import ast
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
    
    def changeStateUse(self, newState):
        self.state=newState
        return self.state
        

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

def printList():
    print "Driers : ",drierAvail[00],drierAvail[55],drierAvail[57],drierAvail[59]
    print "Washers: ",washerAvail[00],washerAvail[55],washerAvail[57],washerAvail[59]

def updateAvailable():
    washerAvail[55]=availableMachine(washer[55])
    washerAvail[57]=availableMachine(washer[57])
    washerAvail[59]=availableMachine(washer[59])
    washerAvail[00]=washerAvail[55]+washerAvail[57]+washerAvail[59]
    drierAvail[55]=availableMachine(drier[55])
    drierAvail[57]=availableMachine(drier[57])
    drierAvail[59]=availableMachine(drier[59])
    drierAvail[00]=drierAvail[55]+drierAvail[57]+drierAvail[59]
    printList() 

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
        was=washingMachine(blk,"Available",x)
        dri=dryingMachine(blk,"Available",x)
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


def deregister_Machine(machineType, blk):
    if machineType=='drier':
        
        if drierAvail[blk]<1:
            return -1
        
        else:
            tempNumber = drierAvail[blk] -1
            del drier[blk][(drierAvail[blk]-1)]
            updateAvailable()
            return tempNumber
        
    elif machineType=='washer':
        
        if washerAvail[blk]<1:
            return -1
        else:
            tempNumber = washerAvail[blk] -1
            del washer[blk][(washerAvail[blk]-1)]
            updateAvailable()
            return tempNumber

def register_Machine(machineType, blk):
    
    if machineType=='drier':
        
        tempNumber = drierAvail[blk]
        drier[blk][(drierAvail[blk])]=dryingMachine(blk,False,(drierAvail[blk]))
        updateAvailable()
        return tempNumber
    
    elif machineType=='washer':
        
        tempNumber = washerAvail[blk]
        washer[blk][(washerAvail[blk])]=washingMachine(blk,False,(washerAvail[blk]))
        updateAvailable()
        return tempNumber


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
    




@app.route('/drier', methods = ['GET','POST','DELETE', 'PATCH'])
def api_drier():
# Exception Handling for GET requests without arguments
    while True:
        try:
            blk=int(request.args['blk'])
            break;
        
        except:
            blk=[55,57,59]
            break;
        
    while True:
        try:
            id=int(request.args['id'])
            break;
        
        except:
            id=-1
            break;
        
    while True:
        try:
            state=str(request.args['state'])
            break;
        
        except:
            state=-1
            break;
    print blk, id, state
    if blk==55 or blk==57 or blk==59: 
        
        if id!=-1:
            if state!=-1:
                if request.method == 'PATCH':
                    newState=drier[blk][id].changeStateUse(state)
                    quer="Drier "+str(blk)+"-"+str(id)+" is now set to "+str(newState)
                    if request.headers['Content-Type']=='text/plain':
                        return quer
                    elif request.headers['Content-Type']=='application/json':
                        return json.dumps(quer)  
            else:
                if request.method == 'GET':
                    quer=drier[blk][id].displayState()
                    if request.headers['Content-Type']=='text/plain':
                        return quer
                    elif request.headers['Content-Type']=='application/json':
                        return json.dumps(quer) 
                elif request.method == 'DELETE':
                    quer
  
        else:
            if request.method == 'DELETE':
                number=deregister_Machine('drier', blk)
                quer=''
                
                if number == -1:
                    quer= "ERROR: There is no drier to deregister."
                else:
                    quer= 'Deregistered Drier'+str(number)+' at blk '+str(blk)
                if request.headers['Content-Type']=='text/plain':
                    return quer
                elif request.headers['Content-Type']=='application/json':
                    return json.dumps(quer) 
                
            elif request.method == 'POST':
                quer=''
                number=register_Machine('drier', blk)
                quer='Added Drier '+str(number)+' at blk '+str(blk)
                if request.headers['Content-Type']=='text/plain':
                    return quer
                elif request.headers['Content-Type']=='application/json':
                    return json.dumps(quer)
                
            elif request.method == 'GET':
                quer=''
                for e in drier[blk]:
                    quer+=('Drier '+str(blk)+'-'+str(drier[blk][e].displayNumber())+' \n')    
                if request.headers['Content-Type']=='text/plain':
                    return quer
                elif request.headers['Content-Type']=='application/json':
                    return json.dumps(quer) 
    else:
        quer=''
        for a in blk:
            for e in drier[a]:
                quer+=('Drier '+str(a)+'-'+str(drier[a][e].displayNumber())+' \n')
        if request.headers['Content-Type']=='text/plain':
            return quer
        elif request.headers['Content-Type']=='application/json':
            return json.dumps(quer) 


    
@app.route('/washer', methods = ['GET','POST','DELETE'])
def api_washer():
# Exception Handling for GET requests without arguments
    while True:
        try:
            blk=int(request.args['blk'])
            break;
        
        except:
            blk=[55,57,59]
            break;
        
    while True:
        try:
            id=int(request.args['id'])
            break;
        
        except:
            id=-1
            break;
        
    while True:
        try:
            state=str(request.args['state'])
            break;
        
        except:
            state=-1
            break;
    print blk, id, state
    if blk==55 or blk==57 or blk==59: 
        
        if id!=-1:
            if state!=-1:
                if request.method == 'PATCH':
                    newState=washer[blk][id].changeStateUse(state)
                    quer="Washer "+str(blk)+"-"+str(id)+" is now set to "+str(newState)
                    if request.headers['Content-Type']=='text/plain':
                        return quer
                    elif request.headers['Content-Type']=='application/json':
                        return json.dumps(quer)  
            else:
                if request.method == 'GET':
                    quer=washer[blk][id].displayState()
                    if request.headers['Content-Type']=='text/plain':
                        return quer
                    elif request.headers['Content-Type']=='application/json':
                        return json.dumps(quer) 
                elif request.method == 'DELETE':
                    quer
  
        else:
            if request.method == 'DELETE':
                number=deregister_Machine('washer', blk)
                quer=''
                
                if number == -1:
                    quer= "ERROR: There is no washer to deregister."
                else:
                    quer= 'Deregistered washer'+str(number)+' at blk '+str(blk)
                if request.headers['Content-Type']=='text/plain':
                    return quer
                elif request.headers['Content-Type']=='application/json':
                    return json.dumps(quer) 
                
            elif request.method == 'POST':
                quer=''
                number=register_Machine('washer', blk)
                quer='Added Washer '+str(number)+' at blk '+str(blk)
                if request.headers['Content-Type']=='text/plain':
                    return quer
                elif request.headers['Content-Type']=='application/json':
                    return json.dumps(quer)
                
            elif request.method == 'GET':
                quer=''
                for e in washer[blk]:
                    quer+=('Washer '+str(blk)+'-'+str(washer[blk][e].displayNumber())+' \n')    
                if request.headers['Content-Type']=='text/plain':
                    return quer
                elif request.headers['Content-Type']=='application/json':
                    return json.dumps(quer) 
    else:
        quer=''
        for a in blk:
            for e in washer[a]:
                quer+=('Washer '+str(a)+'-'+str(washer[a][e].displayNumber())+' \n')
        if request.headers['Content-Type']=='text/plain':
            return quer
        elif request.headers['Content-Type']=='application/json':
            return json.dumps(quer) 


if __name__ == '__main__':
    app.run(debug=True)



# curl -H "Content-type: text/plain" -X PATCH http://127.0.0.1:5000/drier?blk=55\&id=9\&state=False
# curl -H "Content-type: text/plain" -X PATCH http://127.0.0.1:5000/dryier?blk=55\&id=9\&state=True
# curl -H "Content-type: text/plain" -X GET http://127.0.0.1:5000/drier?blk=55
# curl -H "Content-type: text/plain" -X GET http://127.0.0.1:5000/drier?blk=55\&id=2
# curl -H "Content-type: text/plain" -X POST http://127.0.0.1:5000/drier?blk=55
# curl -H "Content-type: text/plain" -X DELETE http://127.0.0.1:5000/drier?blk=55
