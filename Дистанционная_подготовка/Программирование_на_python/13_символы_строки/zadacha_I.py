
s = input()

def IsPalindrome(s):
	s = s.lower()
	new = s[::-1]

	if bool(s==new):
		print("YES")
	else:
		print("NO")

IsPalindrome(s)
