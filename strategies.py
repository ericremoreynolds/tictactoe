def human_strategy(state):
	import os
	os.system("cls")
	print str(state)
	while True:
		move = raw_input("Move for %s: " % (state.turn)).upper()
		if len(move) != 2 or move[0] not in "ABC" or move[1] not in "123":
			print "Invalid move"
		else:
			i = "ABC".find(move[0]) * 3 + "123".find(move[1])
			if state.board[i] is not None:
				print "Invalid move"
			else:
				return state.play(i)
			
def random_strategy(state):
	import random
	free = tuple(i for i, x in enumerate(state.board) if x is None)
	return state.play(free[random.randint(0, len(free)-1)])
