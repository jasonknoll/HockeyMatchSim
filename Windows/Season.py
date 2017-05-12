#Possibly create an array of every match
#Declare the winner without playoffs based off of points

from Match import *

class Season: 
	def __init__(self):
		self.matches = [] #array of every match (2,460 matches)

	def createMatch(self, t1, t2):
		i = 0
		while (i < 82):
			self.matches.append(Match(t1, t2)) #create the match (make a loop to make 82 of them) 0-81
		"""
		i = 0
		while (i < len(matches)):
			matches[i].run() #make a run function without printing the scores
		"""
		#add the game to the 2 team's schedule.

	def runSeason(self):
		pass
		#run all of the games / set the standings

	def testGames(self, t1, t2):
		pass
		#We can simulate a season using only two teams here
