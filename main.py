'''
    .-    .-..  .     -..-  ..    ...       --..  ..-   -.    ..    --.   .-
    A     L     E     X     I     S         Z     Ú     Ñ     I     G     A
--------------------------------------------------------------------------------
                { Full name } : Alexis Alberto Zúñiga Alonso
        { Instagram: @thisisalexza }        { GitHub: @coding-cluster }
                                © Copyright 2025
--------------------------------------------------------------------------------
>> Description:
 > Genetic algorithm implementation to solve the "Eight Queen" optimisation
 > problem using Python.
'''

# << Imports >>
import utilities as ut
from algorithms import Individual
from numpy import array

# << Global constants >>
GLOBAL_MAX = 28

# << Main funtion >>
def main():
    # << Program Start >>
    ut.logo()

    # Instance creation from class
    individual = Individual(array([]))
    
    # << Genetic Algorithm Methods >>
    individual.randomChromosomeGeneration()
    fitness = individual.calculate_fitness(GLOBAL_MAX)
    
    # Show the generated chromosome and its fitness
    print(f"Generated: {individual.chromosome} | Fitness: {fitness}")

# << Program execution >>
if __name__ == "__main__":
    main()
