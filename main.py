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

import utilities as ut
from algorithms import Individual
from numpy import array

GLOBAL_MAX = 28

def main():
    # Program start
    ut.logo()

    individual = Individual(array([]))
    individual.randomChromosomeGeneration()
    fitness = individual.calculate_fitness(GLOBAL_MAX)
    print(f"Generated: {individual.chromosome} | Fitness: {fitness}")

if __name__ == "__main__":
    main()
