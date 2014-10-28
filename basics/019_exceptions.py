#====================================================================================
# TOPIC: PYTHON - Exceptions
#====================================================================================
# NOTES: *  PYTHON Exceptions, Are RUN TIME ERRORS or EXECUTION TIME ERRORS
#        *  CODE that doesn't handle exceptions will compile, but when the un-handled 
#           exception is encountered then the program exits at the point of failure.
#        *  Handling exceptions in PYTHON is done using
#           "try: ... except ... finally" block
#        *  providing an ELSE with try: block 
#        *  Using PYTHON finally to execute code, irrespective of try-block raising
#           an exception.
#        *  PYTHON Custom user defined exceptions and exception handler
#        *  PYTHON, single try can have multiple exception handlers
#        *  PYTHON ignore exception, use pass keyword in the except section
# 
#====================================================================================
#
# FILE-NAME       : 019_exceptions.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   N/A
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2013
#
# DESC            : Python Exception handling
#
#====================================================================================

#####################################
# 1) Simple PYTHON Exception Example
#####################################

# We attempt to divide by zero, raising an exception
try:
    v = 1/0  # Trying to Divide By zero
except ZeroDivisionError:
    print("Tinitiate: Cannot Divide by ZERO")


##########################################
# 2) PYTHON Exception using ELSE Example
##########################################

# Using "else:" to complete normal execution and subsequent code in a try block
# We attempt to divide by zero, raising an exception
try:
    v = 1/1  # Trying to Divide By zero
except ZeroDivisionError:
    print("Tinitiate: Cannot Divide by ZERO")
else:
    print("Tinitiate: Execution completed successfully")


############################################
# 3) PYTHON Exception using FINALLY Example
############################################

# The finally block executes, whether the irrespective of try-block 
# raising an exception, This is useful to put code/functions 
# where such scenarios are needed

try:
    v = 1/1  # Trying to Divide By zero
except ZeroDivisionError:
    print("Tinitiate: Cannot Divide by ZERO")
finally:
    print("Tinitiate: THIS MESSAGE MUST BE PRINTED")


####################################
# 4) PYTHON User defined Exceptions
####################################

# Create an user defined exception
class tinitiate_exception(Exception):pass

# Block to test the user defined exception
try:
    raise tinitiate_exception
except tinitiate_exception:
    print("This is a user defined exception !")


################################################
# 5) PYTHON Multiple Exceptions in a single try
################################################

# Creating USER defined exceptions
class ti_exception_1(Exception):pass
class ti_exception_2(Exception):pass

# Block to test the user defined exception
try:
    raise ti_exception_1
except ti_exception_1: # Exception handler for user defined exception: ti_exception_1
    print("This is a user defined exception 1 Handler !")
except ti_exception_2: # Exception handler for user defined exception: ti_exception_2 
    print("This is a user defined exception 2 Handler !")


########################################
# 6) Python take no action on exception
#    Python ignore exception, use pass 
#    in the except section
########################################

try:
    a=1/0
except:
    pass

#====================================================================================
# END OF CODE
#====================================================================================
