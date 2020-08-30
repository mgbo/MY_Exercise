
# -*- coding:utf-8 -*-

#matplotlib inline

from matplotlib import pyplot as plt

input_data = open('bet8_1.log', 'r')

durations = list()
seconds = list()
actions = []

print "Начально"
print durations


for line in input_data:
	(sec, act, duration) = line.split()
	durations.append(duration)
	seconds.append(sec)
	actions.append(act)


print '1 col is second \n',seconds
print "\n-------\n"
print "Action :\n",actions
print "\n-------\n"
print 'Duration :\n ',durations

plt.plot(seconds, durations, marker='o', ls='')
plt.xlabel('Time from January 1, 1970, seconds')
plt.ylabel('Duration of actions, seconds')
plt.show()
