#===================================================================================
# TOPIC: PYTHON -  Lists
#===================================================================================
#
# NOTES: *  List is a compound and versatile type.
#        *  Lists can have elements (values) of mixed data types or same data type 
#        *  Lists are written as comma separated elements enclosed in square 
#			brackets, list = ['data']
#        *  List index starts from ZERO
#        *  Lists support conditional and iterative operations 
#        *  Lists have built-in functions and methods similar to strings
#
#===================================================================================
#
# FILE-NAME       :  004_lists.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   N/A
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2013
#
# DESC            : Lists in Python and operations on lists 
#
#===================================================================================

#================================
# 1) LISTS: Creating and Viewing
#================================
# List example
MyNumbersList = [1, 100, 9, 99]
MyStringList  = ["A", 'b', 'Hello', "This"]

# An Empty list
MyList = []

# Adding elements to an empty list
MyList = set([1 ,'a'])

# a Compound elements based list (compound = elements with various data types, here 
# numbers and string)
CompoundList = [1, 100, 'a', 'ZZ']

# Printing a List
print (CompoundList)

# Printing List element by index
# Index starts from 0 to .. n
print (CompoundList[0])

# Creating LIST of LISTS

#==================================================
# 2) LIST: Adding, modifying and removing elements 
#==================================================

# An empty list
TestList = []
print('Elements of TestList: ', TestList) # OUTPUT: Elements of TestList: []

# Add elements to a list, using set()
TestList = [1, 2, 3, 4]
print('Elements of TestList: ', TestList) # OUTPUT: Elements of TestList: [1, 2]

# Modify elements in a list, using the position index of the element
TestList[1] = 100

#This changes the SECOND element [ index(1) ] of the list from 2 to 100
print('Elements of TestList: ', TestList) 
# OUTPUT: Elements of TestList:  [1, 100, 3, 4]

# Removing elements from a list
del TestList[1] # This removed the SECOND element [ index(1) ] of the list: 100
print('Elements of TestList: ', TestList) # OUTPUT: Elements of TestList:  [1, 3, 4]

# Slicing a LIST using indexes
masterList = [1, 2, 3, 4, 5, 6]

# Print a part of the list, Slicing a list using ":" operator
# Also note this Ignores the last INDEX.
print('Slicing a list using ":" operator ' ,masterList[1:5]) 
# OUTPUT:  Slicing a list using ":" operator  [2, 3, 4, 5]

# Print for a index to end of string
print('Print masterList elements from index 2 (position(3) to end of string '
       , masterList[2:]);

# Update elements in a list for a given range
masterList [1:4] = ['New1', 'New2', 'New3']
print('Updated masterList: ' ,masterList)


#=====================
# 3) LIST: Operators 
#=====================

ListOps = [1, 2] 
# Repetition, Printing the List "n" times
print(ListOps*3) # OUTPUT: [1, 2, 1, 2, 1, 2]

# Concatenation, adding another list to the existing list,
# in this case the same list
print(ListOps + ListOps) # OUTPUT: [1, 2, 1, 2]

# Checking if an element is present or not, Using "in" operator
print ('Does element "2" exists in list is ListOps? ', 2 in ListOps) # OUTPUT: True

# Compare lists
list1 = [1, 2]
list2 = [1, 2]
print('The condition list1 == list2 is: ', list1 == list2) # OUTPUT: True 

# Looping and printing over a list
mixedList = [1, 100, 'a', 'ZZ']

# Using for loop to print elements of mixedList 
for element in mixedList: print(element)



#============================
# 4) LIST: Built-in functions 
#============================
newList = [3, 2, 5, 1, 4, 4]

# Length of the LIST
print(len(newList))   # OUTPUT: 5
print(len([1, 2, 3])) # OUTPUT: 3

# get Min and Max element in the list
print(min(newList))  # OUTPUT: 1
print(max(newList))  # OUTPUT: 5
print(sum(newList))  # OUTPUT: 19

#============================
# 5) LIST: Built-in methods 
#============================

# Sort a list
newList.sort()
print(newList)  # OUTPUT: [1, 2, 3, 4, 4, 5]

# Count the occurrences on the passed element
print(newList.count(4)) # OUTPUT: 2

# INSERT element before specified index
# usage list.insert(INDEX-VALUE, newElement)
newList.insert(1, 'A')
print(newList) # OUTPUT: [1, 'A', 2, 3, 4, 4, 5]

# Removes the first occurrence of the specified element
# Throws error if element not found
newList.remove(4);
print(newList) # OUTPUT: [1, 'A', 2, 3, 4, 5]

# Reverses the LIST
newList.reverse()
print(newList) # OUTPUT: [5, 4, 3, 2, 'A', 1]

# POP an element out of the list# removes the first or the last element in the list
newList.pop()
print(newList) # OUTPUT: [5, 4, 3, 2, 'A']
newList.pop(0)
print(newList) # OUTPUT: [4, 3, 2, 'A']

# Clear a list
newList.clear()
print(newList) # OUTPUT: []

# Also reassign list to newList = [], will clear the list.

#===================================================================================
# END OF CODE
#===================================================================================
