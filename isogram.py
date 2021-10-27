#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 16:37:19 2020

@author: jean
"""

string = "jean"

def is_isogram(string):
    string = string.lower()
    for i in range(len(string) - 1 ):
        if string[i] in string[i+1:]:
            return False        
    return True

print(is_isogram(""))