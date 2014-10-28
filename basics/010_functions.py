#===================================================================================
# TOPIC: PYTHON - FUNCTIONS
#===================================================================================
#
# NOTES: *  Function is a code block, that can be called once or multiple times.
#      	    Functions can be reused and provide code modularity, they can accept 
#			input parameters to be used with in its code body.
#        *  In Python create functions using keyword "def" function-name  
#           def myFunction myFunction and parameters(or arguments) in curved  
#			brackets def myFunction(): and a colon to end :
#        *  An optional first line can be used to add a Documentation String,a brief  
#           comment line to describe the function's functionality and parameters, 
#           there are utilities that read this line to generate documentation 
#			automatically. and a "return" to end the function. 
#        *  Sample function syntax without arguments def myFunctionName():
#        *  Sample function syntax with one argument def myFunctionName(input):
#        *  Sample function syntax with multiple arguments 
#			def myFunctionName(input1, input2):
#        *  Note that python interpreter looks for code indentation make sure     
#           next line is indented by atleast 1 whitespace.
#        *  Loops in functions and if..else in functions
#        *  sample usage of List with functions, Tuple with function, 
#			Dictionary with function
#
#===================================================================================
#
# FILE-NAME       : 010_functions.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   N/A
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2013
#
# DESC            : Demonstration of Python functions  
#
#===================================================================================

##################################################################
# 1) Python Function with no input parameters and no return value
##################################################################

def function_no_input_args_no_return():
   "This is a function without any input values or return values"
   print("This message is from the function: function_no_input_args_no_return")
   return
# End of function code: function_no_input_args_no_return

# Calling the function ( Can be called as many times as needed)
function_no_input_args_no_return()

# Calling the function again, to demonstrate reusability
function_no_input_args_no_return()
#OUTPUT:
#    This message is from the function: function_no_input_args_no_return
#    This message is from the function: function_no_input_args_no_return


##################################################################
# 2) Python Function with input parameters and a return value
##################################################################

def function_add_2_numbers(number1, number2):
    "This is a function with 2 input parameters and returning the sum"
    return number1 + number2
# End of function code: function_add_2_numbers

# Calling the function with input parameters
# Capture the return value into a variable
sum_value = function_add_2_numbers(1,2)  # These are the input parameters

# print the return value
print("The value returned from the function and inputs:function_add_2_numbers(1,2) is:", sum_value)
#OUTPUT:
#The value returned from the function and inputs: function_add_2_numbers(1,2) is:  3


##########################################################
# 3) Python Function with loop and conditional constructs
##########################################################

def function_with_constructs(in_string, in_number):
    "This function demonstrates use of various built-in constructs"
    # Loops in function
    # print in_string 5 times
    for c in range(5):
        print(in_string)

    # Checks if the in_number is even or odd
    if in_number%2 == 0:
        print(in_number,' is even.')
    elif in_number%2 != 0:
        print(in_number,' is odd.')
    return
# End of function code: function_with_constructs

# Calling the function function_with_constructs
function_with_constructs("Python", 20)
#OUTPUT:
#    Python
#    Python
#    Python
#    Python
#    Python
#    20  is even.

#################################################
# 4) Python Function with a LIST input parameter
#################################################

# This is a demonstration to convert a list separate stringList and numberList
# accepts in_list a mixed list and in_split_type accepts values "string" or "number"
def function_seperate_list_into_strings_and_numbers(in_list, in_split_type):
    "This is a function separates list into a stringlist and numberlist"
    number_list = []
    string_list = []
    for c in in_list:
        if c.isdigit():
            number_list.append(c)
        else:
            string_list.append(c)

    if in_split_type == "string":
        return string_list;
    elif  in_split_type == "number":
        return number_list;
# End of function code: function_seperate_list_into_strings_and_numbers

# Calling the function function_seperate_list_into_strings_and_numbers
# Passing number as the split parameter
return_list =function_seperate_list_into_strings_and_numbers(['1','A', '2', '3','B', 'c'] ,"number")

#Returns all the numbers in the supplied list
print('The returned list: ', return_list) 

# Passing string as the split parameter
return_list =function_seperate_list_into_strings_and_numbers(['1','A', '2', '3','B', 'c'] ,"string")

# Returns all the strings in the supplied list
print('The returned list: ', return_list) 
#OUTPUT:
#         The returned list:  ['1', '2', '3']
#         The returned list:  ['A', 'B', 'c']

##################################################
# 5) Python Function with a TUPLE input parameter
##################################################
def function_convert_tuple_to_list_of_strings_and_numbers(in_tuple, in_split_type):
    "This is a function separates tuple into a stringlist and numberlist based on split type"
    number_list = []
    string_list = []
    work_list = list(in_tuple) 
    for c in work_list:
        if c.isdigit():
            number_list.append(c)
        else:
            string_list.append(c)

    if in_split_type == "string":
        return string_list;
    elif  in_split_type == "number":
        return number_list;
# End of function code: function_convert_tuple_to_list_of_strings_and_numbers

# Calling the function function_convert_tuple_to_list_of_strings_and_numbers
# Passing string "number" as the split parameter
return_list =function_seperate_list_into_strings_and_numbers(('1','A', '2', '3','B', 'c'),"number")
# Returns all the numbers in the supplied TUPLE			  
print('The returned list: ', return_list) 
# Passing string "string" as the split parameter
return_list =function_seperate_list_into_strings_and_numbers(('1','A', '2', '3','B', 'c'),"string")
# Returns all the strings in the supplied TUPLE
print('The returned list: ', return_list) 
#OUTPUT:
#         The returned list:  ['1', '2', '3']
#         The returned list:  ['A', 'B', 'c']

######################################################
# 6) Python Function with a DICTIONARY input parameter
######################################################

def function_convert_dictionary_to_list_of_strings_and_numbers(in_dictionary, in_split_type):
    "This is a function separates dictionary into lists of keys and values"
    if in_split_type == "keys":
        return in_dictionary.keys()
    elif  in_split_type == "values":
        return in_dictionary.values()
# End of function code: function_convert_dictionary_to_list_of_strings_and_numbers

# Calling the function function_convert_dictionary_to_list_of_strings_and_numbers
# Passing string "keys" as the split parameter
return_list = function_convert_dictionary_to_list_of_strings_and_numbers({1:'A',2:'B', 3:'C'}, "keys")
# Returns all the keys in the supplied dictionary
print('The returned list: ', return_list) 
# Passing string "values" as the split parameter
return_list = function_convert_dictionary_to_list_of_strings_and_numbers({1:'A',2:'B', 3:'C'}, "values")
# Returns all the values in the supplied dictionary
print('The returned list: ', return_list) 
#OUTPUT:
#         The returned list:  ['1', '2', '3']
#         The returned list:  ['A', 'B', 'c']


#===================================================================================
# END OF CODE
#============ LABELS === 
#
#===================================================================================
