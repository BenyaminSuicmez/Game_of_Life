import numpy as np


# Creating the game board
board = np.random.choice((0,1), size=(30, 30), p=[0.7, 0.3]).astype(np.uint8)


shift1 = np.roll(board, shift = 1, axis=0)
shift2 = np.roll(board, shift = -1, axis=0)
shift3 = np.roll(board, shift = 1, axis=1)
shift4 = np.roll(board, shift = -1, axis=1)
shift5 = np.roll(board, shift = (1, 1), axis=(0, 1))
shift6 = np.roll(board, shift = (1, -1), axis=(0, 1))
shift7 = np.roll(board, shift = (-1, -1), axis=(0, 1))
shift8 = np.roll(board, shift = (-1, 1), axis=(0, 1))

neighbors = (shift1 + shift2 + shift3 + shift4 + shift5 + shift6 + shift7 + shift8)


# Rule 1: Cell lives AND has 2 or 3 neighbors
survives = (board == 1) & ((neighbors == 2) | (neighbors == 3))

# Rule 2: Cell is dead AND has exactly 3 neighbors
born = (board == 0) & (neighbors == 3)

# Creating the temporary board
temp_board = (survives | born).astype(np.uint8)

