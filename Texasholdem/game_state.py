# The game state will keep necessary information about the 
# state of the game, passing this object between classes and methods

class Game_State:
	
	def __init__(self, table, players, finished):
		self.table = table
		self.players = players
		self.finished = finished
		self.small_blind = 0
		self.big_blind = 0
		
	
