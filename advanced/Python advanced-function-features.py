# >>TITLE - Python python-advanced-function-features


# >>BREADCRUMB - PYTHON,python-advanced-function-features.py


# >>HEADLINE - Python advanced-function-features.py
# >>AUTHOR - Venkata Bhattaram / TINITIATE.COM
# >>DATEPUBLISHED - 2016-07-07


# >>DESC<<
# Python python-advanced-function-features.py
# >><<


# >>KEYWORDS<<
# Python python-advanced-function-features.py
# >><<


# >>POINTS<<
# + Decorators are callable objects that takes a function as its input parameter.
# + Decorators are ideal for extending the behavior of functions that 
#   we don't want to modify.
# + Could be used for auditing a Function, running analytics
# >><<


# >>FILE-NAME - python-advanced-function-features.py
# >>DEPENDANT-FILES - N/A



# >>CODE-TITLE - Simple Function
# >>CODE-NOTES<<
# Demonstration of a simple function
# >><<
# >>CODE-ALL-OS<<
# A Simple Function
# -----------------
def Add2Nums(Num1,Num2):
    return Num1+Num2;

# Print the variable
print(Add2Nums(1,2))
# >><<
# >>OUTPUT<<
# 3
# >><<
 

 
# >>CODE-TITLE - Nested Function
# >>CODE-NOTES<<
# Demonstration of a function inside a function, or a nested function
# >><<
# >>CODE-ALL-OS<<
# A Nested Function
# -----------------
# Outer Function "add2numsAndFive"
def add2numsAndFive(num1,num2):
    
    # Inner Function or Nested Function "Add5"
    def Add5(num):
        return num+5;

    return Add5(num1+num2)
# Func-END

# Call the Function add2numsAndFive
print(add2numsAndFive(1,2))
# >><<
# >>OUTPUT<<
# 8
# >><<



# >>CODE-TITLE - Passing function as a parameter to another function
# >>CODE-NOTES<<
# Demonstration of a Passing function as a parameter to another function
# >><<
# >>CODE-ALL-OS<<   
# Passing a Function as a Parameter to Another Function
# -----------------------------------------------------
# Function that "add5" adds 5 to input number`
def add5(num1):
   return num1+5

   
def addSpl(num1, num2):
    return num1+num2
    
    
# Function that Accepts another 
# function as an input parameter
# Parameter Name is "func"
def addTwoNums(func):
    num1 = 1
    num2 = 2
    
    # Return the parameter, by passing another parameter "num1"
    if func == 'add5':
        return func(num1)
        
    elif func == 'appSpl':
        return func(num1, num2):

# Calling "addTwoNums" function with "add5" function 
# as input parameter

print(addTwoNums(add5))

print(addTwoNums(addSpl))
# >><<
# >>OUTPUT<<
# 6
# >><<



# >>CODE-TITLE - Function returns another function as output
# >>CODE-NOTES<<
# Demonstration of a Function returns another function as output
# >><<
# >>CODE-ALL-OS<<
# Function returns another function as output
# -------------------------------------------
def AddNumWith5(Num1):
    
    # Nested Function
    def Add5():
        return Num1+5

    # Return the "Add5" function
    return Add5

# Capture the Returned function into add_5,
# And add_5 is an object not a variable
add_5 = AddNumWith5(5)

# Printing add_5() is printing as a function
print(add_5())  # OUTPUT: 10

# Printing add_5 is printing as a variable
print(add_5)    # OUTPUT: Some Object Address
# >><<
# >>OUTPUT<<
# 10
# Some Object Address
# >><<



# >>CODE-TITLE - Wrappers and Decorators
# >>CODE-NOTES<<
# - A Functions "Functionality" can be enhanced without changing the function
# - The easy option to enhance a function,
#   - Change the Function
#   - Call the Function as an Inner Funciton in another function called 
#     the wrapper or outer function.
#   - Using a Deocorator
# >><<
# >>CODE-ALL-OS<<

# Parent Function
# This is the function whose function should be enhanced
# ------------------------------------------------------
def AddTWONums(Num1,Num2):
    return Num1+Num2;

    
# Enhance Functionality by a wrapper function
# Change the parent functions functionality
# Call the funciton "AddTWONums" inside the wrapper
# --------------------------------------------------
def add3Nums_1(Num1,Num2,Num3):

    # Call the parent function inside the add3Nums_1
    return AddTWONums( AddTWONums(Num1,Num2) ,
                       Num3)

# Called the add3Nums_1 function
print(add3Nums_1(1,2,3))


# >>TAGS -  python-advanced-function-features
