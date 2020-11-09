<<<<<<< HEAD
# Janice
import student

# Update Program
def update_student(data):
    # Make sure Student ID is valid
    while True:
        print("Please input the student ID you are searching for: ")
        searchStudentID = input()
        try:
            s = student.StudentInfo(searchStudentID, "L", "A", 1, {}, 'true')
            if int(searchStudentID) > len(data):  # Make sure under the dict index of students -1 or no
                raise ValueError('This student doesn\'t exist')
        except ValueError as error:
            print("Hmmm... {}".format(error))
        else:
            break

    # fetches the student's information
    studentDict = s.search_student_id(data)
    s = student.StudentInfo(searchStudentID, studentDict["_lastName"], studentDict["_firstName"],
                            studentDict["_gradeLevel"], studentDict["_transcript"], str(studentDict["_registered"]))

    print("Are you updating your transcript? Y or N")
    transAns = input().lower()
    if transAns == "n" or transAns == "no":
        while True:
            print("What part of the student's information would you like to modify?")
            print("lastname    firstname    grade    registered")
            subjectToChange = input().lower().replace(' ', '')

            print("\nWhat is the new value for {}".format(subjectToChange))
            newValue = input()
            try:
                # Check if the value is valid in student
                dataDict = s.update_student(subjectToChange, newValue, data)
            except ValueError as error:
                print("Hmmm... {}\n".format(error))
            else:   break
    elif transAns == 'y' or transAns == 'yes':
        # Make sure it's not a course that already exists
        print("Current transcript: {}".format(studentDict["_transcript"]))
        dataDict = s.update_student("transcript", studentDict["_transcript"], data)
    else:
        print("Sorry I don't understand")
        return data

    return dataDict # return the data
=======
# Janice
import student

# Update Program
def update_student(data):
    # Make sure Student ID is valid
    while True:
        print("Please input the student ID you are searching for: ")
        searchStudentID = input()
        try:
            s = student.StudentInfo(searchStudentID, "L", "A", 1, {}, 'true')
            if int(searchStudentID) > len(data):  # Make sure under the dict index of students -1 or no
                raise ValueError('This student doesn\'t exist')
        except ValueError as error:
            print("Hmmm... {}".format(error))
        else:
            break

    # fetches the student's information
    studentDict = s.search_student_id(data)
    s = student.StudentInfo(searchStudentID, studentDict["_lastName"], studentDict["_firstName"],
                            studentDict["_gradeLevel"], studentDict["_transcript"], str(studentDict["_registered"]))

    print("Are you updating your transcript? Y or N")
    transAns = input().lower()
    if transAns == "n" or transAns == "no":
        while True:
            print("What part of the student's information would you like to modify?")
            print("lastname    firstname    grade    registered")
            subjectToChange = input().lower().replace(' ', '')

            print("\nWhat is the new value for {}".format(subjectToChange))
            newValue = input()
            try:
                # Check if the value is valid in student
                dataDict = s.update_student(subjectToChange, newValue, data)
            except ValueError as error:
                print("Hmmm... {}\n".format(error))
            else:   break
    elif transAns == 'y' or transAns == 'yes':
        # Make sure it's not a course that already exists
        print("Current transcript: {}".format(studentDict["_transcript"]))
        dataDict = s.update_student("transcript", studentDict["_transcript"], data)
    else:
        print("Sorry I don't understand")
        return data

    return dataDict # return the data
>>>>>>> 8f5946147103d092ce4bb4ed0a3808b334187ed2
