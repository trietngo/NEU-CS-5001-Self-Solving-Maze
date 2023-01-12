"""
    CS5001-5003 Fall 2022
    Final Project - Project Ariadne: Self-Solving Mazes
    Triet Ngo
"""

# Import all maze-related functions
from maze_draw_functions import *
from maze_gen_functions import *


def main():
    '''
        Get user inputs to draw a maze.
    '''

    # Greeting message
    print("Welcome to Project Ariadne!")
    print("Generate a maze and see it get solved!")
    print()

    # Get user input to initialize the program
    user_input = input("Type any key to continue. Type 'Quit' to exit the program: ")
    print()

    # Run the program if the user does not input "quit"
    while user_input.lower() != "quit":

        try:
            # Get user inputs
            print("Input the dimensions of your maze.")
            height = input("--Select the height of your maze: ")
            width = input("--Select the width of your maze: ")
            cell_width = input("--Select the size of each cell: ")

            turtle_maze_height = float(cell_width) * int(height)
            turtle_maze_width = float(cell_width) * int(width)

            # Exception handling for drawing. A maze cannot be drawn
            # if it is bigger than the viewport.
            if turtle_maze_height >= window_height() or turtle_maze_width >= window_width():
                suggested_cell_size = int(window_height() / int(height))
                print("Cells are too big to draw. Try a value lower than " + \
                    str(suggested_cell_size) + ".")
                raise ValueError()
            if float(cell_width) < 5:
                raise ValueError("The size of each cell must be at least 5.")
            if not isinstance(float(cell_width), float) or not isinstance(int(cell_width), int):
                raise TypeError("The cell size must be either a float or integer.")

            # Generate a maze and its solution as lists
            maze, tree, maze_exit_pos = maze_gen(int(height), int(width))
            solution = maze_solution(maze, tree, maze_exit_pos)

            # Ask if user wants to continue drawing
            start = input("Your maze is ready to be drawn. Continue (Y/N)? ")

            # If the user says yes, draw the maze
            if start.lower() in ["yes", "y"]:
                draw_maze(maze, int(cell_width), solution)
                done()
            else:
                print("Maze cancelled.")
                print()

        # Exception handling
        except ValueError as error:
            print(error)
        except TypeError as error:
            print(error)
    
    # Exit message
    print("Thank you for using Project Ariadne. Have a good day!")


if __name__ == '__main__':
    main()
