#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 09:40:51 2021

@author: jean
"""

# Implement your function below.
def mine_sweeper(bombs, num_rows, num_cols):
    # NOTE: field = [[0] * num_cols] * num_rows would not work
    # because you need to create a new list for every row,
    # instead of copying the same list.
    
    points = {}    
    for bomb in bombs:        
        points[tuple(bomb)] = -1
        
        for point in generate_points(tuple(bomb), num_rows, num_cols):            
            if point in points and points[point] > 0:
                points[point] += 1
            else:
                points[point] = 1
    
    field = [[ points[(j,i)] if (j,i) in points else 0 for i in range(num_cols) ] for j in range(num_rows)]
    
    
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

def increment( pos , matrix , num_rows, num_cols ):
    x,y = pos
    matrix[x][y] = -1
    points =  generate_points( pos , num_cols, num_rows )
    for point in points:        
        a,b = point
        if matrix[a][b] >= 0:
            matrix[a][b] += 1
        

# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
# 
#print( to_string( mine_sweeper([[0, 2], [2, 0]], 3, 3))) 
# should return:
# [[0, 1, -1],
#  [1, 2, 1],
#  [-1, 1, 0]]

# 
print( to_string( mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4))) 
# should return:
# [[-1, -1, 2, 1],
#  [2, 3, -1, 1],
#  [0, 1, 1, 1]]

# 
#print( to_string( mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5))) 
# should return:
# [[1, 2, 2, 1, 0],
#  [1, -1, -1, 2, 0],
#  [1, 3, -1, 2, 0],
#  [0, 1, 2, 2, 1],
#  [0, 0, 1, -1, 1]]