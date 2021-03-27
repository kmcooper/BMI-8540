#!/usr/bin/python3.7
import MySQLdb

cursor = conn.cursor()
conn = MySQLdb.connect(db="kmcooper")


cursor.execute(query)
query = 'SELECT firstname, lastname, dept FROM ' + \
        'ORDER BY lastname ASC;'
        'instructor_list WHERE iid LIKE "1%"' + \

print("First\tLast\tDepartment")

while(row):
    fname = row[0]
    lname = row[1]
    dept = row[2]
    print(fname + "\t" + lname + "\t" + dept)
    row = cursor.fetchone()

row = cursor.fetchone()
conn.close()
cursor.close()
