#===================================================================================
# TOPIC: PYTHON - Class Objects
#===================================================================================
# NOTES: *  Object Oriented Programming, in PYTHON
#        *  Class is a collection of FUNCTIONS and Variables 
#			(lists, tuples, dictionaries)
#        *  Objects are instantiation of classes (reference of a class instance)
#        *  Class creation and usage 
#
#===================================================================================
#
# FILE-NAME       : 020_oop_classes.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   N/A
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2013
#
# DESC            : Python Classes and objects
#
#===================================================================================


###########################
# 1) Create a CLASS
###########################
class Tinitiate:
    'This is a brief note about the class, This is the TINITIATE Class'
    # a class Variable
    ti_var   = 100
    # a class list
    ti_list  = ["a","b","c"]
    # a class tuple
    ti_tuple = ("x","y","z")
    # a class dictionary
    ti_dictionary = {"1":"A", "2":"b", "3":"c"}

    # a class function
    def ti_function(self):
        "This is a class function"
        print("This is a message from the TINITIATE Class ti_function")


###################
# 2) Using a Class
###################
# Create an object of the class 
tinObject = Tinitiate()

# use the Class variables/lists..
print(tinObject.ti_var)
print(tinObject.ti_list)
print(tinObject.ti_tuple)
print(tinObject.ti_dictionary)

# Call the the class function
tinObject.ti_function() # This will print the message from the function

# Create another object of the class
tObject = Tinitiate()

# Call the the class function
tObject.ti_function()

#===================================================================================
# END OF CODE
#===================================================================================
