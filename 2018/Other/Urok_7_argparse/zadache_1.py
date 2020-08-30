
import argparse

def Main():
	parser = argparse.ArgumentParser()

	parser.add_argument('filename', help="enter of needed file ")
	parser.add_argument("output", help="output result to a file",
		action="store_true")
	args = parser.parse_args()

	with open (args.filename) as file:
		for line in file:
			print (line,end='')

			if args.output:
				ff = open("output_1.txt","a")
				print (line+'\n', file=ff)

if __name__ == '__main__': 
	Main()











