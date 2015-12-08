import requests


# 2015/12/08 14:49 3DISON Printer (SL1) - Week 13
# Friday, 11 December 2015	9:00am	11:30am	59727
# 							11:30am	2:00pm	59728
# 							2:00pm	4:30pm	59729
# Try to write slotID down every week to learn the pattern



login_add = "http://edimension.sutd.edu.sg/login/index.php"
lase1 = "http://edimension.sutd.edu.sg/mod/scheduler/view.php?what=savechoice&id="
lase2 = "&slotid="
unbook="http://edimension.sutd.edu.sg/mod/scheduler/view.php?id=37018&what=disengage"
log_val =dict(
				username = '1000727',
				password = 'Chwb5278!')
def login():
	print "logging into eDimension"
	s= requests.session()
	while True:
		r = s.post(login_add, data = log_val)
		if r.status_code==200:
			print "Log-in successful"
			break;
		else:
			print "Log-in unsuccessful. Trying again"
	return s
def unboook(s):
	print "Initiating unbooking"
	r = s.get()
def book(s,slot,sectionID):
	print "Initiating booking\n",
	print lase1+str(slot)
	r = s.get(lase1+str(slot)+lase2+str(sectionID))
	if r.status_code==200:
		print "Booking successful"
	else:
		print "Booking unsuccessful."
	return r.text
	
a = book(login(),59728,36992)

print a
