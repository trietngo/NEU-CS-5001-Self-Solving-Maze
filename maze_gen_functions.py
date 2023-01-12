"""
    CS5001-5003 Fall 2022
    Final Project - Maze Generation and Solution Functions
    Triet Ngo
"""


from random import randint


def grid_gen(height, width):
    ''' Name: grid_gen
        Paras: height and width of the desired grid
        Return: a grid in the form of a list, where each element
        is a row containing elements representing a square
    '''

    # Generate element-wise independent list
    # Each [1, 1, 1, 1] list represents a cell in a grid where
    # every element in that list denotes a side of a square.
    # 1 means there is a side present. 0 means there is no wall to the square.

    grid = [[[1, 1, 1, 1] for i in range(width)] for k in range(height)]
    return grid


def maze_gen(height, width):
    ''' Name: maze_gen
        Paras: height and width of the desired maze
        Return: a maze in the form of a list, where each element
        is a row containing elements representing a cell
    '''

    # Exception handling:
    # Dimension of a maze must be at least 2x2 and at most 70x70.
    if height < 2 or width < 2:
        raise ValueError("Dimension of a maze must be at least 2x2.")
    
    if height > 70 or width > 70:
        raise ValueError("Dimension of a maze must be at most 70x70.")

    if not isinstance(height, int) or not isinstance(width, int):
        raise TypeError("Dimensions of a maze must be an integer.")

    # Generate a grid to be made into a maze
    maze = grid_gen(height, width)

    # Wall positions in a [1, 1, 1, 1] cell
    top = 0
    right = 1
    bottom = 2
    left = 3

    # Select an entry point for the maze
    maze_height = len(maze) - 1
    maze_width = len(maze[0]) - 1

    # Current entry point is (x, 0) on the left side of the maze
    x = randint(0, maze_height)     # height
    y = 0                           # width

    # Set the current visited cell to the entry point
    current_visit = (x, y)

    # Since we start on the left side of the maze,
    # The left wall of the entry cell is erased.
    maze[current_visit[0]][current_visit[1]][left] = 0

    ### Traversal tree

    # Initialize tree and add the entry point to the tree
    tree = []
    tree.append(current_visit)

    # Set up the number of cells visited
    num_visit = 1

    # Total number of cells in a grid equals
    # the product of the height and width of the maze
    total_cells = len(maze) * len(maze[0])

    # While there is still an unvisited cell
    while num_visit != total_cells:

        # Possible neighboring cells for each cell given

        # If the cell is in the upper left corner (0, 0)
        # possible neighbors are cells to the right and below
        if x == 0 and y == 0:
            current_neighbors = [(x + 1, y),   
                                (x, y + 1)]

        # If the cell is in the top row with corners excluded
        # possible neighbors are cells to the right, left, and below
        elif x == 0 and y < maze_width:
            current_neighbors = [(x + 1, y),   
                                (x, y + 1),
                                (x, y - 1)]

        # If the cell is in the leftmost column with corners excluded
        # possible neighbors are cells to the right, cells above and below
        elif y == 0 and x < maze_height:
            current_neighbors = [(x + 1, y),
                                (x - 1, y),
                                (x, y + 1)]

        # If the cell is in the bottom-left corner
        # possible neighbors are cells above and cells to the right
        elif x == maze_height and y == 0:
            current_neighbors = [(x - 1, y),   
                                (x, y + 1)]

        # If the cell is in the top-right corner
        # possible neighbors are cells below and cells to the left
        elif y == maze_width and x == 0:
            current_neighbors = [(x + 1, y),
                                (x, y - 1)]
        
        # If the cell is in the bottom row with corners excluded
        # possible neighbors are cells above and cells to the left and right
        elif x == maze_height and 0 < y and y < maze_width:
            current_neighbors = [(x - 1, y),   
                                (x, y + 1),
                                (x, y - 1)]

        # If the cell is in the rightmost column with corners excluded
        # possible neighbors are cells above and below, and cells to the left
        elif y == maze_width and 0 < x and x < maze_height:
            current_neighbors = [(x + 1, y),
                                (x - 1, y),
                                (x, y - 1)]
        
        # If the cell is in the bottom-right corner
        # possible neighbors are cells above and cells to the left
        elif x == maze_height and y == maze_width:
            current_neighbors = [(x - 1, y),
                               (x, y - 1)]

        # Otherwise, a cell typically has 4 neighboring cells
        else:
            current_neighbors = [(x + 1, y),
                                (x - 1, y),   
                                (x, y + 1),
                                (x, y - 1)]

        # Evaluate the neighbors of the current cells:
        # If any neighbor is already in the traversal tree
        # Remove that neighbor from the list
        for item in current_neighbors:
            if item in tree:
                current_neighbors.remove(item)

        # Select a random neighbor to evaluate
        neighbor_index = randint(0, len(current_neighbors) - 1)
        neighbor = current_neighbors[neighbor_index]

        if neighbor in tree:

            # If the neighbor is already in the traversal tree
            # Remove that neighbor from the list and the search backtracks
            current_neighbors.remove(neighbor)
            current_visit = tree[tree.index(current_visit) - 1]

            # Whenever the search backtracks, number of nodes visited
            # decreases by 1
            num_visit -= 1

        # If the neighbor is not in the traversal tree
        # Move the search to the neighbor and make the neighbor
        # the current visit.
        elif neighbor not in tree:

            # Check where to remove wall:
            if neighbor == (x + 1, y):

                # If go down, remove bottom wall of current visit:
                maze[current_visit[0]][current_visit[1]][bottom] = 0

                # If go down, remove top wall of neighbor:
                maze[neighbor[0]][neighbor[1]][top] = 0

            elif neighbor == (x - 1, y):

                # If go up, remove top wall of current visit:
                maze[current_visit[0]][current_visit[1]][top] = 0

                # If go up, remove bottom wall of neighbor:
                maze[neighbor[0]][neighbor[1]][bottom] = 0

            elif neighbor == (x, y + 1):

                # If go right, remove right wall of current visit:
                maze[current_visit[0]][current_visit[1]][right] = 0

                # If go right, remove left wall of neighbor:
                maze[neighbor[0]][neighbor[1]][left] = 0
            
            elif neighbor == (x, y - 1):

                # If go left, remove left wall of current visit:
                maze[current_visit[0]][current_visit[1]][left] = 0

                # If go right, remove left wall of neighbor:
                maze[neighbor[0]][neighbor[1]][right] = 0

            # Set the neighboring cell as the current visited cell
            current_visit = neighbor

            # Add the current visited cell to the traversal tree
            tree.append(current_visit)

        # Update the coordinates according to the current visited cell
        x = current_visit[0]
        y = current_visit[1]

        # Move on to the next cell
        num_visit += 1
    
    ### Pick a random exit:
    # Set up the coordinates of the exit
    # The exit will be assigned randomly among
    # the right-most cell
    x_exit = randint(0, maze_height)
    y_exit = maze_width

    # Assign a position to the exit coordinates
    maze_exit_pos = (x_exit, y_exit)

    # Since the a right-most cell is the exit,
    # the right wall of that cell is erased.
    maze_exit = maze[x_exit][y_exit]
    maze_exit[right] = 0

    # Return the maze, traversal tree, and exit coordinates
    return maze, tree, maze_exit_pos

