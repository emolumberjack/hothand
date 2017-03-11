class hotChecker:
	"""
	Contains methods useful for calculating hothandedness,
	including simpleHot()
	"""

	def __init__(self, logObject):
		# specified game's ID according to stats.nba.com
		self.gameId = logObject.GAME_ID

		# array of 1/0 values indicating a shot's completion
		# 1 = completed, 0 = missed
		self.eventType = logObject.EVENT_TYPE


	def simpleHot(self):
		"""
		Calculates field goal completion percentage (FG%) for three different
		conditions: hot, cold, and average. simpleHot() defines 'hot' as having
		completed the last field goal and 'cold' as missing the last field goal
		"""
		
		# number of shots taken 
		fgAttempted = len(self.eventType)

		# counter for number of completed field goals
		fgSuccess = 0

		# loop through and determine number of field goals completed while hot (hotHandShotsCompleted)
		lastShotCompleted = "false"
		hotHandShotsCompleted = 0

		for shotBool in self.eventType:
			if shotBool == "Made Shot": # if this shot was made,

				fgSuccess = fgSuccess + 1 # increase the completed shots counter by 1

				if lastShotCompleted == "true": # and the last shot was made, aka hot
					hotHandShotsCompleted = hotHandShotsCompleted + 1
					lastShotCompleted = "true"
				else: # and the last shot was missed, aka cool
					lastShotCompleted = "true" 
			else:
				lastShotCompleted = "false"


		# percentage of shots completed while hot
		hotFgPerc = ( hotHandShotsCompleted / fgSuccess ) * 100

		# percentage of shots completed while cool
		coolFgPerc = 100 - hotFgPerc

		# average field goal completion as percentage
		avgFgPerc = ( fgSuccess / fgAttempted) * 100

		gameOutput = " " + str(fgAttempted) + " " + str(hotFgPerc) + " " + str(coolFgPerc) + " " + str(avgFgPerc)
		
		return gameOutput




		


