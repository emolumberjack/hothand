import pandas as pd
import nba_py.player
import nba_py.shotchart
import csv 
''' with open('curry.csv', 'w', newline='') as fp:
	a = csv.writer(fp, delimiter=',')

	

	a.writerows(curryShots.shot_chart())
'''

# Ask user which player they would like to scrape and calculate
# hothandedness for

# refers to NBA player's id on stats.nba.com
# can be found in url for player's page
playerId = 201939

curryShots = nba_py.shotchart.ShotChart(201939)

curryShots.shot_chart().to_csv(path_or_buf='curryshots.csv')

