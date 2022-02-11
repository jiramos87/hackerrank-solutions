#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

# Sample input 0: 07:05:45PM
# Sample output 0: 19:05:45

def timeConversion(s):
    # Write your code here
    ampm_hours = s[0:2]
    ampm_minutes = s[3:5]
    ampm_seconds = s[6:8]
    ampm = s[8:10]
    
    military_hours = ''
    military_minutes = ''
    military_seconds = ''
    
    if ampm == 'AM':
        military_hours = str(ampm_hours)
        if military_hours == '24' or military_hours == '12':
            military_hours = '00'
        military_minutes = str(ampm_minutes)
        military_seconds = str(ampm_seconds)
        
    elif ampm == 'PM':
        military_hours = str(int(ampm_hours) + 12)
        if military_hours == '24':
            military_hours = '12'
        military_minutes = str(ampm_minutes)
        military_seconds = str(ampm_seconds)
        
    return military_hours + ':' + military_minutes + ':' + military_seconds
        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
   s = input('Input AM/PM to convert to military time:')

   result = timeConversion(s)

   print('military time:', result)

    