

import os
os.system("clear")


class Board():

	def __init__(self):
		self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

	def display(self):
		print ("{} | {} | {} ".format(self.cells[1], self.cells[2], self.cells[3]))
		print ("__________")
		print ("{} | {} | {} ".format(self.cells[4], self.cells[5], self.cells[6]))
		print ("__________")
		print ("{} | {} | {} ".format(self.cells[7], self.cells[8], self.cells[9]))

	def update_cells(self, cell_no, player):
		if self.cells[cell_no] == " ":
			self.cells[cell_no] = player

	def check_winner(self, player):
		if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
			return True

		if self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
			return True

		if self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
			return True

		if self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
			return True

		if self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
			return True

		if self.cells[3] == player and self.cells[6] == player and self.cells[9] == player:
			return True

		if self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
			return True

		if self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
			return True

		return False

	def board_reset(self):
		self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

# ------------------------------------------------------------------------

if __name__ == "__main__":
	board = Board()

	def print_header():
		print ("Tic Tac Toe")

	def refrech_screen():
		#clear the screen
		os.system("clear")

		# print the header
		print_header()

		#show the board
		board.display()

	while True:

		refrech_screen()

		# -------------- for X player ------------------
		num_cell = int(input("\nX) please choose number(1-9) of cell : "))

		board.update_cells(num_cell, "X")

		refrech_screen()

		if board.check_winner("X"):
			print ("X is winner")
			play_again = input("Would you like to play again? (N/Y) ").upper()

			if play_again == "Y":
				board.reset()
				continue
			else:
				break


		# ---------------- for O player -----------------
		num_cell = int(input("\nO) please choose number(1-9) of cell : "))

		board.update_cells(num_cell, "O")

		refrech_screen()

		if board.check_winner("O"):
			print ("O is winner")
			play_again = input("Would you like to play again? (N/Y) ").upper()

			if play_again == "Y":
				board.reset()
				continue
			else:
				break
















