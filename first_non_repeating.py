#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 20:30:52 2021

@author: jean
"""

# Implement your function below.
def non_repeating(given_string):    
    count = dict()
    
    for char in given_string:        
        if char in count:
            count[char] +=1
        else: 
            count[char] = 1
    
    for char in given_string:        
        if count[char] == 1:
            return char
        
    return None
    
    

# NOTE: The following input values will be used for testing your solution.
print(non_repeating("abcab"))# should return 'c'
print(non_repeating("abab"))# should return None
print(non_repeating("aabbbc"))# should return 'c'
print(non_repeating("aabbdbc")) # should return 'd'