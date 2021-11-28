#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 22:03:26 2021

@author: jean
"""

# Implement your function below.
def most_frequent(given_list):
    if len(given_list) == 0:
        return None
    
    max_item = None
    items = dict()
    max_count = 0    
    
    for element in given_list:
        if element in items:
            items[element] += 1
        else:
            items[element] = 1
        
        if items[element] > max_count:
            max_count = items[element]
            max_item = element
            
    return max_item

# NOTE: The following input values will be used for testing your solution.

list1 = [1, 3, 1, 3, 2, 1]
# most_frequent(list1) should return 1

list2 = [3, 3, 1, 3, 2, 1]
# most_frequent(list2) should return 3

list3 = []
# most_frequent(list3) should return None

list4 = [0]
# most_frequent(list4) should return 0

list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]
# most_frequent(list5) should return -1