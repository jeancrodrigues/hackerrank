#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumping_on_clouds(c):
    min_path = 0
    idx = 0

    if len(c) == 2:
        return 1

    print("idx {0} min_path {1} c {2}".format(idx , min_path, c[idx]))
    while idx < len(c) - 2:
        min_path += 1        
        if c[idx+2] == 0:
            idx += 2
        else:
            idx += 1

        print("idx {0} min_path {1} c {2}".format(idx , min_path, c[idx]))
    
    if idx < len(c)-1:
        min_path += 1        
    
    return min_path

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumping_on_clouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()