def maze_solution(maze, tree, exit_point):
    ''' Name: maze_solution
        Paras: maze, tree, exit_point returned from maze_gen
        Return: a shortest-path solution to the maze in the form
        of a list of coordinates
    '''

    # Since the traversal tree contains all the cells of the maze.
    # and the exit point is in the rightmost column of the maze.
    # the solution is a walk from the entry point to the exit point
    solution_walk = tree[:(tree.index(exit_point) + 1)]

    # Initialize the shortest path solution
    solution_path = solution_walk

    ### Iterate through the current path backwards

    # Start from the exit point:
    index = len(solution_path) - 1

    # While loop is active if not all vertices have been evaluated
    while index > 0 and index < len(solution_path):

        # The current coordinate
        x_cur = solution_path[index][0]
        y_cur = solution_path[index][1]

        # The previous coordinate
        x_prev = solution_path[index - 1][0]
        y_prev = solution_path[index - 1][1]

        # Possible neighbors of any current coordinates
        possible_neighbors = [(x_cur + 1, y_cur),
                              (x_cur - 1, y_cur),
                              (x_cur, y_cur + 1),
                              (x_cur, y_cur - 1)]

        # Check the current cell in the maze with the
        # current coordinates:

        # If the cell has a top wall, the previous cell
        # must not be above the current cell
        if maze[x_cur][y_cur][0] == 1:
            possible_neighbors.remove((x_cur - 1, y_cur))
        
        # If the cell has a right wall, the previous cell
        # must not be to the right of the current cell
        if maze[x_cur][y_cur][1] == 1:
            possible_neighbors.remove((x_cur, y_cur + 1))
        
        # If the cell has a bottom wall, the previous cell
        # must not be below the current cell
        if maze[x_cur][y_cur][2] == 1:
            possible_neighbors.remove((x_cur + 1, y_cur))
        
        # If the cell has a left wall, the previous cell
        # must not be to the left of the current cell
        if maze[x_cur][y_cur][3] == 1:
            possible_neighbors.remove((x_cur, y_cur - 1))

        # If the previous coordinate is not a possible neighbor
        # of the current cell, then that coordinate is popped from
        # the traversal tree.
        if (x_prev, y_prev) not in possible_neighbors:
            solution_path.pop(index - 1)
            index -= 1

        # If the previous coordinate is a possible neighbor
        # of the current cell, then the search continues backwards.
        elif (x_prev, y_prev) in possible_neighbors:
            index -= 1

    # The function returns the shortest path in the form
    # of a list of coordinates
    return solution_path