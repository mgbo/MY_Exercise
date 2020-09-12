
import time
import random



names = ['Jhon', 'Corey', 'Adam', 'Steve']
majors = ['Math', 'Engineering', 'CompSci', 'Arts']


# print ('Memory (Before):{} Mb'.format(mem_profile.memory_usage_resource()))


def people_list(num_people):
	result = []

	for i in range(num_people):
		person = {
					'id': i,
					'name': random.choice(names),
					'majors' : random.choice(majors)
		}

		result.append(person)

	return result


def people_generator(num_people):

	for i in range(num_people):
		person = {
					'id': i,
					'name': random.choice(names),
					'majors' : random.choice(majors)
		}
		yield person


# t1 = time.clock()
# people = people_list(1000000)
# t2 = time.clock()

# # print ('Memory (After):{} Mb'.format(mem_profile.memory_usage_resource()))
# print ('Took {} seconds'.format(t2-t1))


t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()
print ('Took {} seconds'.format(t2-t1))





