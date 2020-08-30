

# Tic-Tac-Toe w/Board Class
# Part 3: Tie Game


import os

os.system("clear")


class Board():
	def __init__(self):
		self.cells = [" "," ", " ", " ", " ", " ", " ", " ", " ", " "]

	def display(self):
		print ("{} | {} | {}".format(self.cells[1], self.cells[2], self.cells[3]))
		print ("__________")
		print ("{} | {} | {}".format(self.cells[4], self.cells[5], self.cells[6]))
		print ("__________")
		print ("{} | {} | {}".format(self.cells[7], self.cells[8], self.cells[9]))

	def update_cell(self, cell_no, player):
		if self.cells[cell_no] == " ":
			self.cells[cell_no] = player

	def is_winner(self, player):

		if self.cells[1] == player and  self.cells[2] == player and  self.cells[3] == player:
			return True

		if self.cells[4] == player and  self.cells[5] == player and  self.cells[6] == player:
			return True

		if self.cells[7] == player and  self.cells[8] == player and  self.cells[9] == player:
			return True

		if self.cells[1] == player and  self.cells[4] == player and  self.cells[7] == player:
			return True

		if self.cells[2] == player and  self.cells[5] == player and  self.cells[8] == player:
			return True

		if self.cells[3] == player and  self.cells[6] == player and  self.cells[9] == player:
			return True

		if self.cells[1] == player and  self.cells[5] == player and  self.cells[9] == player:
			return True

		if self.cells[3] == player and  self.cells[5] == player and  self.cells[7] == player:
			return True

		return False

	def is_tie(self):
		used_cells = 0

		for cell in self.cells:
			if cell != " ":
				used_cells +=1

		if used_cells == 9:
			return True

		else:
			return False


	def reset(self):
		self.cells = [" "," ", " ", " ", " ", " ", " ", " ", " ", " "]


# -------------------------------------------------

board = Board()

def print_header():
	print ("Welcome to Tic-Tac-Toe\n")

def refresh_screen():
	#clear the screen
	os.system("clear")

	# print the header
	print_header()

	#show the board
	board.display()


while True:
	refresh_screen()

	# --------------------- Для игрок X ------------------------
	# Get X input
	x_choice = int(input("\nX) Please choose 1-9. >"))

	# Update board
	board.update_cell(x_choice, "X")

	# Refresh screen
	refresh_screen()

	# Check for an X win
	if board.is_winner("X"):
		print ("\nX wins!\n")
		play_again = input("Would you like to play again? (N/Y) ").upper()
		
		if play_again == "Y":
			board.reset()
			continue
		else:
			break

	# Check for a tie
	if board.is_tie():
		print ("\nTie game!\n")
		play_again = input("Would you like to play again? (N/Y) ").upper()

		if play_again == "Y":
			board.reset()
			continue
		else:
			break


	# --------------------- Для игрок O ------------------------
	# Get O input
	o_choice = int(input("\nO) Please choose 1-9. >"))

	board.update_cell(o_choice, "O")

	# # Check for an O win
	if board.is_winner("O"):
		print ("\nO wins!\n")
		play_again = input("Would you like to play again? (N/Y) ").upper()

		if play_again == "Y":
			board.reset()
			continue
		else:
			break

	# Check for a tie
	if board.is_tie():
		print ("\nTie game!\n")
		play_again = input("Would you like to play again? (N/Y) ").upper()

		if play_again == "Y":
			board.reset()
			continue
		else:
			break
















