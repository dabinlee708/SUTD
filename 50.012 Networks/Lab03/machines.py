
class machines:
	
	machineCount=0
	
	def __init__(self, blk, state, number):
		self.blk=blk
		self.state=state
		self.number=number
		machineCount+=1
	
	
	def displayState(self):
		return self.state
	
		
	def displayBlk(self):
		return self.blk
	
	
	def displayNumber(self):
		return self.number
	

class washingMachine(machines):
	
	washerCounter=0
	
	def __init__(self):
		self.blk=blk
		self.state=state
		self.number=number
		washerCount+=1
	
	def totalWasher():
		return washerCounter
	
class dryingMachine(machines):

	drierCounter=0
	
	def __init__(self):
		self.blk=blk
		self.state=state
		self.number=number
		drierCount+=1
		
	def totalDrier(self):
		return drierCounter
	
	