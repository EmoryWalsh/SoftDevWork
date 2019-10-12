#Emory Walsh & Raymond Lee
#SoftDev1 pd1
#K18 -- Average
#2019-10-10

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#==========================================================

# FILL IN DATABASE
sql_create_courses_table = """ CREATE TABLE IF NOT EXISTS courses (
                                code TEXT, mark INTEGER, id INTEGER
                            );"""

c.execute(sql_create_courses_table)

with open("courses.csv", newline='') as csvCourses:
    reader = csv.DictReader(csvCourses)
    for row in reader:
        sql_insert_course = str.format("INSERT INTO courses VALUES ('{}', {}, {});", row['code'],  row['mark'], row['id'])
        #print(sql_insert_course)
        c.execute(sql_insert_course)

csvCourses.close()

sql_create_students_table = """ CREATE TABLE IF NOT EXISTS students (
                                name TEXT, age INTEGER, id INTEGER
                            );"""

c.execute(sql_create_students_table)

with open("students.csv", newline='') as csvStudents:
    reader = csv.DictReader(csvStudents)
    for row in reader:
        sql_insert_student = str.format("INSERT INTO students VALUES ('{}', {}, {});", row['name'],  row['age'], row['id'])
        #print(sql_insert_student)
        c.execute(sql_insert_student)

csvStudents.close()


#==========================================================
#==========================================================

def getID(name):
    find_id = str.format("SELECT id FROM students WHERE name = '{}';", name)
    result = c.execute(find_id)
    return result.fetchone()[0]

#Test Cases
print(getID('alison')) #10
print(getID('armin')) #3

def getName(ID):
    return 0

def getGrades(name):
    return 0






#create a table for the averages
create_stu_avg_table = """ CREATE TABLE IF NOT EXISTS stu_avg (
                                code TEXT, mark INTEGER, id INTEGER
                            );"""

c.execute(create_stu_avg_table)




q = '''SELECT name, students.id, mark
  FROM students, courses
  WHERE students.id = courses.id;'''

foo = c.execute(q)	#pretend c is a cursor

#print(foo.fetchall())

#==========================================================

db.commit() #save changes
db.close()  #close database
