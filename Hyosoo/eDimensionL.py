import requests
import time
from bs4 import BeautifulSoup
from lxml.html import parse

# 2015/12/08 14:49 3DISON Printer (SL1) - Week 13
# Friday, 11 December 2015	9:00am	11:30am	59727
# 							11:30am	2:00pm	59728
# 							2:00pm	4:30pm	59729
# Try to write slotID down every week to learn the pattern

# 2015/12/14 11:54 laser Machine (SL2) - Week 14
# http://edimension2015.sutd.edu.sg/mod/scheduler/view.php?id=35750

# Monday,	14 December 2015 2:00pm	3:00pm 59739
# Wednesday,16 December 2015 12:00pm 1:00pm 59755
# 							 1:00pm 2:00pm 59756
# 							 2:00pm 3:00pm 59757
# 							 3:00pm 4:00pm 59758
# 							 4:00pm 5:00pm 59759
# 							 5:00pm 6:00pm 59760
# Thursday, 	17 December 2015 9:00am 10:00am 59761
# 							 10:00am 11:00am 59762
# 							 11:00am 12:00pm 59763
# 							 12:00pm 1:00pm 59764
# 							 1:00pm 2:00pm 59765
# 							 2:00pm 3:00pm 59766
# 							 3:00pm 4:00pm 59767
# 							 4:00pm 5:00pm 59768
# 							 5:00pm 6:00pm 59769
# Friday,		18 December 2015 10:00am 11:00am 59771
# 							 11:00am 12:00pm 59772
# 							 12:00pm 1:00pm 59773
# 							 1:00pm 2:00pm 59774
# 							 2:00pm 3:00pm 59757
# 							 3:00pm 4:00pm 59776

# 2015/12/14 12:06 3DISON Printer (SL1) - Week 14
# http://edimension.sutd.edu.sg/mod/scheduler/view.php?id=32125




login_IP="http://edimension2015.sutd.edu.sg/login/index.php"
lase1 = "http://edimension2015.sutd.edu.sg/mod/scheduler/view.php?what=savechoice&id="
lase2 = "&slotid="
unbook="http://edimension2015.sutd.edu.sg/mod/scheduler/view.php?id=37018&what=disengage"
log_val =dict(
				username = '1000727',
				password = 'Chwb5278!')
laser_machine =36992
def login():
	s= requests.session()
	while True:
		r = s.post(login_IP, data = log_val)
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
	print lase1+str(slot)+lase2+str(sectionID)
	r = s.get(lase1+str(slot)+lase2+str(sectionID))
	print r.status_code
	html = r.text
	if r.status_code==200:
		print "Booking successful"
	else:
		print "Booking unsuccessful."
		soup = BeautifulSoup(html, 'html.parser')
		print soup.title.string,":", soup.p.string


	
# a = book(login(),35756,59745)
# s= login()
# a=s.get("http://edimension2015.sutd.edu.sg/course/view.php?id=16")
# soup = BeautifulSoup(a.text, 'html.parser')
# print soup.title.string
# # soup.prettify()
# a=soup.find_all('div',{"class":"mod-indent"})
# for b in a:
# 	if "Laser Machine" in b.a.span.text:
# 		print b.a.span.text
# 		return b.a.text

def slot_scanner(s, sectionID):
	print "http://edimension2015.sutd.edu.sg/mod/scheduler/view.php?id="+str(sectionID)
	a = s.get("http://edimension2015.sutd.edu.sg/mod/scheduler/view.php?id="+str(sectionID))	
	soup = BeautifulSoup(a.text, 'html.parser')
	b = soup.find('table', {"class":"generaltabel"}, id='yui_3_5_1_1_1450068325681_1475')
	print b


def section_scanner(s):
	print "Accessing Fab Lab booking page"
	a = s.get("http://edimension2015.sutd.edu.sg/course/view.php?id=16")
	soup = BeautifulSoup(a.text, 'html.parser')
	b = soup.find_all('div',{"class":"mod-indent"})
	for c in b:
		if "Laser Machine" in c.a.span.text:
			print c.a.span.text
			return c.a['href'][-5:]
		else:
			pass

s = login()
# url_laser_section_ID = section_scanner(s)[-5:]
# print url_laser_section_ID
# slot=section_scanner(s)
# print slot
time.ctime()


print section_scanner(s)
# book(s,section_scanner(s),59753)