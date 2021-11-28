#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 14:27:14 2021

@author: jean
"""

# Implement your function below.
def click(field, num_rows, num_cols, given_i, given_j,c):    
    if field[given_i][given_j] != 0:
        return field
    
    field[given_i][given_j] = -2
    points = generate_points((given_i, given_j),num_rows, num_cols)
    
    for point in points:        
        a,b = point
        if field[a][b] == 0:
            field = click(field, num_rows, num_cols, a, b,c+1)
            field[a][b] = -2
    
    return field

def generate_points( pos , num_rows, num_cols ):
    x,y = pos
    range_x = range( max( 0,  x - 1 ) , min( num_rows , x + 2 ))
    range_y = range( max( 0,  y - 1 ) , min( num_cols , y + 2 ))    
    points = list()
    for a in range_x:
        for b in range_y:
            if (a,b) != pos:
                points.append((a,b))
    
    return points

# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
field1 = [[0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, -1, 1, 0]]

# 
print(to_string(click(field1, 3, 5, 2, 2,0)))
#should return:
# [[0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 0],
#  [0, 1, -1, 1, 0]]

# 

print(to_string(click(field1, 3, 5, 1, 4,0)))
#
#should return:
# [[-2, -2, -2, -2, -2],
#  [-2, 1, 1, 1, -2],
#  [-2, 1, -1, 1, -2]]


field2 = [[-1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, -1]]

# 
print(to_string(click(field2, 4, 4, 0, 1,0)))
#should return:
# [[-1, 1, 0, 0],
#  [1, 1, 0, 0],
#  [0, 0, 1, 1],
#  [0, 0, 1, -1]]

# 
print(to_string(click(field2, 4, 4, 1, 3,0)))
#should return:
# [[-1, 1, -2, -2],
#  [1, 1, -2, -2],
#  [-2, -2, 1, 1],
#  [-2, -2, 1, -1]]