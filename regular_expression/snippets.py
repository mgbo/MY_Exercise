
import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

Ha HaHa
'''

sentence = 'Start a sentence and then bring it to an end Start'

# print('\tTab')
# print(r'\tTab')
# print('	Tab')
# print(r'	Tab')


pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# matches = pattern.finditer(text_to_search)

# for match in matches:
# 	print(match)


with open('data.txt', 'r') as f:
	contents = f.read()

	

	matches = pattern.finditer(contents)

	for match in matches:
		print(match)










