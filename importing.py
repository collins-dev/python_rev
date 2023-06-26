#!/bin/python3
#IMPORTIN MODULES - 
print ("IMPORTING MODULES IN PYTHON")
import sys
from datetime import datetime as dt #import with alias
print (sys.version)

print(dt.now())
def nl():
	print("\n")
nl()
import math


result = math.sqrt(25)
print(result)   # Output: 5.0
nl()
from math import sqrt


result = sqrt(25)
print(result)   # Output: 5.0

nl()
import math as m #alias


result = m.sqrt(25)
print(result)   # Output: 5.0
nl()
from math import *#importing all functions and variables


result = sqrt(25)
print(result)   # Output: 5.0
