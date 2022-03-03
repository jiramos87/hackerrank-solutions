#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    
    sorted_arr = sorted(arr)
    sightings_count = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0
    }
    
    for i in range(0, len(sorted_arr)):
        sightings_count[sorted_arr[i]] += 1
         
    value_ordered_counts = dict(sorted(sightings_count.items(), key=lambda item: item[1]))
    
    values_ordered = list(value_ordered_counts.values())
    values_ordered.reverse()
    max_values = []
    for i in range(0, len(values_ordered)):
        if i == 0:
            max_values.append(values_ordered[i]) 
        elif i != 0:
            if values_ordered[i] == values_ordered[i - 1]:
                max_values.append(values_ordered[i])
            elif values_ordered[i] != values_ordered[i - 1]:
                break
            
    key_ordered = list(value_ordered_counts.keys())
    key_ordered.reverse()
    max_types = []
    for i in range(len(max_values)):
        max_types.append(key_ordered[i])
        
    return(sorted(max_types)[0])
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #arr_count = int(input().strip())

    arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]

    result = migratoryBirds(arr)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
