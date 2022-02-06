#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    between_numbers = 0
    a_count = 0
    b_count = 0
    print('a:', a, 'b:', b, 'len(a):', len(a), 'len(b):', len(b))
    for i in range(1, 101):
        print('i:', i)
        for j in range(0, len(a)):
            print(j)
            if (i % a[j] == 0):
                a_count += 1
        for k in range(0, len(b)):
            print(k)        
            if (b[k] % i == 0):
                b_count += 1
        
        print('a_count:', a_count, 'b_count:', b_count)
        if (a_count == len(a)):
            print('a yes')
        else:
            print('a no')
        if (b_count == len(b)):
            print('b yes')
        else:
            print('b no')
        if (a_count == len(a) and b_count == len(b)):
            print('between_numbers += 1')
            between_numbers += 1
            print(between_numbers)
        a_count = 0
        b_count = 0
            
    return between_numbers
                

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #first_multiple_input = input().rstrip().split()
    first_multiple_input = [2, 3]
    second_multiple_input = [2, 4]
    third_multiple_input = [16, 32, 96]

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, second_multiple_input))

    brr = list(map(int, third_multiple_input))

    total = getTotalX(arr, brr)
    print('total:', total)

    #fptr.write(str(total) + '\n')

    #fptr.close()