#Possibly create an array of every match
#Declare the winner without playoffs based off of points

from Match import *
from League import *
from Team import *

import os
import sys
from xml.etree import ElementTree
from random import randint

class Season: 
	def __init__(self):
		self.matches = [] #array of every match (2,460 matches)
		self.league = []

	def loadDB(self, name, lg): #file name plus league
		try:
			fileName = name 
			fullPath = os.path.abspath(os.path.join('', fileName))
			dom = ElementTree.parse(fullPath)
			leag = dom.findall('league')
			for l in leag:
				n = l.get('name')
				lg.name = n
			teams = dom.findall('league/team') #check teams
			for t in teams:
				n = t.find('name')
				o = t.find('overall')
				i = t.get('id') #id name/number
				lg.addTeam(Team(n.text, int(o.text), i))
		except FileNotFoundError:
			print(fileName + " does not exist!")

	def menu(self):
		print("--------------------------------------")
		print("1. Run season for a league")
		print("2. Return to menu")
		print("--------------------------------------")
		i = input(">")
		if (i == "1"):
			self.fullSeason()
		elif (i == "2"):
			pass
		else:
			print("'" + i + "' is not a valid option!")

	def findTeamInDB(self, lg, ID):
		i = 0
		while (i < len(lg.teams)):
			if (lg.teams[i].id == ID):
				team = lg.teams[i]
				team.overall = lg.teams[i].overall
				print(team.name)
				print("Overall: " + str(team.overall))
				return team
				break
			i = i + 1

	def twoTeamSeason(self):
		lg = League()
		print("What is the name of your database?")
		n = input(">")
		self.loadDB(n, lg)
		self.setLeague(lg)
		#print(self.league.teams[0].name)
		print("What is the first team's id?")
		fID = input(">")
		fID = fID.lower()
		print("What is the second team's id?")
		sID = input(">")
		sID = sID.lower()
		t1 = self.findTeamInDB(lg, str(fID))
		t2 = self.findTeamInDB(lg, str(sID))
		try:
			self.testCreateMatches(t1, t2)
			self.testGames(t1, t2) #testing it out between two teams
		except AttributeError:
			print("Valid team ID's must be entered")

	def fullSeason(self):
		lg = League()
		print("What is the name of your database?")
		n = input(">")
		self.loadDB(n, lg)
		self.setLeague(lg)
		#print(self.league.name)
		print("--------------------------------------")
		print("1. Run whole season")
		print("2. Return to menu")
		print("--------------------------------------")
		i = input(">")
		if (i == "1"):
			self.createEveryMatch()
			self.runSeason()
		elif (i == "2"):
			pass
		else:
			print("'" + i + "' is not a valid option!")

	def setLeague(self, lg):
		self.league = lg #allow us to sort standings

	def createMatch(self, t1, t2): #somehow create an algorithm that does this randomly
		self.matches.append(Match(t1, t2))
		t1.games = t1.games + 1
		t2.games = t2.games + 1
		t1.lastTeam = t2.name
		t2.lastTeam = t1.name

	def searchLowestGP(self): 
		lowestGP = []
		minimum = self.league.teams[0] #we have a problem here
		for t in self.league.teams:
			if t.games < minimum.games:
				lowestGP = [t]
				minimum = t
			elif t.games == minimum.games:
				lowestGP.append(t)
		return lowestGP

	def findSecondTeam(self, firstTeam): #pick from every team, but the team we pass
		mins = self.searchLowestGP()
		while (True): 
			t2num = randint(0, len(mins)-1)
			print(mins[t2num] != firstTeam)
			if (mins[t2num] != firstTeam):
				return mins[t2num]

	def createEveryMatch(self):
		i = 0
		teamTotal = 0
		gs = 0 #games skipped
		while(i < 2460): #makes it more likely to schedule every game
			if (self.league.name == "NHL"):
				t1num = randint(0, 29)
				if (self.league.teams[t1num].games < 82):
					t1 = self.league.teams[t1num]
					self.league.teams[t1num].canSchedule = False
					self.createMatch(t1, self.findSecondTeam(t1))
					#t2num = randint(0, 29)
					#t2num = randint(0, len(self.searchLowestGP()))
					#add in findSecondTeam here
					"""
					if (t2num != t1num and self.league.teams[t2num].games < 82 and self.league.teams[t2num].lastTeam != t1):
						t2 = self.league.teams[t2num];
						self.league.teams[t2num].canSchedule = False
					"""
						
						#print(str(i) + " " + str(t1num) + " " + str(t2num))
					i = i + 1
				else:
					i = i + 1
			elif (self.league.name == "DEL"):
				pass #german league

		for j in self.league.teams:
			if (j.games < 82):
				nextNum = randint(0, 29)
				if (self.league.teams[nextNum].games >= 82):
					nextNum = randint(0, 29)
				while (self.league.teams[nextNum].games >= 82):
					nextNum = randint(0, 29)
				self.createMatch(j, self.league.teams[nextNum])
		for j in self.league.teams:
			teamTotal = teamTotal + j.games
			#print(j.name + " " + str(j.games))

		#print(gs)
		#print(teamTotal)

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
		while (i < len(self.matches)): #run every match
			self.matches[i].runWithoutScore()
			i = i + 1
		self.displayStandings()
		#run all of the games / set the standings

	def testGames(self, t1, t2):
		i = 0
		while (i < 82):
			self.matches[i].runWithoutScore()
			i = i + 1
		print(t1.name + "' wins " + str(t1.wins) + " points " + str(t1.points))
		print(t2.name + "' wins " + str(t2.wins) + " points " + str(t2.points))
		#We can simulate a season using only two teams here

	def displayStandings(self): #sort standings here
		self.league.teams.sort(key=lambda x: x.points, reverse=True)
		for t in self.league.teams:
			print("-------------------")
			print(t.name + " | GP: " + str(t.games) + " | wins: " + str(t.wins) + " | losses: " + str(t.losses) + " | points: " + str(t.points) + " |")
