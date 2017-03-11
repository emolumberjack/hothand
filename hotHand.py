import pandas as pd
import nba_py.player
import nba_py.shotchart
import csv 
import csv_reader 
import checker

# Takes player id as input and produces string output
# NBA player ID's on stats.nba.com
# can be found in url for player's page

def main(playerId):

	playerShots = nba_py.shotchart.ShotChart(playerId)
	print("Scraping... \n")

	playerShots.shot_chart().to_csv(path_or_buf='shotLog.csv')

	completeOutput = ""
	for num in range(0,10):
		x = checker.hotChecker(csv_reader.simplelist[num])
		tupleValues = x.simpleHot()
		gameOutput = "In this game, this player attempted " + str(tupleValues[0]) + " field goals.\n" + "While hot, this player had a " + str(tupleValues[1]) + " field goal completion percentage.\n" +  "While cool, this player had a " + str(tupleValues[2]) + " field goal completion percentage.\n" + "On average, this player had a " + str(tupleValues[3]) + " field goal completion percentage.\n\n\n\n"
		completeOutput += gameOutput

	return completeOutput