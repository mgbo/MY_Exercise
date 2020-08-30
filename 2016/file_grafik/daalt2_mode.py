#matplotlib inline

from matplotlib import pyplot as plt

input_data = open('bet8_1.log', 'r')

durations = list()
seconds = list()

for line in input_data:
	(sec,action, duration) = line.split()
	durations.append(duration)
	seconds.append(sec)

plt.plot(seconds, durations, marker='o', ls='')
plt.xlabel('Time from January 1, 1970, seconds')
plt.ylabel('Duration of actions, seconds')
plt.show()
input_data.close()
