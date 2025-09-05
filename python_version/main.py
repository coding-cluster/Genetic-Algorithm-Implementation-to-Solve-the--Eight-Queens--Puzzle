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

# << Global constants >>
GLOBAL_MAX = 28
POPULATION = 20
BOARD_SIZE = 8
MAX_GENERATIONS = 50

# << Main funtion >>
def main():
    # << Program Start >>
    ut.logo()

    # Instance creation from class
    individual = Individual([])
    
    '''
    # << Genetic Algorithm Methods >>
    individual.random_chromosome_generation()
    fitness = individual.calculate_fitness(GLOBAL_MAX)
    
    # Show the generated chromosome and its fitness
    print(f"Generated: {individual.chromosome} | Fitness: {fitness}")
    '''
    
    population = individual.create_population(POPULATION, BOARD_SIZE)
    # Print first 3 individuals as a preview
    preview = ", ".join(str(ind) for ind in population[:3])
    print(f"Population size: {len(population)} | Preview: {preview}")

# << Program execution >>
if __name__ == "__main__":
    main()
