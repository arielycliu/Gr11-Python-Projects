<<<<<<< HEAD
"""
STUDENT INFORMATION SYSTEM

Ariel Liu, Janice An

The Woodlands Secondary School

Read data from studentData.json

Main.py: collective programs, calling each separate function, ask users for what program they would like to run
addStudent function: take in current data, return new data with new student to write to json (uses the add method in class)
updateStudent function: take in current data, return updated data (uses update method in class)
searchStudentID function: takes in current data, gets a dict of the student data, displays the attributes of the student (uses search method)
searchStudentLast function: looks up student last name in given data, print out ID and name of results
markChange: changes a previous course mark in transcript(vs update function which adds courses)

Add-ons:
- markChange method changes a previously assigned mark (not to be mistaken with addStudent's ability to add new courses to a transcript)
- program does not crash due to improper inputs
"""

import rep
import addStudent
import searchStudentId
import searchStudentLast
import markChange
import updateStudent

# Read data from Json
file = rep.Repository()
try:
    data = file.read()  # returns a list of dictionaries of students
except:
    data = {}

# Ask user which program they want to run
while True:
    print("Which program would you like to run?")
    print("add   update   searchID   searchLastName   changeMark")
    print("On the other hand, enter exit to stop and update changes")
    ans = input().lower().replace(" ", "")
    if ans == "exit": break

    elif ans == "add":
        dataDict = addStudent.add_student(data)
        file.write(dataDict)  # Write the data into Json
        print("Student added to database")

    elif ans == "update":
        dataDict = updateStudent.update_student(data)
        file.write(dataDict)  # Write the data into Json
        print("Student data updated")

    elif ans == "searchid":
        searchStudentId.search_student_id(data)
        print("Exiting studentID search")

    elif ans == "searchlastname":
        searchStudentLast.search_student_last(data)
        print("Exiting student last name search")

    elif ans == "changemark":
        dataDict = markChange.mark_change(data)
        file.write(dataDict)  # Write the data into Json
        print("Student mark changed")

    else:
        print("I'm sorry I don't understand...\n")

    print("  ." * 16)
    print("\n")
=======
"""
STUDENT INFORMATION SYSTEM

Ariel Liu, Janice An

The Woodlands Secondary School

Read data from studentData.json

Main.py: collective programs, calling each separate function, ask users for what program they would like to run
addStudent function: take in current data, return new data with new student to write to json (uses the add method in class)
updateStudent function: take in current data, return updated data (uses update method in class)
searchStudentID function: takes in current data, gets a dict of the student data, displays the attributes of the student (uses search method)
searchStudentLast function: looks up student last name in given data, print out ID and name of results
markChange: changes a previous course mark in transcript(vs update function which adds courses)

Add-ons:
- markChange method changes a previously assigned mark (not to be mistaken with addStudent's ability to add new courses to a transcript)
- program does not crash due to improper inputs
"""

import rep
import addStudent
import searchStudentId
import searchStudentLast
import markChange
import updateStudent

# Read data from Json
file = rep.Repository()
try:
    data = file.read()  # returns a list of dictionaries of students
except:
    data = {}

# Ask user which program they want to run
while True:
    print("Which program would you like to run?")
    print("add   update   searchID   searchLastName   changeMark")
    print("On the other hand, enter exit to stop and update changes")
    ans = input().lower().replace(" ", "")
    if ans == "exit": break

    elif ans == "add":
        dataDict = addStudent.add_student(data)
        file.write(dataDict)  # Write the data into Json
        print("Student added to database")

    elif ans == "update":
        dataDict = updateStudent.update_student(data)
        file.write(dataDict)  # Write the data into Json
        print("Student data updated")

    elif ans == "searchid":
        searchStudentId.search_student_id(data)
        print("Exiting studentID search")

    elif ans == "searchlastname":
        searchStudentLast.search_student_last(data)
        print("Exiting student last name search")

    elif ans == "changemark":
        dataDict = markChange.mark_change(data)
        file.write(dataDict)  # Write the data into Json
        print("Student mark changed")

    else:
        print("I'm sorry I don't understand...\n")

    print("  ." * 16)
    print("\n")
>>>>>>> 8f5946147103d092ce4bb4ed0a3808b334187ed2
