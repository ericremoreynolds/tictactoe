def human_strategy(state):
	import os
	os.system("cls")
	print str(state)
	while True:
		move = raw_input("Move for %s: " % (state.turn)).upper()
		if len(move) != 2 and move[0] not in "ABC" and move[1] not in "123":
			print "Invalid move"
		else:
			i = "ABC".find(move[0]) * 3 + "123".find(move[1])
			return state.play(i)