class Player:
	def __init__(self, n="", o=0):
		self.name = n
		self.position = ""

		self.overall = o
		self.offense = 0
		self.defense = 0

		self.gamesPlayed = 0
		self.goals = 0
		self.assists = 0
		self.points = self.goals + self.assists
		self.pm = 0 #plus-minus
		#self.ppg = self.points / self.gamesPlayed #points per-game
		#add invdividual overall ratings for specific skills

	def addPm(self): 
		self.pm = self.pm + 1
	def subPm(self):
		self.pm = self.pm - 1
	def addGoal(self):
		self.goals = self.goals + 1
	def addAssist(self):
		self.assists = self.assists + 1
	def addGP(self):
		self.gamesPlayed = self.gamesPlayed + 1

	def calcOffense(self, x): #eventually have it average out all of the other attributes
		self.offense = x
	def calcDefense(self, x):
		self.defense = x
	def calcOverall(self): #for individual skills
		self.overall = (self.offense + self.defense) / 2