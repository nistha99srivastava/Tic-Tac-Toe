board = ["-", "-", "-",
         "-", "-", "-",
          "-", "-", "-"]
#---- Global variables----

#game board
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

#if game is still going
game_still_going = True

#Who won? Tie?
winner = None

#Who's turn is it?
current_player = "X"

#play a game of tic tac toe
def play_game():

  #display initial board
  display_board()

  #while the game is still going
  while game_still_going:

    #handle turn of the single player
    handle_turn(current_player)

    #check whether game still on
    check_if_game_over()

    #flip to other player
    flip_player()

  #if game has ended
  if winner =="X" or winner == "O":
    print(winner + " won!")
  elif winner == None:
    print("Its a tie!")

#handle the tirn of the current player
def handle_turn(player):
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")
  #checking for invalid input.
  while position not in ["1","2","3","4","5","6","7","8","9"]:
    position = input("Invalid input.Choose a position from 1-9: ")
  #checking for invalid position (in case pre-occupied)
  while board[int(position)-1] != "-":
     position = input("Position already occupied.Choose another position from 1-9: ")
  position = int(position) - 1
  board[position] = player
  display_board()


def check_if_game_over():
  check_for_winner()
  check_if_tie()


def check_for_winner():
  global winner #required if want to write to a #global variable.
  #check rows
  row_winner = check_rows()
  #check columns
  coulum_winner = check_coulumns()
  #check diagonals
  diagonal_winner = check_diagonals()
  
  if row_winner:
    winner = row_winner
  elif coulum_winner:
    winner = coulum_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return 

def check_rows():
  #set up global variables
  global game_still_going
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-" #row_1 ,2,3 will have true/false Value
  if row_1 or row_2 or row_3:
    game_still_going = False
  # to check who won.
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return

def check_coulumns():
  #set up global variables
  global game_still_going
  col_1 = board[0] == board[3] == board[6] != "-"
  col_2 = board[1] == board[4] == board[7] != "-"
  col_3 = board[2] == board[5] == board[8] != "-" #row_1 ,2,3 will have true/false Value
  if col_1 or col_2 or col_3:
    game_still_going = False
  # to check who won.
  if col_1:
    return board[0]
  elif col_2:
    return board[1]
  elif col_3:
    return board[2]
  return

def check_diagonals():
  #set up global variables
  global game_still_going
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  if diagonal_1 or diagonal_2 :
    game_still_going = False
  # to check who won.
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  return
  
def check_if_tie():
  global game_still_going
  #check if board full
  if "-" not in board:
    game_still_going = False
  return

def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
  return 


play_game()















#overview of the game (functions needed).
#board
#display board
#play game
#handle turn
#check Win
  #check rows
  #check columns
  #check diagonals
#check Tie
#flip player

