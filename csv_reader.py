import csv 
import pandas as pd
import numpy as np

df = pd.read_csv('curryshots.csv', index_col = 0)

#Prints all the game id's 



	#Loop
		#When gameid = previousscannedgameid
			#Create a new game array with shots made vs missed
	#Print the number of games

class Game:

	def __init__(self, arg1, arg2):
		self.GAME_ID = arg1
		self.EVENT_TYPE = arg2

	#This needs to create a new object


gameNumPrevious = 0
simplelist = []

for num in range(0,1000):

	gameNum = int(df['GAME_ID'][num])
	gameNumNext = int(df['GAME_ID'][num+1])

	if (gameNum != gameNumPrevious):
		a = []
		a.append(df['EVENT_TYPE'][num]) #Assign previous game number and array of EVENT_TYPE to an object
	
	elif (gameNum == gameNumPrevious):
		a.append(df['EVENT_TYPE'][num])

	if (gameNum != gameNumNext):
		x = Game(gameNum, a)
		simplelist.append(x)

	gameNumPrevious = gameNum

print(simplelist[1].EVENT_TYPE)
print(simplelist[1].GAME_ID)

