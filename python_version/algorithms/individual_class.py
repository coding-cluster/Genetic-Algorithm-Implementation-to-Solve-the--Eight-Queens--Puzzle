"""Genetic algorithm primitives for N-Queens."""

# << Imports >>
import random

# << Individual's Class >>
class Individual:
    def __init__(self, chromosome=None):
        """Chromosome is a list of N integers (rows 0..N-1) for each column."""
        self.chromosome = list(chromosome) if chromosome is not None else []
        self.fitness = None
    
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
        conflicts = 0
        
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
    
    # Returns a string with the chromosome itself, and its fitness
    def __repr__(self) -> str:
        return f"Individual(chromosome={self.chromosome}, fitness={self.fitness})"
    