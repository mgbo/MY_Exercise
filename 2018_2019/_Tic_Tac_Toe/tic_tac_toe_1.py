

# Tic-Tac-Toe w/Board Class
# Part 1: Getting Started

import os

os.system("clear")


class Board():
	def __init__(self):
		self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

	def display(self):
		print ("{} | {} | {}".format(self.cells[0], self.cells[1], self.cells[2]))
		print ("___________")
		print ("{} | {} | {}".format(self.cells[3], self.cells[4], self.cells[5]))
		print ("___________")
		print ("{} | {} | {}".format(self.cells[6], self.cells[7], self.cells[8]))


board = Board()
board.display()