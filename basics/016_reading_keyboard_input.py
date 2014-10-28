#====================================================================================
# TOPIC: PYTHON - User Input
#====================================================================================
# NOTES: *  Python provides various methods to read user input.
#        *  Reading single line user input using input (raw_input)
#        *  Reading multi line user input using input (raw_input)
#        *  Reading python file command line arguments
#
#====================================================================================
#
# FILE-NAME       : 016_reading_keyboard_input.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   N/A
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2013
#
# DESC            : Python reading user input, passing arguments to python scripts
#
#====================================================================================

# This is required to read python file command line arguments
import sys;

##################################################
# 1) Reading single line user input using "input"
##################################################

l_UserInput = input("Enter text and press enter: ")
print ("text entered " + l_UserInput)

# The input entered is captured upto the "enter key"

###########################################################
# 2) Reading multi line user input using input (raw_input)
###########################################################

# enter multi-line input and to end make sure to include ":END"
l_UserInput = ""
terminate_str = ":END"  # Identifier to indicate the end of input

print("Enter multiline user input, Please enter the string ':END'")
print("to terminate reading input")
while True:
    data = input()
    if data.strip() == terminate_str:
        break
    l_UserInput += "%s\n" % data

print(l_UserInput)

#################################################
# 3) Reading python file command line arguments
#################################################

# The sys.argv returns all the arguments to this list.
commandline_args_list = sys.argv

print(commandline_args_list)

# Call the program using 
# $ python 016_reading_keyboard_input.py argument1 argument2
# The FIRST element in the list is the file path and name  

#====================================================================================
# END OF CODE
#====================================================================================
