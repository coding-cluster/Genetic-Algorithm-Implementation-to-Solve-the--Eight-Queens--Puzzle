import random
import numpy as np

class Individual:
    def __init__(self, chromosome=None):
        # Chromosome is a list of 8 integers (rows 0..7) for each column
        self.chromosome = np.array(chromosome) if chromosome is not None else []
        self.fitness = None
    
    def randomChromosomeGeneration(self, size: int = 8):
        """
        Generate a random chromosome of given size and store in self.chromosome.

        For 8-queens, size=8 and values are 0..7 (row index per column).
        """
        self.chromosome = [random.randint(0, size - 1) for _ in range(size)]
        return self.chromosome
    
    def calculate_fitness(self, global_max):
        """
        Compute fitness as the negative number of conflicting queen pairs.

        Conflicts are counted for queens sharing the same row or diagonals.
        Higher is better; 0 means a valid solution with no conflicts.
        """
        chrom = self.chromosome     # New instance of chromosome
        
        n = len(chrom)              # Length of the chromosome
        # Check if the chromosome is empty
        if chrom == None or n == 0:
            print("Invalid Chromosome")
            return 0
            
        conflicts = 0               # Conflict counter to calculate fitness
        
        # Count conflicts: check each pair of queens
        for i in range(n):
            for j in range(i + 1, n):       # Start from i + 1 to avoid double-counting
                # Check if queens are on the same row
                if chrom[i] == chrom[j]:
                    conflicts += 1
                # Check if queens are on the same diagonal
                # Analog to the formula |x_1 - x_2| == |y_1 - y_2|
                if abs(i - j) == abs(chrom[i] - chrom[j]):
                    conflicts += 1
        
        self.fitness = global_max - conflicts
        return self.fitness
    
    # Returns a string with the chromosome itself, and its fitness
    def __repr__(self) -> str:
        return f"Individual(chromosome={self.chromosome}, fitness={self.fitness})"
    