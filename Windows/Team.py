class Team:
	def __init__(self, n="", o=0, ID=""):
		self.name = n
		self.id = ID
		self.overall = o
		self.modifier = 0
		self.games = 0
		self.goals = 0
		self.shots = 0
		self.wins = 0
		self.losses = 0
		self.points = 0
		self.goalDif = 0
		self.didWin = False
		self.canSchedule = True
		self.isInOT = False
		self.hasOTL = False
		self.roster = [] #work on this after a general league is created
		self.total = 0 #total of the roster players' overall ratings
		self.lastTeam = ""

		#self.schedule = [] #list of matches
		#Don't use this, as this screws up organization
		self.standingsSpot = 0 #where they are in the standings

	def addPlayer(self, p): #adds player to roster
		self.roster.append(p)

	def addWin(self):
		self.wins = self.wins + 1
		self.points = self.points + 2
	def addLoss(self):
		self.losses  = self.losses + 1
	def addOTL(self): #Work on this later
		self.points = self.points + 1

	def printRoster(self):
		for p in self.roster:
			print(p.name + ", overall:", str(p.overall))

	#add players that have overall ratings
	def calcOverall(self): #average out the overall of all of the players
		for p in self.roster:
			self.total = self.total + p.overall
		self.overall = self.total / len(self.roster)

	def printOverall(self):
		print(self.name + "'s overall: " + str(self.overall))

	def setSchedule(self): #Might not use this
		pass
