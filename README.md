# BinaryGeneticAlgorithm
Python program implementing a genetic algorithm in order to "find" a target binary string. The user passes in the target string via the command line and the program will step through the process of initialization, selection, and reproduction until it finds the target string or a maximum number of iterations has been reached. The user may specify additional paramters for the algorithm via the command line including the population size, mutation rate, and maximum iterations. By default the maximum population size is 100, the mutation rate is 0.05, and there is no upper bound on the number of iterations.

The task is kept simple in order to focus on the algorithm itself, however this code could be modified quite easily in order to suit similar applications - for instance: finding any string of characters rather than only a binary string.

To run the program:
python ga.py <target> <population_size> <mutation_rate> <max_iter>

Ex: python ga.py 01001110101 1000 0.01 5000
