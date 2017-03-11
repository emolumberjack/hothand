import pandas as pd
import nba_py.player
import nba_py.shotchart
import csv 
import csv_reader 
import checker


# Ask user which player they would like to scrape and calculate
# hothandedness for

# refers to NBA player's id on stats.nba.com
# can be found in url for player's page

def main(playerId):

	playerShots = nba_py.shotchart.ShotChart(playerId)
	print("Scraping... \n")

	playerShots.shot_chart().to_csv(path_or_buf='shotLog.csv')

	for num in range(0,10):
		print(num)
		x = checker.hotChecker(csv_reader.simplelist[num])
		x.simpleHot()
		print("\n \n \n \n")
