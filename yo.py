#! /usr/bin/env python
import random
import itertools

x = 'ABCDEFGHIJ'
y = range(1, 11)

moves = list(itertools.product(x, y))
random.shuffle(moves)

while moves:
    move = moves.pop()
    print(move)
    input()
