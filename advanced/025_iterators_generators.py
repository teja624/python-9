#===================================================================================
# TOPIC: PYTHON - ITERATORS and GENERATORS
#===================================================================================
# NOTES: * PYTHON ITERATORS are constructs for loops, 
#        * The biggest advantage of ITERATORS is there is no boundry, 
#          the loop can be closed in any part of the program (or function)  
#        * PYTHOn Generators: They return an iterator,
#          Any function with a keyword "yield" makes the function a generator
#        * "yield" is similar to a "return" except that the state of the function
#          is on hold and using the "next()" will move the function return value
#
#===================================================================================
#
# FILE-NAME       : 025_iterators_generators.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   N/A
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2013
#
# DESC            : Python Iterators and Generators
#
#===================================================================================

###############
#1) ITERATORS
###############

# This is a simple for loop
for value1 in [1,2,3,4,5]:
    print(value1)

# Using an Iterator
# Create some data
value2 = [1,2,3,4,5]

# Create an iterator using the iter function
itr = iter(value2)


# Call the print to display the next value
print(itr.next())
print(itr.next())
print(itr.next())
print(itr.next())

# From "An Introduction to Python"
# Each time next() is called, the generator resumes where it 
# left-off (it remembers all the data values and which 
# statement was last executed). 


# This gives an error are there are no more elements
#print(itr.next())

# the biggest advantage is there is no "end loop", see for loop indentation
# we can add more code inbetween the ".next()" providing some flexibility


###################
# 2) Generators
###################
#Function converted to a generator using yield

def func1():
    yield 22
    yield 33
    yield 44


# Call the function as an iterator
myIter = func1()


# print the state of the function as an iterator
print(myIter.next())
print(myIter.next())
print(myIter.next())


# Put the yield in a loop in the function to use in more scenarios
def func2():
    for c1 in [1,2,3,4,5]:
        yield c1


# Call the function as an iterator
myIter = func2()


# print the state of the function as an iterator
print(myIter.next())
print(myIter.next())
print(myIter.next())
print(myIter.next())
print(myIter.next())


#===================================================================================
# END OF CODE
#===================================================================================
#TAGS: Python Iterators python Generators
#===================================================================================
