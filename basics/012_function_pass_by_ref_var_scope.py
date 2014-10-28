#===================================================================================
# TOPIC: PYTHON - FUNCTION ARGUMENTS PASS BY REFERENCE and VALUE, VARIABLE SCOPE
#===================================================================================
#
# NOTES: *  Variables defined inside a function have local scope
#        *  Variables defined outside a function have global scope.
#        *  Global variables can be accessed inside functions as well.
#        *  Function arguments in python are passed by reference, any parameter 
#            value changed inside the function is reflected outside the call too.
#        *  The parameter passed in is actually a reference to a variable (but  
#           the reference is passed by value)
#        *  Caution, when changing arguments by reference make sure to copy the 
#           contents to a local variable in the function, or else the outer variable
#      	    might be overwritten !
#
#===================================================================================
#
# FILE-NAME       : 012_function_pass_by_ref_var_scope.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   N/A
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2013
#
# DESC            : Demonstration of Python function argument types  
#
#===================================================================================

################################
# 1) Global and Local Variables
################################

# Global variable
cool_variable = 'GlobalValue'

def myFunction():
    cool_variable = 'LocalValue'
    print('Value of cool_variable inside function: ', cool_variable)
# End of function code:  myFunction

# Make a call to myFunction
myFunction()
print('Value of cool_variable outside function: ', cool_variable) 


#######################
# 2) Pass by Reference
#######################

# Create a source list
source_list = ['A', 'B', 'C']

def function_pass_by_reference(in_list):
    print('function_pass_by_reference says Input List: ', in_list)

    # Changing the input by appending a value to in_list
    in_list.append('D')
    print('function_pass_by_reference says changed List: ', in_list)
# End of function code:  function_pass_by_reference


print('Before passing reference to function, source_list: ', source_list)

# Passing the "source_list" and NOT A COPY of the "source_list"
function_pass_by_reference(source_list)
print('After passing reference to function, source_list: ', source_list)

# OUTPUT
#    Before passing to function, source_list:  ['A', 'B', 'C']
#    Input List:  ['A', 'B', 'C']
#    changed List:  ['A', 'B', 'C', 'D']
#    After passing to function, source_list:  ['A', 'B', 'C', 'D']


#######################
# 3) Pass by Value
#######################

# Create a source list
source_list_2 = ['A', 'B', 'C']

def function_pass_by_value(in_list):
    print('function_pass_by_value says Input List: ', in_list)

    # Reassigning a local value, [pass by value example]
    in_list =[1, 2, 3, 4]
    print('function_pass_by_value says changed List: ', in_list)
# End of function code:  function_pass_by_value


print('Before passing by value to function, source_list: ', source_list_2)

# Passing the "source_list" and NOT A COPY of the "source_list"
function_pass_by_value(source_list_2)
print('After passing by value to function, source_list: ', source_list_2)

# OUTPUT
#    Before passing to function, source_list:  ['A', 'B', 'C']
#    Input List:  ['A', 'B', 'C']
#    changed List:  ['A', 'B', 'C', 'D']
#    After passing to function, source_list:  ['A', 'B', 'C', 'D']

#===================================================================================
# END OF CODE
#============ LABELS === 
#
#===================================================================================
