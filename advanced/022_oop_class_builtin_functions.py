#===================================================================================
# TOPIC: PYTHON - Class Built-in Functions
#===================================================================================
# NOTES: *  Object Oriented Programming, in PYTHON
#        *  Constructors in PYTHON
#        *  "self" in Python
#
#===================================================================================
#
# FILE-NAME       : 022_oop_class_builtin_functions.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   N/A
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2013
#
# DESC            : Python Class built-in attributes
#
#===================================================================================

#######################################
# 1) Create a CLASS with a constructor
#    built-in function (__init__)
#######################################

# CONSTRUCTOR:1) A function, that is executed automatically when 
#                the object of the class is created
#             2) Tt is created using the syntax __init__(self, arguments...)
#             3) The first argument is "self" always
#             4) Once a constructor is created all the other functions
#                MUST have the first parameter as "self"
#             5) "self": is a reference to the object instance

class Tinitiate:
    'This is a brief note about the class, This is the TINITIATE Class'
    # a class Variable
    ti_var   = 100

    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    # a class function,"self" holds all the attributes and functions of this class
    # so a reference to any class member can be done easily
    # in here instead of passing var1, var2 we just pass 
	# self.( its part of the SYNTAX! )
    def print_member_attributes(self):
        "This class function prints the varibles var1 and var2 from the constructor"
        print("Variables from the CONSTRUCTOR var1: ",self.var1 ," var2:",self.var2)

# OBJECT of the CLASS Tinitiate
tiObject = Tinitiate(1,2)

# Call the CLASS's function
tiObject.print_member_attributes()


# Class with constructor with an ARRAY (unspecified number) of parameters
class ManyValues(object):
    def __init__(self, *args):
        self.items = tuple(args)
        print(self.items)

# This will Print the input parameters as there is a print in the constructor
tObj = ManyValues('A','B','C')


#############################################
# 2) PYTHON class built-in function
#    __iter__, This returns a "loop of data"  
#############################################

# Create a class with the __init__ method 
class IterTest():
    def __init__(self, classList):
        self.classList = classList

    def __iter__(self):
        return (i for i in self.classList)

# Create an object of the Class with a input TUPLE 
t_Obj = IterTest(('JAVA','C++', 'SCALA'))


# The result is a loop of elements.
# now iterate over the result
for data in t_Obj:
    print(data)


#===================================================================================
# END OF CODE
#===================================================================================
