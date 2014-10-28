#====================================================================================
# TOPIC: PYTHON - Execute OS Commands
#====================================================================================
# NOTES: *  Python provides ways to execute OS commands
#        *  Using "OS" Module "system" function
#        *  Using the "subprocess.call"
#
#====================================================================================
#
# FILE-NAME       : 017_os_commands.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   N/A
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2013
#
# DESC            : Python Executing OS Commands
#
#====================================================================================

################################################
# 1) Executing OS command using the OS Module  
################################################

import os
import subprocess

OScommand = "echo Tinitiate.com"
os.system(OScommand)

################################################
# 2) Executing OS command using subprocess.call  
################################################

subprocess.call(["echo", "Tinitiate.com"])

#====================================================================================
# END OF CODE
#====================================================================================
