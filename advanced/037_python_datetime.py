# >>NOTES<<
# %a  Locale’s abbreviated weekday name.
# %A  Locale’s full weekday name.      
# %b  Locale’s abbreviated month name.     
# %B  Locale’s full month name.
# %c  Locale’s appropriate date and time representation.   
# %d  Day of the month as a decimal number [01,31].    
# %f  Microsecond as a decimal number [0,999999], zero-padded on the left
# %H  Hour (24-hour clock) as a decimal number [00,23].    
# %I  Hour (12-hour clock) as a decimal number [01,12].    
# %j  Day of the year as a decimal number [001,366].   
# %m  Month as a decimal number [01,12].   
# %M  Minute as a decimal number [00,59].      
# %p  Locale’s equivalent of either AM or PM.
# %S  Second as a decimal number [00,61].
# %U  Week number of the year (Sunday as the first day of the week)
# %w  Weekday as a decimal number [0(Sunday),6].   
# %W  Week number of the year (Monday as the first day of the week)
# %x  Locale’s appropriate date representation.    
# %X  Locale’s appropriate time representation.    
# %y  Year without century as a decimal number [00,99].    
# %Y  Year with century as a decimal number.   
# %z  UTC offset in the form +HHMM or -HHMM.
# %Z  Time zone name (empty string if the object is naive).    
# %%  A literal '%' character.
# >><<

# >>CODE<<
import time;

localtime = time.localtime(time.time())
print("Current System Time :", localtime)

localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)


######################################
# DATE and TIME to User Defined Format 
######################################
import datetime

today = datetime.datetime.today()

# YYYYMMDD
format1 = "%Y%m%d"

# Print Format
s = today.strftime(format1)
print(s)


# DD-MON-YYYY
format2 = "%d-%b-%Y"

# Print Format
s = today.strftime(format2)
print(s)


# DD-MON-YYYY HH24:MI:SS
format3 = "%d-%b-%Y %H:%M:%S"

# Print Format
s = today.strftime(format3)
print(s)

# >><<

###################
# STRING to Date
#################### Convert String to Date
# Convert String to Date Time
l_date_time_string="2016-06-24 16:00:00"

l_datetime=datetime.datetime.strptime(l_date_time_string, "%Y-%m-%d %H:%M:%S").date()
print(l_datetime)


#################################
# Date Comparisions and Checking
#################################

# Convert String to Date Time in format3
# DD-MON-YYYY HH24:MI:SS
l_date_string1 = "2016-06-24 16:00:00"
format3        = "%Y-%m-%d %H:%M:%S"

# Get Todays Date Time in format3
s = today.strftime(format3)

# Convert string s back to date time in format3
t1=datetime.datetime.strptime(s, format3).date()

# Create a new time in format format3
t2=datetime.datetime.strptime(l_date_string1, format3).date()

# Comparision
if(t1 > t2):
    print(t1," is Greater than ",t2)
else:
    print(t1," is Less than ",t2)


# >>TITLE - Python Date and Time
