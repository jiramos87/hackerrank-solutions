#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    season_min = scores[0]
    season_max = scores[0]
    min_record_count = 0
    max_record_count = 0
    for score in scores:
        if score < season_min:
            season_min = score
            min_record_count += 1
        if score > season_max:
            season_max = score
            max_record_count += 1
    return [max_record_count, min_record_count]
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 9

    scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]

    result = breakingRecords(scores)
    print('scores:', scores)
    print('min_record_count - max_record_count')
    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()