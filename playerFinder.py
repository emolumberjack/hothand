import nba_py.player
import pandas
'''
convertNameString( userString ):


playerSearch( playerList, userString ):
	parameters: 
		playerList: DataFrame object containing player's ids, name in (Last, First) and (First Last) forms, etc.
		userString: input string from user. Compared to names in playerList to determine if it is a substring

	output:
		returns a tuple containing two lists: a list of possible player names in (First Last) format and a list of those possible player's IDs
'''

def convertNameString( userString ):
	'''
	given a user's search string, convert into something that
	can be compared to an element of PlayerList().info()
	'''
	return userString



def playerSearch( playerList, userString ):
	'''
	given a string that can be compared to an element of PlayerList().info(),
	return associated playerId
	'''
	nameString = convertNameString(userString)
	playerId = 0
	possiblePlayers = []
	possiblePlayerIds = []

	# loop through all rows of display_first_last and collect a list of possible players
	for index in range(0, playerList.shape[0] - 1):
		#if namestring is a substring of this player's name
		if nameString in playerList.get_value(index, "DISPLAY_FIRST_LAST" ):
			
			# add this player to the list of possible players			
			possiblePlayers.append( playerList.get_value(index, "DISPLAY_FIRST_LAST") )

			# add this player's id to the list of possible player ids
			playerId = playerList.get_value(index, "PERSON_ID")
			possiblePlayerIds.append( playerId )

	return possiblePlayers, possiblePlayerIds
