#===================================================================================
# TOPIC: PYTHON -  Dictionary
#===================================================================================
#
# NOTES: *  Dictionaries are associative arrays, unordered set of key:value pairs.
#        *  Dictionaries declaration is in flower brackets
#			 d = {'Key1' : 'value1', 'Key2' : 'value2'} 
#        *  Dictionaries keys can be any immutable type (Strings and Numbers)
#        *  Dictionaries support conditional and iterative operations 
#        *  Dictionaries have built-in functions and methods similar to strings
#
#===================================================================================
#
# FILE-NAME       : 006_dictionary.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   N/A
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2013
#
# DESC            : Dictionaries in Python and operations on Dictionaries. 
#
#===================================================================================

#=====================================
# 1) DICTIONARY: Creating and Viewing
#=====================================

# Key is String in dict1
dict1 = {'key1':'Value1', 'key2':'Value2', 'key3':'Value3'}
print(dict1) # OUTPUT: {'key1': 'Value1', 'key2': 'Value2', 'key3': 'Value3'}

eats = {'APPLE':'FRUIT', 'POTATO':'ROOT', 'OKRA':'VEGETABLE'}
print(eats) # OUTPUT: {'OKRA': 'VEGITABLE', 'POTATO': 'ROOT', 'APPLE': 'FRUIT'}

# Print a value of a key 
print(eats['POTATO']) # OUTPUT: ROOT

#===========================================
# 2) DICTIONARY: Modify and Delete elements 
#===========================================

# Change a Keys value
eats['POTATO'] = 'VEGETABLE'
print(eats['POTATO']) # OUTPUT: VEGETABLE

# remove one element, key-name: POTATO
del eats['POTATO']

# remove all elements
eats.clear()

# delete dictionary
del eats

#print(eats) # This will result in error.

# Recreate eats
eats = {'APPLE':'FRUIT', 'POTATO':'ROOT', 'OKRA':'VEGETABLE'}

# Get all Keys, returns a list
print(eats.keys())
eats.keys


#=================================================
# 3) DICTIONARY: Advanced operations on dictionary 
#=================================================

# Read all elements of a dictionary
for key, value in eats.items():
    print(key, value)
# OUTPUT
#    APPLE FRUIT
#    OKRA VEGETABLE
#    POTATO ROOT

#===================================================================================
# END OF CODE
#===================================================================================
