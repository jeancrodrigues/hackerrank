#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 10:45:54 2021

@author: jean
"""

from math import sqrt, floor, ceil

def encryption(s):
    s = s.replace(" ","")
    
    nrows = floor(sqrt(len(s)))
    
    ncols = ceil(sqrt(len(s)))
    
    if ncols * nrows < len(s):
        nrows += 1
    
    encoded_strings = []
    for col in range(ncols):
        encoded = ""
        for row in range(nrows):
            pos = col + ( row * ncols )
            encoded += s[pos] if pos < len(s) else ""
        encoded_strings.append(encoded)
    
    return " ".join(encoded_strings)
    
    