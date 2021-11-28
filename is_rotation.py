#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 19:58:52 2021

@author: jean
"""

# Implement your function below.
def is_rotation(list1, list2):
    if len(list1) != len(list2):
        return False
    
    first_equal = 0
    while first_equal < len(list1) and list1[0] != list2[first_equal]:
        first_equal += 1
    
    element = 0
    equal = True
    while element < len(list1) and equal:
        equal = equal and list1[ element ] == list2[ ( element + first_equal ) % len(list2) ]
        element += 1
    return equal

# NOTE: The following input values will be used for testing your solution.
list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
# is_rotation(list1, list2a) should return False.
list2b = [4, 5, 6, 7, 1, 2, 3]
# is_rotation(list1, list2b) should return True.
list2c = [4, 5, 6, 9, 1, 2, 3]
# is_rotation(list1, list2c) should return False.
list2d = [4, 6, 5, 7, 1, 2, 3]
# is_rotation(list1, list2d) should return False.
list2e = [4, 5, 6, 7, 0, 2, 3]
# is_rotation(list1, list2e) should return False.
list2f = [1, 2, 3, 4, 5, 6, 7]
# is_rotation(list1, list2f) should return True.
list2g = [7, 1, 2, 3, 4, 5, 6]
# is_rotation(list1, list2g) should return True.

