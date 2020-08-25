import numpy

def fitness(equation_inputs, pop):
  f = numpy.sum(pop*equation_inputs, axis = 1)
  return f

def mating_pool(pop, fitness, num_parents):
  parents = numpy.empty(num_parents, pop.shape[1])
  for parent in range(num_parents):
    max_fitness = numpy.where(fitness == numpy.max(fitness))
    max_fitness_idx = max_fitness[0][0]
    parents[parent, :] = pop[max_fitness_idx, :]
    fitness[max_fitness_idx] = -999999999
  return parents

def crossover(parents, offspring_num):
  offspring = numpy.empty(offspring_num)
  crossover_point = numpty.uint8(offspring_num[1]/2)
  for x in range(offspring_num[0]):
    #Index of first parent
    parent1_idx = x%parents.shape[0]
    #Index of second parent
    parent2_idx = (x+1)%parents.shape[0]
    #Offspring will have first half of genes taken from first parent, second half from second parent
    offspring[x, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
    offspring[x, crossover_point:] = parents[parent2_idx, crossover_point:]
  return offspring

def mutation(offspring_crossover):
  # Mutation randomly changes a single gene in each offspring
  for x in range(offspring_crossover.shape[0]):
    rnd_val = numpy.random.uniform(-1.0, 1.0, 1)
    offspring_crossover[x, 4] = offspring_crossover[x, 4] + rnd_val
  return offspring_crossover

equation_inputs = [height, clears, holes, blockages]
num_weights = 6

# Genetic Algorithm parameters: population size, mating pool size
solutions_per_pop = 10
num_parents = 4

# Defining population size
pop_size = (solutions_per_pop, num_weights)

# Creating initial population
population = numpy.random.uniform(low = -4, high = 4, size = pop_size)

num_generations = 5
for generation in range(num_generations):
  print("Generation : ", generation)
  fitness = fitness(equation_inputs, population)
  parents = mating_pool(init_population, fitness, num_parents)
  offspring_crossover = crossover(parents, offspring_num = (pop_size[0]-parents.shape[0], num_weights))
  offspring_mutation = mutation(offspring_crossover)
  # Creating new population based on parents and offspring
  population[0:parents.shape[0], :] = parents
  population[parents.shape[0]:, :] = offspring_mutation

fitness = fitness(equation_inputs, population)
best_idx = numpy.where(fitness == numpy.max(fitness))

print("Best solution : ", population[best_idx, :])
print("Best solution fitness : ", fitness[best_idx])