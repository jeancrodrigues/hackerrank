#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeated_string(s, n):
    times = n // len(s)
    left = n % len(s)
    return s.count('a') * times + s[:left].count('a')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeated_string(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()