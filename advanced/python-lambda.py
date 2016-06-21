# Lambda Expressions
# These are used to create shortcuts for functions


##################
# NORMAL FUNCTION
##################

# Function to Add 2 Numbers
def Add2Nums(Num1, Num2):
    return Num1+Num2;


##################
# LAMBDA FUNCTION
##################
AddLda = lambda x,y: x+y

print(AddLda(1,3))


##################
# NORMAL FUNCTION
##################

# Function Identify if EVEN or ODD
def EvenOrOdd(Num1):
    if(Num1%2 == 0):
        return "EVEN";
    else:
        return "ODD";


##################
# LAMBDA FUNCTION
##################

# Lambda Identify if EVEN or ODD
EvenOrOddLda = lambda x: 'EVEN' if(x%2==0) else 'ODD'

print(EvenOrOddLda(12))



########################
# Functions with Lambda
########################

# MAP Function
# Applies a Function to a each element in a Sequence by iteration 

# USAGE: map(someFunction, someSequence)


# Simple Iteration with Lambda
sequence = [2, 3, 4, 5, 6]
y = list(map(lambda v : v * 5, sequence))

print(y)


# Using Function as a Sequence
def Add2(x):
        return (x+2)
def Add3(x):
        return (x+3)


MyFunctions = [Add2, Add3]

for num in range(5):
    data = list(map(lambda x: x(num), MyFunctions))
    print(data)


# FILTER Function
# Removes list of a values that dont match the criteria
evenList = list( filter((lambda x: x%2 == 0), range(10)))
print(evenList)



from functools import reduce

# REDUCE Function
# Import Reduce from functools in Python 3X
# Accepts a function and list of values to return a single value
# by processing the result over and over untill a single value remains

addData = reduce((lambda x,y:x+y),range(10))
print(addData)

mulData = reduce((lambda x,y:x*y),range(1,10))
print(mulData)







    