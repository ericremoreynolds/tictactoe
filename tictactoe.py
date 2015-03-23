from strategies import human_strategy, random_strategy

X = 'x'
O = 'o'

class State(object):
	winning_combinations = tuple(
		tuple(i for i, x in enumerate(b) if x)
		for b in (
			(1, 1, 1, 0, 0, 0, 0, 0, 0),
			(0, 0, 0, 1, 1, 1, 0, 0, 0),
			(0, 0, 0, 0, 0, 0, 1, 1, 1),
			(1, 0, 0, 0, 1, 0, 0, 0, 1),
			(0, 0, 1, 0, 1, 0, 1, 0, 0),
			(1, 0, 0, 1, 0, 0, 1, 0, 0),
			(0, 1, 0, 0, 1, 0, 0, 1, 0),
			(0, 0, 1, 0, 0, 1, 0, 0, 1),
		)
	)
	
	opponent = {
		X: O,
		O: X
	}

	def __init__(self, turn, board):
		self.turn = turn
		self.board = tuple(board)
		
	def winner(self):
		for indices in State.winning_combinations:
			selection = tuple(self.board[i] for i in indices)
			if selection == (X, X, X):
				return X
			elif selection == (O, O, O):
				return O
		if not any(z is None for z in self.board):
			return 0
		return None
	
	def play(self, i):
		assert self.board[i] is None
		board = list(self.board)
		board[i] = self.turn
		return State(State.opponent[self.turn], board)
		
	def __str__(self):
		s  = "     1   2   3\n"
		s += "   +---+---+---+\n"
		s += " A | %s |\n" % (' | '.join(x or ' ' for x in self.board[0:3]))
		s += "   +---+---+---+\n"
		s += " B | %s |\n" % (' | '.join(x or ' ' for x in self.board[3:6]))
		s += "   +---+---+---+\n"
		s += " C | %s |\n" % (' | '.join(x or ' ' for x in self.board[6:9]))
		s += "   +---+---+---+"
		return s
		
		
strategies = (
	human_strategy,
	random_strategy
)

state = State('o', (None for _ in range(9)))

if __name__ == "__main__":
	import os
	turn = 0
	while True:
		state = strategies[turn % 2](state)
		winner = state.winner()
		if winner is not None:
			os.system("cls")
			print state
			print {
				X: "X won",
				O: "O won",
				0: "Draw"
			}[winner]
			exit()
		turn += 1
		