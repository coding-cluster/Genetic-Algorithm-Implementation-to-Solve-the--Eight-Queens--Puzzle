'''
    .-    .-..  .     -..-  ..    ...       --..  ..-   -.    ..    --.   .-
    A     L     E     X     I     S         Z     Ú     Ñ     I     G     A
-------------------------------------------------------------------------------
                { Full name } : Alexis Alberto Zúñiga Alonso
        { Instagram: @thisisalexza }        { GitHub: @codingcluster }
                                © Copyright 2025
-------------------------------------------------------------------------------
>> Description:
 > Genetic algorithm implementation to solve the "Eight Queen" optimisation
 > problem using Python.
'''

import utilities as ut
from algorithms import Individual


def main():
    # Program start
    ut.logo()

    individual = Individual([])
    individual.randomChromosomeGeneration()
    individual


if __name__ == "__main__":
    main()
