# Tic Tac Toe

A strategy is a function which takes `state` and returns a new state which has been modified with a call to  `state.play(i)`.

For example, the random strategy is implemented like so:

```python
def random_strategy(state):
    import random
    free = tuple(i for i, x in enumerate(state.board) if x is None)
    return state.play(free[random.randint(0, len(free)-1)])
```

The state object has a few useful functions and properties:
* `state.turn` is equal to `'x'` if it's X's turn or `'o'` if it's O's turn
* `state.opponent` is equal to `'o'` if it's X's turn or `'x'` if it's O's turn
* `state.winner()` checks if the board is in terminal state. It returns
    * `'x'` if X has won
    * `'o'` if O has won
    * `0` if the players have drawn
    * `None` otherwise
* `state.board` is a tuple of length 9 containing the three rows in order (containing `'x'`,  `'o'` or `None`)
