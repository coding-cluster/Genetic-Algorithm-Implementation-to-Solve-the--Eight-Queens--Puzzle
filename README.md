<table>
    <tr>
        <td width="35%" valign="top">
            <img src="https://images.unsplash.com/photo-1680783954745-3249be59e527?q=80&w=1064&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="AI concept" width="100%" />
        </td>
        <td valign="top">
            <h1>Eight Queens with a Genetic Algorithm</h1>
            <p>
                <strong>Author:</strong> Alexis Alberto Zúñiga Alonso<br/>
                <strong>Instagram:</strong> <a href="https://instagram.com/thisisalexza" target="_blank">@thisisalexza</a><br/>
                <strong>GitHub:</strong> <a href="https://github.com/codingcluster" target="_blank">@codingcluster</a>
            </p>
        </td>
    </tr>
  
</table>

Solve the classic Eight Queens puzzle using a Genetic Algorithm (GA). This project explores heuristic search, representation, and evolutionary operators to reach constraint satisfaction efficiently.

## Overview
- Goal: Place 8 queens on a chessboard so no two attack each other.
- Method: Genetic Algorithm with population-based search and probabilistic operators.
- Language: Python
- Status: Educational, minimal, easy to extend.

## How it works
- Representation: Each chromosome encodes a board as a permutation of length N (index = column, value = row).
- Fitness: Negative count of conflicts (row and diagonal clashes). Zero conflicts = solution.
- Selection: Tournament or roulette (implementation-dependent).
- Crossover: One-point or ordered crossover suitable for permutations.
- Mutation: Swap or random reset of gene positions.
- Elitism: Best individuals preserved across generations.
- Termination: Found perfect fitness or reached max generations.

## Quickstart
- Python 3.8+ recommended.

## License
This project is licensed under the Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0). See the `LICENSE` file for details.

Photo credits: Images loaded via [Unsplash](https://images.unsplash.com/photo-1680783954745-3249be59e527?q=80&w=1064&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D) Source.