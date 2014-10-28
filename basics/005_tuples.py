#===================================================================================
# TOPIC: PYTHON -  Tuples
#===================================================================================
#
# NOTES: *  Tuple is a immutable(Cannot be changed) group of elements.
#        *  Tuple declaration is in curly brackets t = ('data') 
#        *  Tuple is a compound and versatile type.
#        *  Tuples can have elements (values) of mixed data types or same data type 
#        *  Tuple index starts from ZERO
#        *  Tuples support conditional and iterative operations 
#        *  Tuples have built-in functions and methods similar to strings
#
#===================================================================================
#
# FILE-NAME       :  005_tuples.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   N/A
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2013
#
# DESC            : Tuples in Python and operations on tuples.
#
#===================================================================================

#=================================
# 1) TUPLES: Creating and Viewing
#=================================
tuple1 = (1, 2, 3, 4)
tuple2 = ('A', 'b', 1, 2)

print(tuple1)
print(tuple2)

#====================================================
# 2) TUPLES: Adding, modifying and removing elements 
#====================================================

# Tuples are immutable and cannot be changed
# We cannot change individual elements of tuple
# tuple1[0]=99 # This will result in an error as TUPLES are immutable
# we can overwrite a tuple though
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)

# Easier option for updating parts of tuple are creating 
#  new tuples with parts of existing ones
#  Create a Tuple with elements 2,3,4 from tuple1
tuple3=tuple1[1:4]
print(tuple3)

#===========================
# 3) TUPLES: Deleting Tuples 
#===========================
del tuple3
# print(tuple3) # This will throw an error, as this TUPLE doesnt exist

#======================
# 4) TUPLES: Operators 
#======================
# creating a new tuple with appending tuples or concatenating tuples
tuple33 = tuple1 + tuple2
print('tuple33: ', tuple33) #OUTPUT: tuple33:  (1, 2, 3, 4, 5, 'A', 'b', 1, 2)

tuple34 = (1,2,3) + ('a','b','c') 
print('tuple34: ', tuple34) #OUTPUT: tuple34:  (1, 2, 3, 'a', 'b', 'c')

# Check if element exists
print(1 in tuple34) #OUTPUT: True

for LOOP_COUNTER in (1, 2, 3): print(LOOP_COUNTER) 
# OUTPUT: 1
#         2
#         3

# Multiplication of the tuple values, duplication (multiple times)
print(tuple1*3) # OUTPUT: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Slicing in Tuples
tuple99 = (11, 22, 33, 44, 55, 66)
print('tuple99: ', tuple99) #OUTPUT: tuple99: (11, 22, 33, 44, 55, 66)

# SLice from Index 1 to ONE element before Index 3
print(tuple99[1:3]) # OUTPUT: (22, 33)

# Negative numbers in Index counts from reverse (-1 is last element) 
print(tuple99[-1])  # OUTPUT: 66

# Slice [n:] with no upper bound prints from nth index to end of index(last element)
print(tuple99[2:])  # OUTPUT: (33, 44, 55, 66)


#============================
# 5) TUPLES: Built-in methods 
#============================

# COUNT method counts the occurrences of an element in the tuple
print((1,1,2,3).count(1)) # OUTPUT: 2 

# MIN and MAX element of the TUPLE
print(min(tuple99), max(tuple99)) # OUTPUT: 11 66

# LENGTH of tuple
print(len(tuple99))

# SUM of all ELEMENTS
print(sum(tuple99)) # OUTPUT: 231

#===================================================================================
# END OF CODE
#===================================================================================
