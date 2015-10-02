from flask import Flask, url_for, json
app = Flask(__name__)

studentDirectory={0:'dabin',1:'hatib',2:'huihui'}\

washers59=[]
driers59=[]
washers57=[]
driers57=[]
washers55=[]
driers55=[]
washers=[]
driers=[]


for x in range(1,10):
    digit59=str(59.00+x/100.00)
    digit57=str(57.00+x/100.00)
    digit55=str(55.00+x/100.00)
    washers59.append("W"+digit59)
    driers59.append("D"+digit59)
    washers57.append("W"+digit57)
    driers57.append("D"+digit57)
    washers55.append("W"+digit55)
    driers55.append("D"+digit55)


twashers=washers55+washers57+washers59
tdriers=driers55+driers57+driers59

driers.append(tdriers)
driers.append(driers55)
driers.append(driers57)
driers.append(driers59)
washers.append(twashers)
washers.append(washers55)
washers.append(washers57)
washers.append(washers59)

NumWashers=len(washers[0])
NumDriers=len(driers[0])
print NumDriers
print NumWashers


@app.route('/')
def api_root():
    return 'Welcome to SUTD Laundry\n'

@app.route('/nwashers')
def api_washers():
    return 'Number of Washers: ' + json.dumps(NumWashers)+'\n'

@app.route('/ndriers')
def api_driers():
    return 'Number of Driers: ' + json.dumps(NumDriers)+'\n'

@app.route('/nwashers/<int:blk>')
def api_washer(blk):
    return 'Number of Washers:'

@app.route('/ndriers/<int:blk>')
def api_drier(blk):
    if blk==55:
        ind=1
    elif blk==57:
        ind=2
    elif blk==59:
        ind=3
    else:
        blk="SUTD"
        ind=0
    return 'Number of Driers at '+json.dumps(blk)+' is '+ json.dumps(len(driers[ind]))+'\n'

if __name__ == '__main__':
    app.run()
