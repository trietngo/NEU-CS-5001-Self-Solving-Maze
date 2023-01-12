"""
    CS5001-5003 Fall 2022
    Final Project - Drawing Self-Solving Mazes
    Triet Ngo
"""

# Import Turtle and all maze generation functions
from turtle import *
from maze_gen_functions import *


# Initialize the pen
maze_pen = Turtle()
maze_pen.hideturtle()
maze_pen.speed(0)
maze_pen.width(1)

# Draw horizontal walls
def draw_x(maze, cell_width, start_x, start_y):
    ''' Name: draw_x
        Paras:
            maze - the generated maze in the form of a list
            cell_width - width or size of the cell
            start_x - starting x coordinate
            start_y - starting y coordinate
        Return: nothing, draw a series of horizontal lines
    '''

    # Define number of rows and columns
    num_row = len(maze)
    num_column = len(maze[0])
    
    # Iterate through each row of the maze
    for i in range(1, num_row + 1):

        # For each square in a row, if a horizontal
        # wall does not exist in the maze, Turtle does not draw
        for k in range(1, (num_column + 1)):
            if maze[i - 1][k - 1][0] == 0:
                maze_pen.up()
            elif maze[i - 1][k - 1][0] == 1:
                maze_pen.down()
            maze_pen.forward(cell_width)

        maze_pen.up()
        maze_pen.setpos(start_x, (cell_width * (-i) + start_y))
        maze_pen.down()
    

    # Draw the bottom row and set position for the vertical walls
    maze_pen.down()
    maze_pen.forward(cell_width * num_column)
    maze_pen.up()
    maze_pen.setpos(start_x, (cell_width * (2 - num_row) + start_y))

# Draw vertical walls
def draw_y(maze, cell_width, start_x, start_y):
    ''' Name: draw_y
        Paras:
            maze - the generated maze in the form of a list
            cell_width - width or size of the cell
            start_x - starting x coordinate
            start_y - starting y coordinate
        Return: nothing, draw a series of vertical lines
    '''

    # Define number of rows and columns
    num_row = len(maze)
    num_column = len(maze[0])

    # Draw the leftmost vertical side of the maze
    # If a section does not have a vertical wall,
    # or that the entry point is detected, do not draw
    # a vertical wall
    for r in range(1, (num_row + 1)):
        if maze[r - 1][0][3] == 0:
            maze_pen.up()
        elif maze[r - 1][0][3] == 1:
            maze_pen.down()

    # Set up the next position to draw all the inner
    # vertical walls
    maze_pen.setpos((0 + start_x), start_y)
    
    # For each square in a row, if a vertical
    # wall does not exist in the maze, Turtle does not draw
    for i in range(1, num_column + 1):

        for k in range(1, (num_row + 1)):
            
            if maze[k - 1][i - 1][3] == 0:
                maze_pen.up()
            elif maze[k - 1][i - 1][3] == 1:
                maze_pen.down()
            
            maze_pen.forward(cell_width)

        maze_pen.up()

        maze_pen.setpos((cell_width * i + start_x), start_y)
        maze_pen.down()
    
    # Draw the rightmost vertical side of the maze
    # If a section does not have a vertical wall,
    # or that the exit point is detected, do not draw
    # a vertical wall
    for j in range(1, (num_row + 1)):

        if maze[j - 1][num_column - 1][1] == 0:
            maze_pen.up()
        elif maze[j - 1][num_column - 1][1] == 1:
            maze_pen.down()
        
        maze_pen.forward(cell_width)


