from Team import *
from random import *

class Match:
	def __init__(self, t1, t2):
		self.team1 = t1
		self.team2 = t2

	def calcTeamOverall(self): #use this when preforming multiple matches
		self.team1.calcOverall()
		self.team2.calcOverall()
	def calcModifier(self, t1, t2):
		if (t1.overall > 100):
			t1.overall = 100
		elif (t1.overall < 0):
			t1.overall = 0
		if (t2.overall > 100):
			t2.overall = 100
		elif (t2.overall < 0):
			t2.overall = 0
		t1.modifier = randint(randint(1,1), 15) * t1.overall #adds a random element
		t2.modifier = randint(randint(1,1), 15) * t2.overall
	def calcScore(self, t1, t2):
		t1.score = randint(randint(0,1), randint(4,5))
		t1.shots = randint(20, 32)
		t2.score = randint(randint(0,1), randint(4,5))
		t2.shots = randint(20, 32)
	def checkMod(self, t1, t2): #vapenashion \//\
		if (t1.modifier > t2.modifier and t1.score < t2.score and t1.overall - t2.overall > 7):
			i = 0 #gives any team a chance to claim victory
			while (i < 1):
				t1.score = randint(randint(1,1), randint(4,5))
				t2.score = randint(randint(0,0), 3)
				i = i + 1
		elif (t1.modifier < t2.modifier and t1.score > t2.score and t2.overall - t1.overall > 7):
			i = 0
			while (i < 1):
				t1.score = randint(randint(0,0), 3)
				t2.score = randint(randint(1,1), randint(4,5))
				i = i + 1
	def checkOverall(self, t1, t2):
		if (t1.overall - t2.overall >= 13):
			t1.score = t1.score + 2
			t1.shots = t1.shots + randint(10, 15)
		if (t2.overall - t1.overall >= 13):
			t2.score = t2.score + 2
			t2.shots = t2.shots + randint(10, 15)
	def checkShots(self, t1, t2):
		if (t1.shots <= t1.score):
			t1.shots = t1.shots + 10
		elif (t2.shots <= t2.score):
			t1.shots = t1.shots + 10

	def checkWin(self, t1, t2):
		if (t1.score > t2.score):
			t1.didWin = True
			t1.addWin()
			t1.goals = t1.goals + t1.score
			t2.didWin = False
			t2.goals = t2.goals + t2.score
			
			if (t2.hasOTL == True):
				t2.addOTL()
				t2.hasOTL = False
			else:
				t2.addLoss()
			
		elif (t2.score > t1.score):
			t1.didWin = False
			t1.goals = t1.goals + t1.score
			t2.didWin = True
			t2.addWin()
			t2.goals = t2.goals + t2.score
			
			if (t1.hasOTL == True):
				t1.addOTL()
				t1.hasOTL = False	
			else:
				t1.addLoss()
		else:
			t1.didWin = False
			t2.didWin = False

	def checkOT(self, t1, t2):
		if (t1.didWin == False and t2.didWin == False):
			whoWins = randint(0, 1)
			if (whoWins == 0):
				t1.score = t1.score + 1
				t2.hasOTL = True
			else:
				t2.score = t2.score + 1
				t1.hasOTL = True
			#print("Tie game detected")
			self.checkWin(t1, t2)
	def printWin(self, t1, t2):
		print("-------------")
		if (t1.didWin == True):
			print("{0} won!".format(t1.name))
		elif (t2.didWin == True):
			print("{0} won!".format(t2.name))
	def printScore(self, t1, t2):
		#print(str(t1.points))
		#print(str(t2.points))
		print(t1.name + ": " + str(t1.score) + " goals | " + str(t1.shots) + " shots")
		print(t2.name + ": " + str(t2.score) + " goals | " + str(t2.shots) + " shots")

	def runWithoutScore(self):
		self.calcModifier(self.team1, self.team2)
		self.calcScore(self.team1, self.team2)
		self.checkMod(self.team1, self.team2)
		self.checkOverall(self.team1, self.team2)
		self.checkShots(self.team1, self.team2)
		self.checkWin(self.team1, self.team2)
		self.checkOT(self.team1, self.team2)

	def run(self): #run all of the functions
		self.calcModifier(self.team1, self.team2)
		self.calcScore(self.team1, self.team2)
		self.checkMod(self.team1, self.team2)
		self.checkOverall(self.team1, self.team2)
		self.checkShots(self.team1, self.team2)
		self.checkWin(self.team1, self.team2)
		self.checkOT(self.team1, self.team2)
		self.printWin(self.team1, self.team2)
		self.printScore(self.team1, self.team2)
