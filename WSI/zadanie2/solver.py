from selection_methods import tournament_selection
import random
import numpy as np
import sympy as sp
from tools import get_start_points
import functions
from math import sqrt


class Function():
    def __init__(self, function, dimensions):
        self.dim = dimensions
        self.fun = function
        self.vars = self.get_variables()

    def get_variables(self):
        variables = []
        x = sp.IndexedBase('x')
        for i in range(self.dim):
            variable = x[i+1]
            variables += [variable]
        return tuple(variables)

    def eval(self, coords):
        value = self.fun

        for j in range(self.dim):
            variable = self.vars[j]
            value = value.subs(variable, coords[j])

        return value


class Individual():
    def __init__(self, coords, function):
        self.genome = coords
        self.cost = self.eval_cost(function)

    def eval_cost(self, function):
        coords = self.genome
        cost = function.eval(coords)
        return cost

    def eval_fitness(self, pop_cost):
        cost = 1 / self.cost
        fitness = cost / pop_cost
        self.fitness = fitness


class Evolution():
    def __init__(self, args):

        self.generation = 0
        function = getattr(functions, args.function)
        self.size = args.size
        self.pc = args.pc
        self.pm = args.pm
        self.mutation_sigma = args.mutation_sigma
        self.function = Function(function(2), 2)

        start_points = get_start_points(
            mean=args.start_points_mean,
            sigma=args.start_points_sigma,
            size=args.size
        )

        self.population = self.create_population(start_points)
        self.eval_fitnesses()
        self.eval_mean_dist()
        self.best_individual()

        self.data = {
            0: [
                start_points,
                self.mean_dist,
                self.champion.genome,
                self.champion.cost
            ],
        }

    def create_population(self, start_points):
        population = []
        for point in start_points:
            individual = Individual(point, self.function)
            population.append(individual)
        return population

    def evolve(self):
        parents = tournament_selection(self.population, self.pc)
        offsprings = self.crossover(parents)
        mutants = self.mutation(offsprings)
        self.population = self.population + mutants + parents
        self.eval_fitnesses()
        self.population = self.choose_population()
        self.eval_mean_dist()
        self.best_individual()
        self.generation += 1
        self.data_update()

    def crossover(self, parents):
        offsprings = []
        for i in range(0, len(parents), 2):
            parent1 = parents[i]
            parent2 = parents[i+1]
            siblings = self.crossover_1p(parent1, parent2)
            offsprings += siblings
        return offsprings

    def crossover_1p(self, A, B):
        genome_A = A.genome
        genome_B = B.genome
        offspr1_genome = (genome_A[0], genome_B[1])
        offspr2_genome = (genome_B[0], genome_A[1])
        offspring1 = Individual(offspr1_genome, self.function)
        offspring2 = Individual(offspr2_genome, self.function)
        offsprings = [offspring1, offspring2]
        return offsprings

    def mutation(self, offsprings):
        sigma = self.mutation_sigma
        mutants = []

        for offspring in offsprings:
            genome = offspring.genome
            mutated_genome = []

            for chromosome in genome:
                if random.random() < self.pm:
                    perturbation = np.random.normal(0, sigma)
                    mutated_chromosome = chromosome + perturbation
                    mutated_genome.append(mutated_chromosome)
                else:
                    mutated_chromosome = chromosome
                    mutated_genome.append(mutated_chromosome)
            mutant = Individual(tuple(mutated_genome), self.function)
            mutants.append(mutant)

        return mutants

    def eval_fitnesses(self):
        inv_cost = 0
        for individual in self.population:
            inv_cost += 1 / individual.cost
        for individual in self.population:
            individual.eval_fitness(inv_cost)

    def eval_mean_dist(self):
        sum_dist = 0
        for individual in self.population:
            coords = individual.genome
            sum_dist += sqrt(coords[0] ** 2 + coords[1] ** 2)
        self.mean_dist = sum_dist / self.size

    def best_individual(self):
        best_fit = 0
        for individual in self.population:
            if individual.fitness > best_fit:
                best_fit = individual.fitness
                best_indiviudal = individual
        self.champion = best_indiviudal

    def choose_population(self):
        population = self.population
        population.sort(key=lambda x: x.fitness, reverse=True)
        chosen_population = population[:self.size]
        return chosen_population

    def data_update(self):
        points = []
        for individual in self.population:
            point = individual.genome
            points.append(point)
        self.data[self.generation] = [
            points,
            self.mean_dist,
            self.champion.genome,
            self.champion.cost
        ]
