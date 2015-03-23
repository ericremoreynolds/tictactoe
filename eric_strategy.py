cache = {}

def evaluate(state):
	key = (state.turn, state.board)
	if key in cache:
		return cache[key]
	w = state.winner()
	if w == 0:
		ret = (0, None)
	elif w == state.turn:
		ret = (1, None)
	elif w == state.opponent:
		ret = (-1, None)
	else:
		opt_e = -1
		for i, x in enumerate(state.board):
			if x is None:
				e, _ = evaluate(state.play(i))
				e = -e
				if e >= opt_e:
					opt_e = e
					opt_i = i
				if e == 1:
					break
		ret = (opt_e, opt_i)
	cache[key] = ret
	return ret

def eric_strategy(state):
	_, i = evaluate(state)
	return state.play(i)