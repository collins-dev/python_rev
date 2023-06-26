#!/bin/python3
#print strings
print ("STRINGS IN PYTHON")

print ("Hello, World!")
print ("""this string 
runs multiple lines""")#triple line for multiple lines
print ("this string is "+"awsome")# We can add concatinate strings 
print ("\n")#new line
print ("Testing for the new line")
print ("\n")#new line
print ("MATHS IN PYTHON")
print (50 + 50)#add
print (50 - 50)#subtract
print (50 * 50)#multiply
print (50 / 50)#divide
print (50 + 50 - 50 * 50 / 50)#PEMDAS
print (50**2) #exponent
print (50 % 6) #modulo (remainder)
print (50 / 6) #float
print (50 // 6)#no remainder
print("\n")
print ("VARIABLES AND METHODS")
quote = "All is fair in love and war."
print(quote)

print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case
print(len(quote)) #counts characters


name = "Heath" #string
age = 33 #int
gpa = 3.7 #float - has a decimal

print(int(age))
print(int(30.1))
print(int(30.9)) #Will it round? No!

print("My name is " + name + " and I am " + str(age) + " years old.")


age +=1
print(age)

birthday = 1
age += birthday
print(age)
print ("\n")
print ("MORE EXAMPLES ON VARIABLES")
# Variable assignment
x = 10 # integer
name = "John" #string
is_true = True #Boolean


# Variable usage
y = x + 5
print(y)
print("Hello, " + name)
if is_true: #conditon 
    print("The condition is true")
print("\n")
# Built-in method example
numbers = [1, 2, 3, 4, 5]
length = len(numbers)
print("Length:", length)


# User-defined method example
def greet(name):
    print("Hello, " + name)


greet("Alice")

#Functions
print ("\n")
print ("FUNCTIONS")
print("Here is an example function:")

def who_am_i(): #this is a function without parameters
	name = "Heath"
	age = 30 #local variable
	print("My name is " + name + " and I am " + str(age) + " years old.")

who_am_i()	

#adding parameters
def add_one_hundred(num):#function with parameter
	print(num + 100)
	
add_one_hundred(100)

#multiple parameters
def add(x,y):
	print(x + y)

add(7,7)

def multiply(x,y):
	return x * y

multiply(7,7)
print(multiply(7,7))

def square_root(x):
	print(x ** .5)
	
square_root(64)


def nl():
	print('\n')
	
nl()

print("  ")
print ("BOLEAN EXPRESSION")
print("Boolean expressions:")

bool1 = True
bool2 = 3*3 == 9

bool3 = False
bool4 = 3*3 != 9
b = 3
print (type(b))

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))
print (type(bool2))

nl()

#Relational and Boolean operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >=7
less_than_equal_to = 7 <= 7

test_and = True and True #True
test_and2 = True and False #False
test_or = True or True #True
test_or2 = True or False #True

test_not = not True #False
print(x == y)   # Output: False
print(x < y)    # Output: True


# Boolean expressions
print(x < y and y > 0)    # Output: True
print(x < y or y < 0)     # Output: True
print(not (x == y))       # Output: True

nl()
print ("CONDITIONAL STATEMENTS")
#Conditional Statements
def drink(money):
	if money >= 2:
		return "You've got yourself a drink!"
	else:
		return "No drink for you!"

print(drink(3))
print(drink(1))


def alcohol(age,money):
	if(age >= 21) and (money >= 5):
		return "We're getting a drink!"
	elif (age >= 21) and (money < 5):
		return "Come back with more money."
	elif (age < 21) and (money >= 5):
		return "Nice try, kid!"
	else:
		return "You're too poor and too young!"
		
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(20,4))
nl()
print("TUPLES")
#Tuples - Do not change, ()
grades = ("a", "b", "c", "d", "f")

#(grades.pop, grades.append won't work - not mutable)

print(grades[1])
fruits = ("apple", "banana", "orange")
fruits2 = ("grape", "kiwi")


combined = fruits + fruits2
print(combined)         # Output: ("apple", "banana", "orange", "grape", "kiwi")


print(len(fruits))      # Output: 3


subtuple = fruits[1:3]
print(subtuple)         # Output: ("banana", "orange")
nl()
print ("LOOPS")
#For loops - start to finish of an iterate
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
	print(x)
	
#While loops - execute as long as true
i = 1

while i < 10:
	print(i)
	i += 1

nl()
print ("ADVANCED STRINGS")
#ADVANCED STRINGS

my_name = "Heath"
print(my_name[0]) #first letter
print(my_name[-1]) #last letter

sentence = "This is a sentence."
print(sentence[:4])

print(sentence.split()) #delimeter - default is a space

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, 'give me all your money'" #show example
quote = "He said, \"give me all your money\""
print(quote)

too_much_space = "                       hello          "
print(too_much_space.strip())

print("A" in "Apple") #returns true
print("a" in "Apple") #returns false - case sensitive

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #improved

movie = "The Hangover"
print("My favorite movie is {}.".format(movie))
print("My favorite movie is %s" % movie)
print(f"My favorite movie is {movie}")
nl()
print ("DICTIONARIES")

#DICTIONARIES - key/value pairs {}

drinks = {"White Russian": 7, "Old Fashion": 10, "Lemon Drop": 8} #drink is key, price is value
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
employees['Legal'] = ["Mr. Frond"] #adds new key:value pair
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]}) #adds new key:value pair
print(employees)

drinks['White Russian'] = 8
print(drinks)

print(drinks.get("White Russian"))
