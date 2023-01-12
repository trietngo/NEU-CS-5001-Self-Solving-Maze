"""
    CS5001-5003 Fall 2022
    Final Project - Unit Testing for Mazes
    Triet Ngo
"""

from maze_gen_functions import *
import unittest

class Test_maze(unittest.TestCase):
    ''' Class Test_maze
    '''

    def test_grid_gen(self):
        ''' Name: test_grid_gen
            Paras: self
            Return: nothing, tests if the maze generated is as desired
        '''
        target_grid = [
            [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
            [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
            [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        ]
        self.assertEqual(grid_gen(3, 4), target_grid)
    
    def test_maze_1x1(self):
        ''' Name: test_maze_1x1
            Paras: self
            Return: nothing, tests if an 1x1 maze will throw a ValueError
        '''
        with self.assertRaises(ValueError):
            maze_gen(1, 1)
    
    def test_maze_100x100(self):
        ''' Name: test_maze_100x100
            Paras: self
            Return: nothing, tests if an 100x100 maze will throw a ValueError
        '''
        with self.assertRaises(ValueError):
            maze_gen(100, 100)
    
    def test_maze_invalid(self):
        ''' Name: test_maze_invalid
            Paras: self
            Return: nothing, tests if inputs other than integers will throw
                    a TypeError
        '''
        with self.assertRaises(TypeError):
            maze_gen(3.5, 4.05)


def main():
    # Start the test with a verbosity of 2 for the test results
    unittest.main(verbosity=2)


if __name__ == '__main__':
    main()
