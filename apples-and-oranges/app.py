#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple_count = 0
    orange_count = 0
    #print('a', a, 'b', b, 's', s, 't', t)
    for i in range(len(apples)):
        #print('apple', apples[i])
        pos = apples[i] + a
        #print('pos', pos)
        if pos >= s and pos <= t:
            apple_count += 1
            #print('apple_count', apple_count)
    
    for i in range(len(oranges)):
        #print('orange', oranges[i])
        pos = oranges[i] + b
        #print('pos', pos)
        if pos >= s and pos <= t:
            orange_count += 1
            #print('oranges_count', orange_count)
    
    print(apple_count)
    print(orange_count)
    

if __name__ == '__main__':

    sample_first_input = ['7', '11']
    s = int(sample_first_input[0])

    t = int(sample_first_input[1])
    # first_multiple_input = input().rstrip().split()

    # s = int(first_multiple_input[0])

    # t = int(first_multiple_input[1])

    sample_second_input = ['5', '15']
    a = int(sample_second_input[0])

    b = int(sample_second_input[1])

    # second_multiple_input = input().rstrip().split()

    # a = int(second_multiple_input[0])

    # b = int(second_multiple_input[1])

    sample_third_input = ['3', '2']
    m = int(sample_third_input[0])

    n = int(sample_third_input[1])

    # third_multiple_input = input().rstrip().split()

    # m = int(third_multiple_input[0])

    # n = int(third_multiple_input[1])

    apples = [-2, 2, 1]
    oranges = [5, -6]

    # apples = list(map(int, input().rstrip().split()))

    # oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
