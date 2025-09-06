"""Genetic Algorithm Implementation"""

from algorithms.individual_class import Individual

class GeneticAlgorithm():
    def __init__(self, population):
        self.population = list(population) if population is not None else []

    def generate_population(self, population_size: int, size: int):
        """
        Create a list-based population of Individuals with random chromosomes.
    
        - population_size: number of individuals to create
        - size: board size (N for N-Queens)

        Returns a list[Individual] and also stores it in self.population.
        """
        self.population = []
        # Gaussian formula to calculate pairs
        max_populations = (size * (size - 1)) // 2
        
        for i in range(population_size):
            ind = Individual([])
            ind.random_chromosome_generation(size)
            ind.calculate_fitness(max_populations)
            self.population.append(ind)
        
        return self.population

    def pmx_crossover(self, population: list, population_size: int,
                            size: int):
        print(self.population)