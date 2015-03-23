
class State(object):
	def __init__(self, turn, board):
		self.turn = turn
		self.board = board
	
state = State('o', (None for _ in range(9)))

