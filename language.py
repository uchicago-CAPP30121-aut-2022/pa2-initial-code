"""
CAPP 121: Language shifts

YOUR NAME

Functions for language shift simulation.

This program takes the following parameters:
    grid _file (string): the name of a file containing a sample region
    R (int): neighborhood radius
    A (float): the language state transition threshold A
    Bs (list of floats): a list of the transition thresholds B to
      use in the simulation
    C (float): the language state transition threshold C
      centers (list of tuples): a list of community centers in the
      region
    max_steps (int): maximum number of steps

Example use:
    $ python3 language.py -grid_file tests/writeup-grid-with-cc.txt
	  --r 2 --a 0.5 --b 0.9 --c 1.2 --max_steps 5
While shown on two lines, the above should be entered as a single command.
"""

import copy
import click
import utility


def run_simulation(grid, R, thresholds, centers, max_steps):
    """
    Do the simulation.

    Inputs:
      grid (list of lists of ints): the grid
      R (int): neighborhood radius
      thresholds (float, float, float): the language
        state transition thresholds (A, B, C)
      centers (list of tuples): a list of community centers in the
        region
      max_steps (int): maximum number of steps

    Returns ((int, int, int), int): A tuple containing the frequency of each 
      language state and the number of steps taken in the simulation
    """

    # YOUR CODE HERE

    # REPLACE (0, 0, 0), 0 WITH AN APPROPRIATE RETURN VALUE
    return (0, 0, 0), 0

def median_language_shift_length(grid, R, threshold_list, centers, max_steps):
    """
    Run the simulation with various values of threshold B.

    Inputs:
      grid (list of lists of ints): the grid
      R (int): neighborhood radius
      threshold_list (list of tuples): a list of language state transition
        thresholds (A, B, C)
      centers (list of tuples): a list of community centers in the
        region
      max_steps (int): maximum number of steps

    Returns (int): the median number of steps taken in each simulation. 
    """

    # YOUR CODE HERE

    # REPLACE 0 WITH AN APPROPRIATE RETURN VALUE
    return 0

@click.command(name="language")
@click.option('--grid_file', type=click.Path(exists=True),
              default="tests/writeup-grid.txt", help="filename of the grid")
@click.option('--r', type=int, default=1, help="neighborhood radius")
@click.option('--a', type=float, default=0.6, help="transition threshold A")
@click.option('--b', type=float, default=0.8, help="transition threshold B")
@click.option('--c', type=float, default=1.6, help="transition threshold C")
@click.option('--max_steps', type=int, default=1,
              help="maximum number of simulation steps")
def cmd(grid_file, r, a, b, c, max_steps):
    '''
    Run the simulation.
    '''

    grid, centers = utility.read_grid(grid_file)
    print_grid = len(grid) < 20

    print("Running the simulation...")

    if print_grid:
        print("Initial region:")
        for row in grid:
            print("   ", row)
        if len(centers) > 0:
            print("With community centers:")
            for center in centers:
                print("   ", center)

    # run the simulation
    frequencies, num_steps = run_simulation(grid, r, (a, b, c), centers, max_steps)

    if print_grid:
        print("Final region:")
        for row in grid:
            print("   ", row)

    print("Final language state frequencies:", frequencies)
    print("Number of steps in simulation:", num_steps)

if __name__ == "__main__":
    cmd()
