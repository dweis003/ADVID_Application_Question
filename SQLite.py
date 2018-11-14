# python imports
import csv
import sqlite3
import sys

#CSV File Names
data_filename_1 = 'CITY.csv'
data_filename_2 = 'RECORDS.csv'

#create DB in memory
conn1 = sqlite3.connect(':memory:')
c1 = conn1.cursor()

#CREATE RECORDS AND CITIES TABLES
c1.execute("""CREATE TABLE RECORDS(ID CHAR(16) NOT NULL, Name CHAR(150), Phone INT(15), 
            Address TEXT(500), Time_Stamp TIMESTAMP, PRIMARY KEY(ID))""")
c1.execute("""CREATE TABLE CITIES(City_Name TEXT(500), PRIMARY KEY(City_Name))""")
#-------------------------------------------------------------------------------    
#storage for rows in CITY CSV
City = []

#load data from CITIES CSV
with open(data_filename_1) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
         Cities = row[0]
         City.append(Cities)
         

i = 0
while i < len(City):
    c1.execute("""INSERT INTO CITIES VALUES (?)""", (City[i],))
    conn1.commit
    i += 1
   

#-------------------------------------------------------------------------------    
#storage for rows in RECORDS CSV
ID = []
name = []
phone = []
address = []
time = []

    
#load data from RECORDS CSV
with open(data_filename_2) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        times = row[4]
        addresss = row[3]
        phones = row[2]
        names = row[1]
        IDs = row[0]

        time.append(times)
        address.append(addresss)
        phone.append(phones)
        name.append(names)
        ID.append(IDs)
        

i = 0
while i < len(ID):
    c1.execute("""INSERT INTO RECORDS (ID, Name, Phone, Address, Time_Stamp) VALUES (?, ?, ?, ?, ?)""", (ID[i], name[i], phone[i], address[i], time[i]))
    conn1.commit
    i += 1
    
   
#------------------------------------------------------------------------------- 
print ("CITIES DATABASE")

c1.execute("""SELECT * FROM CITIES""")
obj1 = c1.fetchall()
rowcount=len(obj1)
x = 0
while x < rowcount:
    print obj1[x][0]
    x=x+1

print("\n")
#-------------------------------------------------------------------------------
print ("RECORDS DATABASE")

c1.execute("""SELECT * FROM RECORDS""")
obj2 = c1.fetchall()
rowcount=len(obj2)
y = 0
while y < rowcount:
    print obj2[y][0], obj2[y][1], obj2[y][2], obj2[y][3], obj2[y][4]
    y=y+1
#-------------------------------------------------------------------------------
print("\n")
#SOLUTION TO QUESTION 4 PART A
print("#SOLUTION TO QUESTION 4 PART A")
c1.execute("""SELECT strftime('%H',Time_Stamp) as "Hour",  count(strftime('H',Time_Stamp)) 
            FROM RECORDS 
            Where ID LIKE 'A%'
            Group By Hour
            ORDER BY Hour ASC""")
obj3 = c1.fetchall()
rowcount=len(obj3)
y = 0
while y < rowcount:
    print obj3[y][0], obj3[y][1]
    y=y+1
#-------------------------------------------------------------------------------
print("\n")
#SOLUTION TO QUESTION 4 PART B
print("#SOLUTION TO QUESTION 4 PART B")
c1.execute("""SELECT * FROM RECORDS WHERE strftime('%Y %m %d',Time_Stamp) = '2018 11 06' """)
obj4 = c1.fetchall()
rowcount=len(obj4)
y = 0
while y < rowcount:
    print obj4[y][0], obj4[y][1], obj4[y][2], obj4[y][3], obj4[y][4]
    y=y+1
#-------------------------------------------------------------------------------
print("\n")
#SOLUTION TO QUESTION 5
print("#SOLUTION TO QUESTION 5")
c1.execute("""Select C.City_Name FROM CITIES C
            WHERE  EXISTS
                (SELECT * FROM RECORDS WHERE Address LIKE '%' || C.City_Name || '%')
            GROUP BY C.City_Name ORDER By C.City_Name ASC """)
obj5 = c1.fetchall()
rowcount=len(obj5)
y = 0
while y < rowcount:
    print obj5[y][0]
    y=y+1
    
#CLOSE DATABASE
c1.close
conn1.close()