def draw_solution(maze, cell_width, solution_path, start_x, start_y):
    ''' Name: draw_solution
        Paras:
            maze - the generated maze in the form of a list
            cell_width - width or size of the cell
            solution_path - mathematical solution of the maze as a list
                            of tuples
            start_x - starting x coordinate
            start_y - starting y coordinate
        Return: nothing, draw the solution to the
    '''

    # Set up the solution path
    maze_pen.showturtle()
    maze_pen.width(cell_width / 10)
    maze_pen.color("red")

    # Get the entry point from the path list
    entry_point = solution_path[0]

    # Setting up the starting position for the solution path
    x_entry = entry_point[0]
    y_entry = entry_point[1]

    sol_start_x = start_x - (cell_width / 2)
    sol_start_y = start_y - ((x_entry + 0.5) * cell_width)

    maze_pen.setpos(sol_start_x, sol_start_y)

    ### Traverse through the maze:

    # Initial position and heading
    maze_pen.down()
    maze_pen.forward(cell_width)
    maze_pen.setheading(0)

    # Iterate through all the coordinates in the solution list
    for i in range(0, len(solution_path) - 1):

        # Current set of (x, y) coordinate
        x_cur = solution_path[i][0]
        y_cur = solution_path[i][1]

        # Next set of (x, y) coordinate
        x_next = solution_path[i + 1][0]
        y_next = solution_path[i + 1][1]

        # Current set of Turtle coordinates
        x_cur_pos = start_x + (cell_width * (y_cur + 0.5))
        y_cur_pos = start_y - ((x_cur + 0.5) * cell_width)

        # Next set of Turtle coordinates
        x_next_pos = start_x + (cell_width * (y_next + 0.5))
        y_next_pos = start_y - ((x_next + 0.5) * cell_width)

        # Possible neighboring coordinates of any given cell
        possible_neighbors = [(x_cur + 1, y_cur),
                              (x_cur - 1, y_cur),
                              (x_cur, y_cur + 1),
                              (x_cur, y_cur - 1)]

        # If the arrow goes up
        if solution_path[i + 1] == (x_cur - 1, y_cur):
            maze_pen.setheading(90)
            maze_pen.setpos(x_cur_pos, y_cur_pos + cell_width)
        
        # If the arrow goes right
        elif solution_path[i + 1] == (x_cur, y_cur + 1):
            maze_pen.setheading(0)
            maze_pen.setpos(x_cur_pos + cell_width, y_cur_pos)
        
        # If the arrow goes down
        elif solution_path[i + 1] == (x_cur + 1, y_cur):
            maze_pen.setheading(270)
            maze_pen.setpos(x_cur_pos, y_cur_pos - cell_width)
        
        # If the arrow goes left
        elif solution_path[i + 1] == (x_cur, y_cur - 1):
            maze_pen.setheading(180)
            maze_pen.setpos(x_cur_pos - cell_width, y_cur_pos)
        
        # Otherwise, just go to the next set of coordinates
        elif solution_path[i + 1] not in possible_neighbors:
            maze_pen.setpos(x_next_pos, y_next_pos)
    
    # Setup the exit path
    exit_point = solution_path[-1]
    x_exit = exit_point[0]
    y_exit = exit_point[1]

    # Exit path's Turtle coordinate
    sol_end_x = start_x + ((y_exit + 0.5) * cell_width)
    sol_end_y = start_y - ((x_exit + 0.5) * cell_width)

    # Draw the exit path
    maze_pen.setpos(sol_end_x, sol_end_y)
    maze_pen.setheading(0)
    maze_pen.forward(cell_width)

    done()


def draw_maze(maze, cell_width, solution_path):
    ''' Name: draw_maze
        Paras:
            maze - the generated maze in the form of a list
            cell_width - width or size of the cell
            solution_path - mathematical solution of the maze as a list
                            of tuples 
        Return: nothing, draw a maze that solves itself
    '''

    # Making sure the maze is always at the center
    # of the Turtle screen
    start_x = -(cell_width * (len(maze[0])) / 2)
    start_y = cell_width * (len(maze) / 2)

    # Starting position
    maze_pen.up()
    maze_pen.setpos(start_x, start_y)
    maze_pen.down()

    # Draw all horizontal lines
    draw_x(maze, cell_width, start_x, start_y)

    # Set up position and heading for vertical lines
    maze_pen.up()
    maze_pen.right(90)
    maze_pen.setpos(start_x, start_y)
    maze_pen.down()

    # Draw all vertical lines
    draw_y(maze, cell_width, start_x, start_y)

    # Set up heading for the solution
    maze_pen.up()
    maze_pen.left(90)

    # Draw the solution math
    draw_solution(maze, cell_width, solution_path, start_x, start_y)

    done()