# >>TITLE - Python Modules

# >>BREADCRUMB - PYTHON,MODULES


# >>HEADLINE - Python Modules, __init__.py, __main__.py, __all__, __main__ explained
# >>AUTHOR - Venkata Bhattaram / TINITIATE.COM
# >>DATEPUBLISHED - 2016-07-24


# >>DESC<<
# Python Modules, __init__.py, __main__.py, __all__, __main__ explained
# >><<


# >>KEYWORDS<<
# What is are Python Modules, __init__.py, __main__.py, __all__, __main__ explained
# >><<


# >>POINTS<<
# + Pyhton Modules are collection python files grouped under one name
# + To use a module, it must be "imported" using the "import" clause
# + __init__py is an empty file that needs to be placed in a folder 
#   so that the FolderName becomes the "Module Name" and the files in the 
#   folder or Module become "importable" in other files. 
# + __all__ This is a special "directive"(a string "__all__") that is placed in  the
#   __init__.py file, If this is done then when we import the module, Python loads 
#   all the modules to the memory.
#
# + __main__.py
#
# + __main__ 
#  
# >><<



# >>CODE-TITLE - Python Create Module
# >>CODE-NOTES<<
# Steps to create a Module
# 1. Create a folder with your module name, say "Website" 
#    [Dont use spaces or spl characters in the folder name]
# 2. Add your python files, say SignUp.py, Search.py, Reports.py
# 3. Create an empty file with name __init__.py
#    This makes the folder a module.
# 
# ref. the folder Structure below
#
#  |-- Website [Folder Name]
#  |
#  |---- __init__.py
#  |---- SignUp.py
#  |---- Search.py
#  |---- Reports.py
# 
# >><<
# >>CODE-ALL-OS<<

# usage in other python programs
from Website import SignUp, Search, Reports

# Lets assume there are fuctions Function1, Function2, Function3
# In each of the files SignUp, Search, Reports respectively.
SignUp.Function1()
Search.Function2()
Reports.Function3()

# >><<



# >>CODE-TITLE - Python what is __all__ ?
# >>CODE-NOTES<<
# Steps to create a Module
# 1. __all__ is a list of python files in a module
# 2. __all__ list is part of the __init__.py file 
# 3. The files part of the __all__ list will be loaded when a 
#    " from Website import * " call is made.
# 4. If there is no __all__ then the " from Website import * "
#    will not load all the files (SignUp.py, Search.py, Reports.py)
# 
# ref. the folder Structure below
#
#  |-- Website [Folder Name]
#  |
#  |---- __init__.py
#  |---- SignUp.py
#  |---- Search.py
#  |---- Reports.py
# 
# >><<
# >>CODE-ALL-OS<<
# __init__.py code

__all__ = [SignUp, Search, Reports]

# >><<



# >>CODE-TITLE - Python How to access files from other modules or folders ?
# >>CODE-NOTES<<
#
# Importing files from different folder in Python ?
# 1. Consider there are 2 folders or modules 
#    
#  |-- Website [Folder Name]
#  |
#  |---- __init__.py
#  |---- SignUp.py
#  |---- Search.py
#  |---- Reports.py
#
#  
#  |-- Offers [Folder Name]
#  |
#  |---- __init__.py
#  |---- DailyOffers.py
#  |---- WeeklyOffers.py
#  |---- CashBacks.py
# 
# 2. To call WeeklyOffers.py from search.py
# 
# >><<
# >>CODE-ALL-OS<<

# Python access files from other modules or folders
import sys
sys.path.insert(0, sys.path.insert(0, r'c:\path\to\Offers'))

from Offers import WeeklyOffers

# >><<



# >>CODE-TITLE - Python execute module with __main__.py
# >>CODE-NOTES<<
#
# 1. A Python program is run by the command line
#    python myfile.py
#    
#  |-- Website [Folder Name]
#  |
#  |---- __init__.py [This indicates the folder is a module]
#  |---- __main__.py [Executes when "python website.py" is called at command line]
#  |---- SignUp.py
#  |---- Search.py
#  |---- Reports.py
#

# 2. We can execute the module, (Code resides in the __main__.py file)
# 
# >><<
# >>CODE-ALL-OS<<

# Run the Module as a file, This executes the contents of the __main__.py file

$ python Website

# >><<



# >>CODE-TITLE - Python the __main__ builtin variable
# >>CODE-NOTES<<
#
# 1. __main__ is a built in variable that holds the current executing program.
# 2. __name__ is a built in varaible that holds the current program
# 2. Consider 2 files pgm1.py and pgm2.py
# 
# >><<
# >>CODE-ALL-OS<<

# File: pgm1.py
# ---- Code Start ----
var1_pgm1 = "Variable 1 of pgm1"
var2_pgm1 = "Variable 2 of pgm1"

def mainFunc():
    if(__name__ == '__main__'):
        print("This code is run as 'python pgm1.py'")
    else:
        print("This code is run as 'import pgm1'")

# ---- Code end ----


# File:  pgm2.py
import pgm1
#
print(pgm1.mainFunc)



# Run the programs as following
# 1. python pgm1.py
#    OUTPUT: 
#
#
# 2. python pgm2.py
#    OUTPUT: 
#
# >><<


# >>TAGS<<
# Python Modules, __init__.py, __main__.py, __all__, __main__ explained
# >><<
