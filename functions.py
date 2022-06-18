# module function

import math
# # functions in math module
print(dir(math))

# here we arew selecting specific square root function
from math import sqrt
print(sqrt(16))

# # to select all the fucntions
from math import *

#################################################################

# user-defined functions

def add (first,second):
    print(first + second)

add(1,5)

