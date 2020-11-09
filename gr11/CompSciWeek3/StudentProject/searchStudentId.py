<<<<<<< HEAD
# Ari
import student


# search studentID program
def search_student_id(data):
    # Make sure valid Student ID
    while True:
        print("Please input the student ID you are searching for: ")
        searchStudentID = input()
        try:
            s = student.StudentInfo(searchStudentID, "Liu", "A", 1, {}, 'true')
            if int(searchStudentID) > len(data) - 1:  # Make sure under the dict index of students
                raise ValueError('This student doesn\'t exist')
        except ValueError as error:
            print("Hmmm... {}".format(error))
        else:
            break

    # Search for student data and return dict of student
    studentDict = s.search_student_id(data)

    # Print the attributes the user wants to know
    while True:
        print("\nWhat attribute would you like to look up?")
        print("last name, first name, grade level, transcript, registration status, all, or exit program")
        attribute = input().lower().replace(" ", "")

        if attribute == "exit" or attribute == "exit program":
            break  # before the rest so it doesn't print ID

        print("Student ID: %08d" % (int(searchStudentID),))

        if attribute == "studentid":
            print("   - - - - -")

        elif attribute == "lastname":
            print("Student Last Name: {}".format(studentDict["_lastName"]))

        elif attribute == "firstname":
            print("Student First Name: {}".format(studentDict["_firstName"]))

        elif attribute == "grade" or attribute == "gradelevel":
            print("Student Grade: {}".format(studentDict["_gradeLevel"]))

        elif attribute == "transcript":
            print("Student Transcript: {}".format(studentDict["_transcript"]))

        elif attribute == "registration" or attribute == "registrationstatus":
            print("Student Registration Status: {}".format(studentDict["_registered"]))

        elif attribute == "all":
            print("Student info:")
            for n in studentDict:
                print(n[1:], end=':  ')
                print(studentDict[n])

        else:
            print("Sorry I don't understand")
        print(" *" * 18)
    return
=======
# Ari
import student


# search studentID program
def search_student_id(data):
    # Make sure valid Student ID
    while True:
        print("Please input the student ID you are searching for: ")
        searchStudentID = input()
        try:
            s = student.StudentInfo(searchStudentID, "Liu", "A", 1, {}, 'true')
            if int(searchStudentID) > len(data) - 1:  # Make sure under the dict index of students
                raise ValueError('This student doesn\'t exist')
        except ValueError as error:
            print("Hmmm... {}".format(error))
        else:
            break

    # Search for student data and return dict of student
    studentDict = s.search_student_id(data)

    # Print the attributes the user wants to know
    while True:
        print("\nWhat attribute would you like to look up?")
        print("last name, first name, grade level, transcript, registration status, all, or exit program")
        attribute = input().lower().replace(" ", "")

        if attribute == "exit" or attribute == "exit program":
            break  # before the rest so it doesn't print ID

        print("Student ID: %08d" % (int(searchStudentID),))

        if attribute == "studentid":
            print("   - - - - -")

        elif attribute == "lastname":
            print("Student Last Name: {}".format(studentDict["_lastName"]))

        elif attribute == "firstname":
            print("Student First Name: {}".format(studentDict["_firstName"]))

        elif attribute == "grade" or attribute == "gradelevel":
            print("Student Grade: {}".format(studentDict["_gradeLevel"]))

        elif attribute == "transcript":
            print("Student Transcript: {}".format(studentDict["_transcript"]))

        elif attribute == "registration" or attribute == "registrationstatus":
            print("Student Registration Status: {}".format(studentDict["_registered"]))

        elif attribute == "all":
            print("Student info:")
            for n in studentDict:
                print(n[1:], end=':  ')
                print(studentDict[n])

        else:
            print("Sorry I don't understand")
        print(" *" * 18)
    return
>>>>>>> 8f5946147103d092ce4bb4ed0a3808b334187ed2
