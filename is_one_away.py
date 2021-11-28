#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 08:50:24 2021

@author: jean
"""

def is_one_away(s1, s2):    
    s1,s2 = (s1,s2) if len(s1) >= len(s2) else (s2,s1)

    diff = len(s1) - len(s2)
    inc = 0
    count = 0
    
    if(diff > 1):
        return False
    
    for i in range(len(s2)):
        if s1[i+inc] != s2[i]:
            count += 1
            inc += diff
        if count > 1:
            return False
        
    return True

# NOTE: The following input values will be used for testing your solution.
print(is_one_away("abcde", "abcd") )  # should return True
print(is_one_away("abde", "abcde") )  # should return True
print(is_one_away("a", "a") )  # should return True
print(is_one_away("abcdef", "abqdef") )  # should return True
print(is_one_away("abcdef", "abccef") )  # should return True
print(is_one_away("abcdef", "abcde") )  # should return True
print(is_one_away("aaa", "abc")  ) # should return False
print(is_one_away("abcde", "abc")  ) # should return False
print(is_one_away("abc", "abcde")  ) # should return False
print(is_one_away("abc", "bcc")  ) # should return False