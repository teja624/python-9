#===================================================================================
# TOPIC: PYTHON - OBJECT ORIENTED PROGRAMMING OOP CLASS INHERITANCE
#===================================================================================
# NOTES: *  PYTHON - CLASS INHERITANCE.
#        *  Inheritance, is the process of accessing Functions and Members of a 
#           class (parent) from a child class.
#        *  To inherit parent class, pass the parent class name as a parameter to 
#			the child class.
#        *  Simple one parent one child inheritance.
#        *  Python Multiple inheritance.
#        *  Inheritance overriding
#        *  Inheritance using SUPER
#        *  Private variables,Note there is no Private functions / methods in PYTHON 
#
#===================================================================================
#
# FILE-NAME       : 024_oop_inheritance.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   N/A
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2013
#
# DESC            : Python Class inheritance
#
#===================================================================================

#################################################################
# 1) Inheritance demo, with one parent class and one child class
#################################################################

# Create a PARENT class, which will be inherited by a child class
class ParentClass():
    Parentvar1 = "parentVariable Value" 
    def parentFunction(self):
        print("This is a message from ParentClass.parentFunction")


#This is a clhld class that inherits ParentClass,
# SYNTAX is to call the parent class as a parameter to the child class
class ChildClass(ParentClass):
    ChildVar1 = "parentVariable Value" 
    def childFunction(self):
        print("This is a message from ChildClass.childFunction")


# Create an object of the Child Class
cObj = ChildClass()


# CALL CHILDCLASS and PARENTCLASS methods from the child object
cObj.childFunction()
cObj.parentFunction()


#################################################################################
# 2) Multiple Inheritance demo, with multiple parent classes and one child class
#################################################################################

#Create one more parent class, to demonstrate multiple parent inheritance
class anotherParent():
    "This is another parent-level class"
    def newParentFunction(self):
        print("This is a message from the anotherParent.newParentFunction")


# Class that inherits from 2 parents
class GrandChild(ParentClass,anotherParent):
    "This is a GrandChild class"

gcObj = GrandChild()

gcObj.newParentFunction()
gcObj.parentFunction()


#############################
# 3) Inheritance Overriding
#############################
# * Overriding is all about NAMES of Functions and Variables.
# * Overriding is the process of using the same NAME for
#   Functions and variables, In the child class, which 
#   inherits same named Functions and variables from 
#   a parent class.
# * Python provides syntax to OVERRIDE the parent functions


#Demonstration of OverRiding
class xParent():  # Create a Parent Class
    "This is a Parent Class"
    var1 = "Parent-Test"
    def func1(self):
        print("This is parent class")


# Child class that inherits the xParent
# and uses the names same as the ones from the parent class
class xChild(xParent):
    "This is the Child class"
    var1 = "Child-Test"
    def func1(self):
        print("This is child class")


objA = xChild()
objA.func1()    # This should print message from the child class


#################################
# 4) Inheritance super function
#################################
# * SUPER is useful for accessing inherited methods from parent class
# that have been overridden in the child class. 

class Parent1():    # Parent Class with a method
    "A parent class to demonstrate the SUPER"
    def func1(self):
        print("This is a message from Parent1.func1")

class Child1(Parent1):    # Child Class with a method
    "A child class to demonstrate the SUPER"
    def func1(self):
        print("This is a message from Child1.func1")

    # This is a func2, calling the Parent1 classes method.
    def func2(self):
        super(Child1,self).func1()


# Create an objec to demonstrate SUPER()
supObject = Child1()
supObject.func1()
supObject.func2()

#######################
# 5) Private variables
#######################
# * Create Private variables using a double underscore prefix
#   for the variable names
# * 

class private_test():
    "This is a class to demonstrate the Private variables"
    __private_var1 = "This is a Private Value"

    public_var = "This is a public value"


# Create an object of the provate_test class
ObjPrv = private_test()


# The following code throws an error as the private variable 
# is not accessible from outside the class
# print(ObjPrv.__private_var1)


# print the public variable of the class
print(ObjPrv.public_var)


#===================================================================================
# END OF CODE
#===================================================================================
#TAGS: PYTHON - OBJECT ORIENTED PROGRAMMING OOP CLASS INHERITANCE
#      PYTHON SUPER Inheritance Overriding
#      python Multiple Inheritance
#===================================================================================
