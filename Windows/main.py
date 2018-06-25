#! python3

#Based off of my euro 2016 simulation,
#I'm making a hockey simulator engine
#I could eventually make a league simulation that does an entire season

#CHECKLIST:
#Calculate the winner of a match using user input or parse an xml file /DONE/
#Simulate an entire league (possibly post season too) /DONE/
#Add more details to matches
#Don't use rosters until the general system of simulating a season is working
#Export outputs of league status

global version
version = "0.2.6"



import os
import sys
from xml.etree import ElementTree

from Team import *
from Match import *
from Player import *
from League import *
from Season import *

def noRosterGame(): #The real test match
	t1 = Team("Team 1", 100)
	t2 = Team("Team 2", 0)
	m = Match(t1, t2)
	m.run

def loadDB(name, lg): #file name plus league
	global foundFile
	foundFile = False
	try:
		fileName = name 
		fullPath = os.path.abspath(os.path.join('', fileName))
		dom = ElementTree.parse(fullPath)
		teams = dom.findall('league/team') #check teams
		foundFile = True
		for t in teams:
			n = t.find('name')
			o = t.find('overall')
			i = t.get('id') #id name/number
			try:
				lg.addTeam(Team(n.text, int(o.text), i))
			except AttributeError:
				print("Error loading file")
				foundFile = False
				break
	except FileNotFoundError:
		print(fileName + " does not exist!")
		foundFile = False
		#menu()
		#sys.exit()
def testLeagueTeams(lg):
	i = 0
	while (i < len(lg.teams)):
		print(lg.teams[i].name)
		i = i + 1

def testMatch(t1, t2):
	m = Match(t1, t2)
	m.run()

def findTeamInDB(lg, ID):
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

def testMatchFromDB(): #load from what the player says to load from
	testLG = League()
	t1 = Team()
	t2 = Team()
	print("|Test Match from Database|")
	print("What is the name of your database? (xml)")
	n = input(">")
	loadDB(n, testLG)
	if (foundFile == True):
		print("What is the first team's id?")
		fID = input(">")
		fID = fID.lower()
		#check for team 1 id and then team 2 id
		print("What is the second team's id?")
		sID = input(">")
		sID = sID.lower()
		t1 = findTeamInDB(testLG, str(fID))
		t2 = findTeamInDB(testLG, str(sID))
		try:
			testMatch(t1, t2)
		except AttributeError:
			print("Valid team ID's must be entered")
	else:
		pass

def listTeamsInDB():
	print("What is the name of your database? (xml)")
	lg = League()
	n = input(">")
	loadDB(n, lg)
	if (foundFile == True):
		lg.listTeams()
	else:
		pass

def testMatchMenu():
	print("|Test Match|")
	print("What is the first team's name?")
	t1Name = input(">")
	print("What is their overall rating?")
	t1Ovr = input(">")
	print("What is the second team's name?")
	t2Name = input(">")
	print("What is their overall rating?")
	t2Ovr = input(">")

	t1 = Team(t1Name, int(t1Ovr))
	t2 = Team(t2Name, int(t2Ovr))
	testMatch(t1, t2)

def createLeagueFromDB():
	print("|Sim Season from DB|")
	s = Season()
	s.menu()
	#sim every single game
	#using the season class (or something)

def credits():
	print("Created by Jason Knoll")
	#print("I love hockey. (Just thought you should know that)")

def menu():
	os.system("@echo off")
	os.system("cls")
	os.system("clear") #clears the command line
	while True:
		print("--------------------------------------")
		print("Hockey League Simulation v" + version)
		print("1. Test Match")
		print("2. Test Match from Database")
		print("3. Create League from Database") #must have team name and overall
		print("4. List Teams in League")
		print("5. Exit")
		print("--------------------------------------")
		i = input(">")
		if (i == "1"):
			testMatchMenu()
		elif (i == "2"):
			testMatchFromDB()
		elif (i == "3"):
			createLeagueFromDB()
		elif (i == "4"):
			listTeamsInDB()
		elif (i == "5"):
			print("Exiting...")
			sys.exit()
		elif (i == "menu"):
			menu()
		elif (i == "clear"):
			os.system("cls")
		elif (i == "credits"):
			credits()
		elif (i == "exit" or i == "quit"):
			print("Exiting...")
			sys.exit()
		else:
			print("'" + i + "' is not a valid option!")

menu()

"""
setNHLTeams()
loadDB('nhldb.xml', nhl)
testLeagueTeams(nhl)
"""