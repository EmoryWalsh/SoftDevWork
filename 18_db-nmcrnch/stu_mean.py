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

def getID(name): #find the id given the name
    find_id = str.format("SELECT id FROM students WHERE name = '{}';", name)
    result = c.execute(find_id)
    return result.fetchone()[0]

#Test Cases
#print(getID('alison')) #10
#print(getID('armin')) #3

def getName(ID): #find the name given the id
    find_name = str.format("SELECT name FROM students WHERE id = '{}';", ID)
    result = c.execute(find_name)
    return result.fetchone()[0]

#Test Cases
#print(getName(10)) #'alison'
#print(getName(3)) #'armin'

def getGrades(ID): #find grades given ID
    find_grades = str.format("SELECT mark FROM courses WHERE id = '{}'", ID)
    result = c.execute(find_grades)
    return result.fetchall()

#Test Cases
#print(getGrades(10)) #(85, 80)
#print(getGrades(3)) #(55, 85)

def average(ID): #averages the grades of student with ID
    grades = getGrades(ID)
    sum = 0
    for grade in grades:
        sum += grade[0]
    #print(sum)
    return sum/len(grades)

#Test Cases
print(average(10)) #82.5
print(average(3)) #70




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
