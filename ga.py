"""
Ex: python ga.py <target> <population_size> <mutation_rate> <max_iter> 
"""

import sys
import random
import math
#create random binary string of given length
def random_init(length):
	res = list("0" * length)
	for i in range(len(res)):
		if 0.5 < random.uniform(0,1):
			res[i] = "1"
	return "".join(res)

#calculate fitness of test given target, simple fitness calculation is the number of correct characters
def calc_fitness(test, target):
	fitness = 0
	for i in range(len(test)):
		if test[i] == target[i]:
			fitness += 1
	return fitness

#uniform crossover function, each bit from each parent has a 50% chance of being represented in the child
def uniform_crossover(p1, p2):
	c = []
	for i in range(len(p1)):
		if 0.5 < random.uniform(0,1):
			c.append(p1[i])
		else:
			c.append(p2[i])
	return "".join(c)

#mutate string x with probability mr
def mutate(x, mr):
	m = list(x)
	for i in range(len(x)):
		if mr < random.uniform(0,1):
			#flip bit
			m[i] = "1" if m[i] == "0" else "0"
	return "".join(m)

#get target from command line input
if len(sys.argv) < 2:
	print("No solution given. Terminating.")
	sys.exit()

target = sys.argv[1]
#default values
max_iter = 0
mut_rate = 0.05
pop_size = 100

if len(sys.argv) >= 3:
	pop_size = int(sys.argv[2])
if len(sys.argv) >= 4:
	mut_rate = float(sys.argv[3])
if len(sys.argv) >= 5:
	max_iter = int(sys.argv[4])

#init population
population = []
for i in range(pop_size):
	population.append(random_init(len(target)))	#get random binary strings as initial population

#Loop over rest:
num_iter = 0
while(max_iter == 0 or num_iter < max_iter):
	#eval fitness (optimal fitness is len(target))
	fit = []
	max_fit = 0
	curr_best = population[0]
	for i in range(pop_size):
		fit.append(calc_fitness(population[i], target))
		if fit[i] > max_fit:
			max_fit = fit[i]
			curr_best = population[i]
		#check if target found
		if fit[i] == len(target):
			print(curr_best)
			print("Target found in " + str(num_iter) + " iterations.")
			sys.exit(0)

	#output fittest member for this iteration
	print(curr_best)

	#create mating pool
	#normalize fitness scores
	sum_fit = sum(fit)
	for i in range(pop_size):
		fit[i] = fit[i] / sum_fit
		#round to two decimal places and multiply by 100 for whole numbers
		fit[i] = math.ceil(fit[i]*100)

	#probabalistically allocate members based on fitness, population[i] is allocated fit[i] times
	mating_pop = []
	for i in range(pop_size):
		for j in range(fit[i]):
			mating_pop.append(population[i])

	#shuffle array
	random.shuffle(mating_pop)

	#crossover
	new_pop = []
	for i in range(pop_size):
		#perform uniform crossover on 2 random parents from the population
		new_pop.append( uniform_crossover( mating_pop[random.randint(0,len(mating_pop)-1)] , mating_pop[random.randint(0,len(mating_pop)-1)] ) )
		#mutate
		new_pop[i] = mutate(new_pop[i], mut_rate)

	population = new_pop

	num_iter += 1