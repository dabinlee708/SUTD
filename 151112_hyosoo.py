a=0
b=0
nu=7
nv=7
u=1.0/(nu-1)
v=1.0/(nv-1)
print "Value of a =",a
points=[]
row=[]
col=[]
print "list created"

for a in range (0,nu):
	point_list_col=[]
	print a,"point_list_col created"
	du=a*u
	print a, "du=",du
	
	for b in range (0,nv):

		val1=b*v
		print a,b,"val1",val1,"b",b,"v",v
		tup1=(du,val1)
		print a,b,"tup1",tup1
		point_list_col.append(tup1)
		# print "point_list_col",point_list_col

	print"tup1",tup1
	col.append(tup1)
	print "col",col
print "col",col		
print "row",row
