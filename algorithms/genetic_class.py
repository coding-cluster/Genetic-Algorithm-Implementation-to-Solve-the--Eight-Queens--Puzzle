import random
import numpy as np

class Individual:
    def __init__(self, chromosome=None):
        # Chromosome is a list of 8 integers (rows 0..7) for each column
        self.chromosome = np.array(chromosome) if chromosome is not None else []
        self.fitness = None
    
    def randomChromosomeGeneration(self, size: int = 8):
        """Generate a random chromosome of given size and store in self.chromosome.

        For 8-queens, size=8 and values are 0..7 (row index per column).
        """
        self.chromosome = [random.randint(0, size - 1) for _ in range(size)]
        return self.chromosome
    
    def __repr__(self) -> str:
        return f"Individual(chromosome={self.chromosome}, fitness={self.fitness})"
        