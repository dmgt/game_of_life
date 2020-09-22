# TODO
# Display an empty board - DONE
# Display a starting board with a mix of x's and o's - DONE
# Calculate the next state
# Print board in sequence

import random

board = [[random.choice('xo') for i in range(12)] for j in range(12)]
for row in board:
  for cell in row:
    print(cell, " ", end='')
  print()


# Set up pairs 
# Modulo operator needed for any +1 cases, to avoid out of indexing
for y in range(12): 
  for x in range(12):
    neighbors = \
      board[y-1][x] +        board[y-1][(x+1) % 12] + \
      board[y][(x+1) % 12] + board[(y+1) % 12][(x+1) % 12] + \
      board[(y+1) % 12][x] + board[(x+1) % 12][x-1] + \
      board[y][x-1] +        board[y-1][x-1]
    aliveNeighbors = neighbors.count('x')

    # If cell is alive

    # If cell is dead 

    print(y, x, board[y][x])


# Encode rules for evolution





# Indicies
#print(board[0][0])
#print(board[4][4])

# How to encode the rules?

# How to step time?


# Potential issue- if too few cells have neighbors to evolve - can wrap board around 
