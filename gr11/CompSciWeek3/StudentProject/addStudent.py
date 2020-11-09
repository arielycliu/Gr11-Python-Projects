<<<<<<< HEAD
# Janice
import student
import transcript


# Faster feedback loop for customer
def add_input(question):
    if question == 0:
        print("Input your last name: ")
        return input()
    elif question == 1:
        print("Input your first name: ")
        return input()
    elif question == 2:
        print("Input your grade: ")
        return input()
    else:
        print("Are you registered to take courses: Y or N") # don't call transcript then don't check it here
        return input()


# Test if the attributes are valid by kinda fake initiating an obj
def test_input(question, studentInfo, nextStudentID):
    if question == 0:
        s = student.StudentInfo(nextStudentID, studentInfo, "A", "1", {}, "True") # just testing if it's valid
    elif question == 1:
        s = student.StudentInfo(nextStudentID, "A", studentInfo, "1", {}, "True")
    elif question == 2:
        s = student.StudentInfo(nextStudentID, "A", "A", studentInfo, {}, "True")
    elif question == 3:
        s = student.StudentInfo(nextStudentID, "A", "A", "1", {}, studentInfo)
    return


# Add Student Function
def add_student(data):
    nextStudentID = len(data)
    print("Your assigned ID is: %08d" % (nextStudentID,))  # Give the student the next assigned ID
    validStudentInfo = []
    transcriptData = {}

    # Function for calling input and checking for errors
    for i in range(4):  # There is a more efficient way to conduct this
        while True:  # But this is the most user friendly with the fastest feedback loop
            studentInfo = add_input(i)
            try:
                test_input(i, studentInfo, nextStudentID)  # We're checking if the attribute would be valid each time
            except ValueError as error:
                print("Hmmm... {}".format(error))
            else:
                validStudentInfo.append(studentInfo)
                break

    # If the registration status is true run the input transcript program
    registrationCheck = validStudentInfo[3].lower()
    if registrationCheck == 'true' or registrationCheck == 'y':
        transcriptData = transcript.add_transcript({})  # only if taking courses is true

    # Add Program
    s = student.StudentInfo(nextStudentID, validStudentInfo[0], validStudentInfo[1], validStudentInfo[2],
                            transcriptData, validStudentInfo[3])

    dataDict = s.add_student(data) # run method add
    return dataDict



=======
# Janice
import student
import transcript


# Faster feedback loop for customer
def add_input(question):
    if question == 0:
        print("Input your last name: ")
        return input()
    elif question == 1:
        print("Input your first name: ")
        return input()
    elif question == 2:
        print("Input your grade: ")
        return input()
    else:
        print("Are you registered to take courses: Y or N") # don't call transcript then don't check it here
        return input()


# Test if the attributes are valid by kinda fake initiating an obj
def test_input(question, studentInfo, nextStudentID):
    if question == 0:
        s = student.StudentInfo(nextStudentID, studentInfo, "A", "1", {}, "True") # just testing if it's valid
    elif question == 1:
        s = student.StudentInfo(nextStudentID, "A", studentInfo, "1", {}, "True")
    elif question == 2:
        s = student.StudentInfo(nextStudentID, "A", "A", studentInfo, {}, "True")
    elif question == 3:
        s = student.StudentInfo(nextStudentID, "A", "A", "1", {}, studentInfo)
    return


# Add Student Function
def add_student(data):
    nextStudentID = len(data)
    print("Your assigned ID is: %08d" % (nextStudentID,))  # Give the student the next assigned ID
    validStudentInfo = []
    transcriptData = {}

    # Function for calling input and checking for errors
    for i in range(4):  # There is a more efficient way to conduct this
        while True:  # But this is the most user friendly with the fastest feedback loop
            studentInfo = add_input(i)
            try:
                test_input(i, studentInfo, nextStudentID)  # We're checking if the attribute would be valid each time
            except ValueError as error:
                print("Hmmm... {}".format(error))
            else:
                validStudentInfo.append(studentInfo)
                break

    # If the registration status is true run the input transcript program
    registrationCheck = validStudentInfo[3].lower()
    if registrationCheck == 'true' or registrationCheck == 'y':
        transcriptData = transcript.add_transcript({})  # only if taking courses is true

    # Add Program
    s = student.StudentInfo(nextStudentID, validStudentInfo[0], validStudentInfo[1], validStudentInfo[2],
                            transcriptData, validStudentInfo[3])

    dataDict = s.add_student(data) # run method add
    return dataDict



>>>>>>> 8f5946147103d092ce4bb4ed0a3808b334187ed2
