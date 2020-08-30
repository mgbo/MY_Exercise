# Tic-Tac-Toe w/Board Class
# Part 2:  Making move


import os

os.system("clear")


class Board():
	def __init__(self):
		self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

	def display(self):
		print ("{} | {} | {}".format(self.cells[0], self.cells[1], self.cells[2]))
		print ("__________")
		print ("{} | {} | {}".format(self.cells[3], self.cells[4], self.cells[5]))
		print ("__________")
		print ("{} | {} | {}".format(self.cells[6], self.cells[7], self.cells[8]))

	def update_cell(self, cell_no, player):
		if self.cells[cell_no] == " ":
			self.cells[cell_no] = player

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

	# Get X input
	x_choice = int(input("\nX) Please choose 1-9. >"))

	# Update board
	board.update_cell(x_choice, "X")

	# Refresh screen
	refresh_screen()

	# Get O input
	o_choice = int(input("\nO) Please choose 1-9. >"))

	board.update_cell(o_choice, "O")















