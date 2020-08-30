

s = input()
first_word = s[:s.find(' ')]

#print ("first_word : ",first_word)

second_word = s[s.find(' ') + 1:]

#print ("second_word : ",second_word)

print(second_word + ' ' + first_word)

