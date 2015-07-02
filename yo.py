#! /usr/bin/env python
import random
import itertools

x = 'ABCDEFGHIJ'
y = range(1, 11)


def showmove(move):
    return '{}{}'.format(x[move[0]], y[move[1]])


def find_adjacents(move):
    result = set()
    xpos, ypos = move
    if xpos > 0:
      result.add((xpos - 1, ypos))
    if ypos > 0:
      result.add((xpos, ypos - 1))
    if xpos < len(x) - 1:
      result.add((xpos + 1, ypos))
    if ypos < len(y) - 1:
      result.add((xpos, ypos + 1))
    return result


moves = list(itertools.product(range(len(x)), range(len(y))))
random.shuffle(moves)
hits = set()

while moves:
    # John's magic woo... this (will be) works, but not even he's sure what it's doing?
    # This will win the game, John guarantees it!
    # Caveat: If the other player wins first, it won't win... I'm not sure this is helpful.
    adjacents = list(set(itertools.chain.from_iterable(find_adjacents(hit) for hit in hits)) &
        set(moves))
    if adjacents:
        move = random.choice(adjacents)
        moves.remove(move)
    else:
        move = moves.pop()
    print(showmove(move))
    while True:
        result = input().lower().strip()
        if result in 'mhs':
            break
    if result == 'h':
        hits.add(move)
    elif result == 's':
        hits.add(move)
    else:
        pass
