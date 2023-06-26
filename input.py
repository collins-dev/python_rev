#!/bin/python3
import math
name = input ("Enter your name : ")
drink = input ("What is your favoite drink: ")
print ("Hello "+name+ "! Have a "+drink+".")

age = input("Enter your age: ")
age = int(age)  # Convert the input to an integer


print("You will be " + str(age + 1) + " next year.")


#mini calculator

x = float(input("Give me a number: "))
o = input("Give me an operator: ")
y = float(input("Give me yet another number: "))

if o == "+":
	print(x + y)
elif o == "-":
	print(x - y)
elif o == "/":
	print(x / y)
elif o == "*":
	print(x * y)
elif o == "**" or o == "^":
	print(x ** y)
elif o == "//":
	print(x//y)
else:
	print("Unknown operator.")
