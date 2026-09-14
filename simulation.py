import numpy as np
import cv2



def game_of_life_simulation(generations, delay):

    # Creating two booleans to check whether to pause the simulation or not
    paused = False
    

    # Initializing an index for the while loop
    i = 0

    # Creating the game board
    board = np.random.choice((0,1), size=(800, 800), p=[0.7, 0.3]).astype(np.uint8)


    while i <= generations:
          if not paused and i <= generations:
              
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
              
              # Updating the actual game board
              board = np.copy(temp_board)
              
              # Creating a board version compatible with cv2-color logic 
              display_board = board * 255
              
              # Showing the evolution
              display_board = cv2.resize(display_board, dsize=(1600, 1600), interpolation=cv2.INTER_NEAREST)
              
              cv2.imshow("The Game of Life", display_board)
              
              # Waiting delay-ms for UX reasons and also providing the possibility of stopping or pausing the game
              key = cv2.waitKey(delay) & 0xFF

              i += 1
                                   
              if key == ord(" "):
                  paused = True
              
              if key == ord("q"):
                  break


          if paused and i <= generations:
              cv2.imshow("The Game of Life", display_board)

              # Interpreting the pressed key just once
              key = cv2.waitKey(30) & 0xFF
                            
              if key == ord(" "):
                   paused = False

              if key == ord("q"):
                   break




    # Holding the last state instead of destroying all windows
    while True:
         key = cv2.waitKey(delay) & 0xFF

         if key == ord("q"):
              break

         else:
              cv2.imshow("The Game of Life", display_board)


    # Clean finish
    cv2.destroyAllWindows()
              

  

    