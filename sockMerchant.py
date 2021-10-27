#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sock_merchant(n, ar):
    ar.sort()
    colors = {}
    for i in ar:
        if i in colors:
            colors[i] = colors[i] + 1 
        else:
            colors[i] = 1
    
    pairs = 0
    for i in colors:
        pairs += pairs[i] // 2 
        
    return pairs 
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sock_merchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()