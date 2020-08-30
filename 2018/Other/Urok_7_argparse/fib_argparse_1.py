
import argparse

def fib(n):
	a,b = 0,1
	for i in range(n):
		a,b = b, a+b
		print ("a :{} and b :{}".format(a,b))
	return a

def Main():
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group()

	parser.add_argument("num", help ="you need to write n ",type=int)
	group.add_argument("-v", "--verbose",action="store_true")
	group.add_argument("-q", "--quiet", action="store_true")
	parser.add_argument("-o","--output", help="output result to a file",
		action="store_true")
	

	args = parser.parse_args()

	result = fib(args.num)
	if args.verbose:
		print ("The "+str(args.num)+ "th fib number is "+str(result))
	elif args.quiet:
		print (result)

	if args.output:
		f = open("fibonacci.txt","a")
		f.write(str(result)+'\n')

	else:
		print ("fib("+str(args.num)+")"+str(result))

if __name__ == '__main__': 
	Main()














