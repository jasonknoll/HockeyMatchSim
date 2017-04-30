from Season import *
from Division import *
from Team import *
from Match import *

#eventually add conferences and divisions to make simulations more realistic
#Somehow schedule every match and determine a winner

class League:
	def __init__(self):
		self.name = ""
		self.teams = [] #list of teams
		self.divisions = []
		#self.season = Season() #figure this out later

	def addTeam(self, t):
		self.teams.append(t)

	def listTeams(self):
		for t in  self.teams:
			print(t.name + ", ID: " + t.id + ", overall: " + str(t.overall))
			
	def standings(self):
		print("TEAM | GP | W | L | OTL | PTS")
		#print(self.teams[0].name)

	def scheduleMatch(self, t1, t2):
		self.season.append(Match(t1, t2))

	def scheduleSeason(self):
		pass #Schedule every single match (82 per team)

	def setName(self, n):
		self.name = n

	def season():
		pass