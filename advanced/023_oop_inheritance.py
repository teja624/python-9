#===================================================================================
# TOPIC: PYTHON - CLASS DECORATOR
#===================================================================================
# NOTES: *  PYTHON - CLASS DECORATOR
#        *  Creating Static and class methods
#        *  Python supports static methods: These are methods(functions)
#           that do not require an object.
#        *  staticmethod  is callable without instantiating the class
#                        It’s definition is immutable via inheritance.
#        *  classmethod is a method that gets passed the class it was called on,
#                       or the class of the instance it was called on, as first
#                       argument. This is useful when you want the method to be a
#                       factory for the class: since it gets the actual class it was
#                       called on as first argument, you can always instantiate the
#                       right class, even when subclasses are involved.
#
#===================================================================================
#
# FILE-NAME       : 023_oop_inheritance.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   N/A
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2013
#
# DESC            : Python Class inheritance
#
#===================================================================================

class tinitiate:
    "Class to demonstrate @classmethod and @staticmethod Decorations"

    # Using the "@classmethod"  
    @classmethod
    def class_function(cls, x):
        print(cls, x)

    @staticmethod
    def static_function(x):
        print(x)


# Create an object of the class tinitiate
obj = tinitiate()


# Call the "CLASS_FUNCTION" using the object
obj.class_function("Class Object Test")

# Call the "STATIC_FUNCTION" using the object
obj.static_function("Static Object Test")


# Call the "STATIC_FUNCTION" directly without the object
tinitiate.static_function("Static Test")

# Call the "CLASS_FUNCTION" directly without the object
tinitiate.class_function("Class Test")


#===================================================================================
# END OF CODE
#===================================================================================
