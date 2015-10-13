from flask import Flask, url_for, json, request, Response, jsonify
from functools import wraps
app = Flask(__name__)


# Create machines class to define machien objects
class machines:
	def __init__(self, blk, state, number):
		self.blk=blk
		self.state=state
		self.number=number

	def displayState(self):
		return self.state

	def displayBlk(self):
		return self.blk

	def displayNumber(self):
		return self.number

	def updateState(self, updatedState):
		self.state = updatedState

# machines_wash inherites machines		
class machine_wash(machines):
	def __init__(self, blk, state, number):
		self.blk=blk
		self.state=state
		self.number=number
# machines_dry inherites machines
class machine_dry(machines):
	def __init__(self, blk, state, number):
		self.blk=blk
		self.state=state
		self.number=number

# make dictionaries of washers and driers
washer55={}
washer57={}
washer59={}
drier55={}
drier57={}
drier59={}

# put each block's washers and driers in dictionary washer
washer={55:washer55, 57:washer57,59:washer59}
drier={55:drier55, 57:drier57, 59:drier59}

# some string values to be reused
dry='drier'
wash='washer'

# definition to register new machines
def addMachine(type, blk, id, state="Available"):
	if type =="drier":
		tempDrier  = machine_dry(blk, state, id)
		drier[blk][id]=tempDrier
		return "Drier "+str(id)+" in block "+str(blk)+" was successfully added."
	elif type == "washer":
		tempWasher = machine_wash(blk, state, id)
		washer[blk][id]=tempWasher
		return "Washer "+str(id)+" in block "+str(blk)+" was successfully added."
	else:
		return "Invalid machine type. Only 'drier' and 'washer' are allowed"

def deleteMachine(type, blk, id):
	if type =="drier":
		try:
			del drier[blk][id]
			return "Drier "+str(id)+" in block "+str(blK)+" was successfully deleted."
		except:
			return "Invalid block and machine ID."
	elif type == "washer":
		try:
			del washer[blk][id]
			return "Washer "+str(id)+" in block "+str(blK)+" was successfully deleted."
		except:
			return "Invalid block and machine ID."
	else:
		return "Invalid block and machine ID"

def changeMachine(type, blk, id, state):
	if type =="drier":
		try:
			drier[blk][id].updateState(state)
			return "Drier "+str(id)+" in block "+str(blK)+" was successfully added." 
		except:
			return "Invalid block and machine ID."
	elif type == "washer":
		try:
			washer[blk][id].updateState(state)
			return "Washer "+str(id)+" in block "+str(blK)+" was successfully added." 
		except:
			return "Invalid block and machine ID."
	else:
		return "Invalid machine type. Only 'drier' and 'washer' are allowed"	
def checkMachine(type, blk, id):
	if type =="drier":
		try:
			return drier[blk][id].displayState() 
		except:
			return "Invalid block and machine ID."
	elif type == "washer":
		try:
			return washer[blk][id].displayState() 
		except:
			return "Invalid block and machine ID."
	else:
		return "Invalid machine type. Only 'drier' and 'washer' are allowed"	


def check_auth(username,password):
	userDB={"hatib":0000,"dabin":1111,"huihui":2222}
	return username in userDB.keys() and userDB[username]==password

def authenticate():
    return Response('Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/secret')
@requires_auth
def api_root():
    return 'secret address: 2.703\n'


@app.route('/drier', methods = ['GET','POST','DELETE','PUT'])
def api_drier():
	while True:
		try:
			blk=int(request.args['blk'])
			break;
		except:
			blk=-1
        	break;
        
    while True:
    	try:
    		id = int(request.args['id'])
    	    break;
        except:
            id=-1
            break;
        
    while True:
        try:
            print "While true loop for state"
            state=str(request.args['state'])
            break;
        
        except:
            state="-1"
            break;

    print blk, id, state	
    if blk!=-1: 
	    if id!=-1:
	        if state!=-1:
	            if request.method == 'PUT':
	            	quer = changeMachine(dry,blk, id, state)
	            	if request.headers['Content-Type']=='text/plain':
	                    return quer
	                elif request.headers['Content-Type']=='application/json':
                    	return json.dumps(quer)
	            elif request.method == 'DELETE':
	            	quer=str(deleteMachine(dry, blk, id))
	            	if request.headers['Content-Type']=='text/plain':
                    	return quer
                	elif request.headers['Content-Type']=='application/json':
                    	return json.dumps(quer)
	            elif request.method =='POST':
	            	quer=str(addMachine(dry, blk, id))
	            	if request.headers['Content-Type']=='text/plain':
              	 		return quer
                	elif request.headers['Content-Type']=='application/json':
                    	return json.dumps(quer)
            	elif request.method == 'GET':
            		quer=str(checkMachine(dry,blk,id))
	            	if request.headers['Content-Type']=='text/plain':
              	 		return quer
                	elif request.headers['Content-Type']=='application/json':
                    	return json.dumps(quer)
                else:
        	    	quer='Invalid command'
			        if request.headers['Content-Type']=='text/plain':
			            return quer
			        elif request.headers['Content-Type']=='application/json':
			            return json.dumps(quer) 
        else:
        	if request.method == 'GET':
        		quer=''
        		for e in drier[blk]:
                    quer+=('Drier '+str(blk)+'-'+str(drier[blk][e].displayNumber())+' \n') 
                if request.headers['Content-Type']=='text/plain':
                    return quer
                elif request.headers['Content-Type']=='application/json':
                    return json.dumps(quer)
            else:
            	quer='Invalid command'
                if request.headers['Content-Type']=='text/plain':
                    return quer
                elif request.headers['Content-Type']=='application/json':
                    return json.dumps(quer) 
    else:
    	quer='Invalid command'
        if request.headers['Content-Type']=='text/plain':
            return quer
        elif request.headers['Content-Type']=='application/json':
            return json.dumps(quer) 


if __name__ == '__main__':
    app.run(debug=True)

