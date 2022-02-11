#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.


def gradingStudents(grades):
    # Write your code here
    rounded_grades = []
    for i in range(len(grades)):
        if grades[i] >= 38:
            next_multiple = math.ceil(grades[i] / 5) * 5
            if (next_multiple - grades[i]) < 3:
                rounded_grades.append(next_multiple)
            else:
                rounded_grades.append(grades[i])
        else:
            rounded_grades.append(grades[i])
            
    return rounded_grades
                

if __name__ == '__main__':

    sample_input = [73, 67, 38, 33]
    print('sample input:', sample_input)

    result = gradingStudents(sample_input)

    print('rounded grades:', result)


