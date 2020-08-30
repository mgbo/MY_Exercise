
before, s, after = "I have 2 small bombs and big bomb".partition("bomb")
print(before)   # "I have 2 small "
print(s)        # "bomb"
print(after)    # "s and big bomb"

print "\n---------"

before, s, after = "I have 2 small bombs and big bomb".partition("dog")
print(before)   # "I have 2 small bombs and big bomb"
print(s)        # ""
print(after)    # ""

s = map(int,raw_input().split())
print s


