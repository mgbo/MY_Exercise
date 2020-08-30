
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--add", nargs="+", help="Creates a local Account")
parser.add_argument("-d", "--delete", nargs="+", help="Delete a local Account")

args = parser.parse_args()

if args.add:
	for u in args.add:
		print ("Creating user " + u)
elif args.delete:
	for u in args.delete:
		print ("delete user " + u)