"""Genetic algorithm primitives for N-Queens."""

# << Imports >>
import random

# << Individual's Class >>
class Individual:
    def __init__(self, chromosome=None):
        """Chromosome is a list of N integers (rows 0..N-1) for each column."""
        self.chromosome = list(chromosome) if chromosome is not None else []
        self.fitness = None
        # Optional: generated population storage when using create_population
        self.population = []
    
    def random_chromosome_generation(self, size: int):
        """Generate a random chromosome of given size and store in self.chromosome.

        For N-queens, values are 0..size-1 (row index per column).
        """
        self.chromosome = [random.randint(0, size - 1) for i in range(size)]
        return self.chromosome
    
    def calculate_fitness(self, global_max: int) -> int:
        """Compute fitness as max non-attacking pairs minus conflicts.

        Conflicts are counted for queens sharing the same row or diagonals.
        Higher is better; reaching `global_max` means no conflicts.
        """
        chrom = self.chromosome  # Chromosome reference
        n = len(chrom)  # Length of the chromosome
        conflicts = 0  # Conflict counter to calculate fitness
        
        # Check if the chromosome is empty
        if chrom is None or n == 0:
            print("Invalid Chromosome")
            return 0
        
        # Count conflicts: check each pair of queens
        for i in range(n):
            for j in range(i + 1, n):  # Start from i + 1 to avoid double-counting
                # Same row
                if chrom[i] == chrom[j]:
                    conflicts += 1
                # Same diagonal: |x1 - x2| == |y1 - y2|
                if abs(i - j) == abs(chrom[i] - chrom[j]):
                    conflicts += 1
        
        self.fitness = global_max - conflicts
        return self.fitness

    def create_population(self, population_size: int, size: int):
        """
        Create a list-based population of Individuals with random chromosomes.

        - population_size: number of individuals to create
        - size: board size (N for N-Queens)

        Returns a list[Individual] and also stores it in self.population.
        """
        self.population = []
        
        # Gaussian formula to calculate max pairs
        max_pairs = (size * (size - 1)) / 2
        for i in range(population_size):
            ind = Individual()
            
            ind.random_chromosome_generation()
            ind.calculate_fitness(max_pairs)
            self.population.append(ind)
        
        return self.population
    
    def pmx_algorithm(self, population: int, size: int):
        """
        Partially Mapped Crossover Algorithm:
        Mutation and crossover are applied to generate new offspring. We randomly
        select two crossover points to exchange portions of data. 
        
        Steps:
        1. Selection of Crossover Points
        2. Copy the middle segment
        3. Determine Mapping Relationship to Legalise Offspring
        4. Legalise offprings with the mapping relationship
        """
        pop = self.population
        
    
    # Returns a string with the chromosome itself, and its fitness
    def __repr__(self) -> str:
        return f"Individual(chromosome={self.chromosome}, fitness={self.fitness})"
    