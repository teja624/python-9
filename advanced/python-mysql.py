import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='tinitiate', db='mysql')

cur = conn.cursor()


# Clear Contents

# Create A Data Base
# Executing DDL (Data Definition Language)

# Create a table
cursor = conn.cursor()
try:
    cursor.execute("drop table ti_test");
except:
    pass;


# Python pymysql MYSQL Create a table with multiple data types
cursor.execute(" create table ti_test ( col1 int, col2 varchar(100), col3 date, col4 text );" )


# python pymysql MYSQL Alter Table to add primary key
cursor.execute("alter table ti_test add constraint ti_test_pk primary key (col1);")


# Python pymysql MYSQL Insert data into the table
cursor.execute("insert into ti_test values (1, 'Test', curdate(), 'THIS IS CLOB DATA .........');")
cursor.execute("insert into ti_test values (2, 'Test2', curdate(), 'THIS IS CLOB DATA .........');")


# python pymysql MYSQL Update data in the table
cursor.execute("update ti_test set col2 = 'DATA CHANGE' where col1 = 1;")


# python pymysql MYSQL delete data in the table
cursor.execute("delete from ti_test where col1 = 2;")


# Commit changes
conn.commit()


# Reading data from Oracle using cx_Oracle
# reading multiple datatypes and print to screen
cursor.execute("SELECT col1, col2, col3, col4 FROM ti_test;")

# Prints the Row count of the cursor
print(cursor.rowcount)

# Fetches a Single Row
rowdata = cursor.fetchone()

print(rowdata)

# use fetchall() to get the list of row data
for l_col1, l_col2, l_col3, l_col4 in cursor.fetchall():
    print("l_col1: ", l_col1)
    print("l_col2: ", l_col2)
    print("l_col3: ", l_col3)
    print("l_col4: ", l_col4)


# Drop table after test
print("drop table ti_test")
cursor.execute("drop table ti_test")


print(cursor.description)


cursor.close()
conn.close()
