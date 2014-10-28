#===================================================================================
# TOPIC: PYTHON - Convert among Dictionary, Tuple, List
#===================================================================================
#
# NOTES: *  Its essential in many cases to convert complex types to simple types,
#           this script demonstrates some examples.  
#        *  Convert TUPLE to LIST.
#        *  Convert DICTIONARY to LIST of TUPLES.
#        *  Convert DICTIONARY to LIST of elements,(Convert DICTIONARY to elements). 
#
#===================================================================================
#
# FILE-NAME       : 007_convert_dict_tuple_list.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   N/A
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2013
#
# DESC            : Convert among Dictionary, Tuple, List 
#
#===================================================================================

# Converting a TUPLE to a LIST
tuple1 = (1, 2, 3, 4, 5)
tup_list  = list(tuple1)

print(tuple1) # OUTPUT: (1, 2, 3, 4, 5)
print(tup_list)  # OUTPUT: [1, 2, 3, 4, 5]

# Convert DICTIONARY to LIST
dictionary1 = {1:'A', 2:'B', 3:'C'}

# This creates a list of TUPLES
dict_list   = list(dictionary1.items())

print(dictionary1) # OUTPUT: {1: 'A', 2: 'B', 3: 'C'}
print(dict_list)  # OUTPUT: [(1, 'A'), (2, 'B'), (3, 'C')]


#Convert DICTIONARY to LIST of elements
finalDictionaryBigList=[]

# Loop through the dict_list to create individual tuples
for tuples in dict_list: 
    #Capture individual tuples
    IndividualTuple = tuples
    #Convert individual tuples to lists
    IndividualTuplesList = list(IndividualTuple)
    # Append the IndividualTuplesList to a final List
    finalDictionaryBigList = finalDictionaryBigList + IndividualTuplesList

# Print the final flat list from the dictionary
print(finalDictionaryBigList)

#===================================================================================
# END OF CODE
#===================================================================================
