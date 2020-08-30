
import argparse

parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()

group.add_argument("-s", "--sub", action="store_true")
group.add_argument("-m", "--mul", action="store_true")

parser.add_argument("x", type=int, help="integer1")
parser.add_argument("y", type=int, help="integer2")

args = parser.parse_args()
answer = args.x + args.y

if args.sub:
    print ('{} - {} = {}'.format(args.x, args.y, args.x-args.y))

elif args.mul:
    print ('{} * {} = {}'.format(args.x, args.y, args.x * args.y))

else:
    print ('{} + {} = {}'.format(args.x, args.y , answer))