#====================================================================================
# TOPIC: PYTHON - FILE IO
#====================================================================================
# NOTES: *  Using the OPEN function we can specify a FILE and the 
#           FILE-MODE(READ, WRITE, APPEND ..)
#        *  Python Reading and writing to files
#        *  Python Opening files
#        *  Python Reading files line by line
#        *  Python writing to files
#        *  Python writing to files line by line
#        *  Python writing Integers, Numbers, FLOAT, DOUBLE to files 
#        *  Python , working with File directory at OS level
#
#====================================================================================
#
# FILE-NAME       : 018_file_io.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   N/A
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2013
#
# DESC            : Python Working with files
#
#====================================================================================

# OPEN() Function, Reading files using PYTHON, Writing to files using PYTHON
# This is a built-in function used to wor with files
# USAGE: FILE_OBJECT = OPEN ("File_path\File_name",FILE_MODE)
# FILE_MODE: "r" READ Mode
#            "w" WRITE Mode (overwrite the file)
#            "a" APPEND Mode (Appends to a file)
#            "r+" READ and WRITE mode

# Required for OS operations
import os

####################################
# 1) Create a file using PYTHON    
####################################
# Create a file handler to create a new file in WRITE mode
# USAGE OF THE DOUBLE \\ is for ESCAPING the single "\"
new_file = open("c:\\tinitiate\\data.txt", "w")

new_file.write("Welcome to Tinitiate.COM\n")
new_file.write("Line 2 data\n")
new_file.write("Line 3 data\n")
new_file.close()


####################################
# 2) Opening and read file in python    
####################################

# Create a file handler to open the file in READ mode
# using the OPEN function
# The OPEN function returns a file object
# Pass File-Name and the access_mode (Read/Write/Append ..)
input_file = open("c:\\tinitiate\\data.txt","r")

# Assign the object "input_file" read function
# To a variable
var_text = input_file.read()

# Print the data in one go
print(var_text)

# Close the File stream handler
input_file.close()


########################################
# 3) readline(): Read file line by line 
########################################

# print the file line by line
print("Print the file line by line")

# ReOpen the file
input_file1 = open("c:\\tinitiate\\data.txt","r")

# While true enter into an infinite loop (we handle it by a break)
while True:
    curr_line = input_file1.readline() # Read line by line, to variable current line
    if not curr_line:
        break                          # Break if there is no line to read
    print(curr_line)                   # Print the current line


# Close the File stream handler
input_file1.close()


################################################################
# 4) readlines(): Read file line by line as a list of strings 
#    suffixed with newline character  "\n"
###############################################################

readlines_file = open("c:\\tinitiate\\data.txt","r")

# Prints the file contents as a LIST
print(readlines_file.readlines()) 

readlines_file.close()


#############################
# 5) write to file in PYTHON   
#############################
# The OPEN function returns a file object
write_file = open("c:\\data\\newdata.txt","w")

# Writing a VARIABLE to file
var_1 = "Data 1"
write_file.write(var_1)

# Close the FILE object in PYTHON
write_file.close


# WRITE mode overwrites the file,
# In order to add content, use APPEND mode "a"

# Writing a LIST to file in PYTHON
append_file = open("c:\\data\\newdata.txt","a")

list_1 = ['a', 'ZZ']
append_file.writelines(list_1)

# Writing a TUPLE to file in PYTHON
tuple_1 = ('A', 'b')
append_file.writelines(tuple_1)

# Writing a DICTIONARY to file in PYTHON
dictionary_1 = {'APPLE':'FRUIT', 'POTATO':'ROOT', 'OKRA':'VEGETABLE'}
append_file.writelines(dictionary_1)

# the close() function will close the file handler
# It flushes all unwritten data to the file
append_file.close


#######################################################
# 6) File and Folder Operations in PYTHON
#######################################################

# File operations will require a programmer to read file properties
# folder properties and more, heres the list of OS level operations
# from PYTHON, import when dealing with files.
# Import the OS module for these operations

# Create a directory in PYTHON [Use the Double \\ to escape one "\" ]
os.mkdir("c:\\tinitiate_test")

# Change the current working directory in PYTHON to "c:\tinitiate_test"
os.chdir("c:\\tinitiate_test")

# Prints the present working directory in PYTHON (PWD in UNIX)
print(os.getcwd())


os.chdir("c:\\")

# Remove a Directory in PYTHON
os.rmdir("c:\\tinitiate_test")

# rename a file in PYTHON
# rename c:\tinitiate\data.txt to c:\tinitiate\info.txt
os.rename("c:\\tinitiate\\data.txt", "c:\\tinitiate\\info.txt" )

# Delete a file from PYTHON
os.remove("c:\\tinitiate\\info.txt" )

#====================================================================================
# END OF CODE
#====================================================================================
