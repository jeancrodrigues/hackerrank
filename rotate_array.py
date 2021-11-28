#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 15:09:05 2021

@author: jean
"""

# Implement your function below.
# n = # rows = # columns in the given 2d array
def rotate(given_array, n):
    for row in range( n//2 ):
        for col in range( row, n - 1 - row ):
            print("{0}".format((row,col)))
            first_point = (row,col)
            point = next_point(first_point, n)
            aux = given_array[row][col]
            while first_point != point:
                aux = exchange_values(given_array, aux, point)
                point = next_point(point, n)        
            given_array[row][col] = aux
    return given_array

def exchange_values(given_array, value, dest_point):
    row_dest, col_dest = dest_point
    aux = given_array[row_dest][col_dest]
    given_array[row_dest][col_dest]=value
    return aux
                
def next_point(point, n):
    row, col = point
    return ( col , ( n - 1 - row ) % n )

def find_point_sequence(first_point, n):
    
    x,y = first_point    
    point = ( y , ( n - 1 - x ) % n )    
    print(point)
    
    while point != first_point:    
        x,y = point        
        point = ( y , ( n - 1 - x ) % n )
        print(point)
    


# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
a1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

a3 = [[1]]
a4 = [[1,2],[3,4]]
#print(to_string(rotate(a1, 3)))
# rotate(a1, 3) should return:
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]

a2 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]]

#print(to_string(rotate(a2, 4)))
# rotate(a2, 4) should return:
# [[13, 9, 5, 1],
#  [14, 10, 6, 2],
#  [15, 11, 7, 3],
#  [16, 12, 8, 4]]

