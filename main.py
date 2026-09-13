import numpy as np


# Creating the game board
board = np.random.choice((0,1), size=(30, 30), p=[0.7, 0.3])

# Creating a second, temporary board
temp_board = np.zeros_like(board)



print(board)

# dont have much time => must speedcode it in a few hours :O