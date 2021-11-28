#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 18:28:09 2021

@author: jean
"""

# Implement your function below.
def common_elements(list1, list2):
    
    result = []
    if len(list1) == 0 or len(list1) == 0:
        return result
    
    left = right = 0
    
    while left < len(list1) and right < len(list2):
        print( "{0} {1}".format(  list1[left] , list2[right]))
        
        if list1[left] == list2[right]:
            result.append(list1[left])
            left += 1
            right += 1
        
        elif list1[left] > list2[right]:
            right+=1
        else:
            left +=1
            
    return result


# NOTE: The following input values will be used for testing your solution.
list_a1 = [1, 3, 4, 6, 7, 9]
list_a2 = [1, 2, 4, 5, 9, 10]
# 
common_elements(list_a1, list_a2) # should return [1, 4, 9] (a list).

list_b1 = [1, 2, 9, 10, 11, 12]
list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
# 
common_elements(list_b1, list_b2) # should return [1, 2, 9, 10, 12] (a list).

list_c1 = [0, 1, 2, 3, 4, 5]
list_c2 = [6, 7, 8, 9, 10, 11]
# 
common_elements(list_c1, list_c2) # should return [] (an empty list).