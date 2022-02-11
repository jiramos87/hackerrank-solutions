#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    integer_sum = 0
    solution_count = 0
    for i in range(0, len(s)):
        if i > len(s) - m:
            return solution_count
        else:
            for j in range(i, i + m):
                integer_sum += s[j]
            if integer_sum == d:
                solution_count += 1
            integer_sum = 0
    return solution_count
            

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # s = list(map(int, input().rstrip().split()))

    # first_multiple_input = input().rstrip().split()

    # d = int(first_multiple_input[0])

    # m = int(first_multiple_input[1])
    s = [1, 2, 1, 3, 2]
    d = 3
    m = 2

    result = birthday(s, d, m)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()