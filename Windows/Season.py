#Possibly create an array of every match
#Declare the winner without playoffs based off of points

from Match import *
from League import *

class Season: 
	def __init__(self):
		self.matches = [] #array of every match (2,460 matches)
		self.league = []

	def setLeague(self, lg):
		self.league = lg #allow us to sort standings

	def createMatch(self, t1, t2): #somehow create an algorithm that does this randomly
		self.matches.append(Match(t1, t2))
		t1.games = t1.games + 1
		t2.games = t2.games + 1

	def createEveryMatch(self, t1, t2):
		pass #use the canSchedule boolean to schedule games

	def testCreateMatches(self, t1, t2):
		i = 0
		while (i < 82):
			self.matches.append(Match(t1, t2)) #create the match (make a loop to make 82 of them) 0-81
			i = i + 1
		"""
		i = 0
		while (i < len(matches)):
			matches[i].run() #make a run function without printing the scores
		"""
		#add the game to the 2 team's schedule.

	def runSeason(self):
		i = 0
		while (i < len(matches)): #run every match
			self.matches[i].runWithoutScore()
			i = i + 1
		#run all of the games / set the standings

	def testGames(self, t1, t2):
		i = 0
		while (i < 82):
			self.matches[i].runWithoutScore()
			i = i + 1
		print(t1.name + "' wins " + str(t1.wins))
		print(t2.name + "' wins " + str(t2.wins))
		#We can simulate a season using only two teams here

	def displayStandings(self):
		pass #sort the teams based on points
