<<<<<<< HEAD
# Ari
import student

# Make sure valid Student ID
def check_valid_ID(data):
    while True:
        print("Please input the student ID of the student to have their mark changed: ")
        searchStudentID = input()
        try:
            # Similar to search student validation, but also checks that courses are present
            # Try making instance make sure it's valid and exists
            s = student.StudentInfo(searchStudentID, "L", "A", 1, {}, 'true')
            if int(searchStudentID) > len(data) - 1:  # Make sure under the dict index of students
                raise ValueError('This student doesn\'t exist')

            # Search for the students dict and make sure transcript has courses
            studentsDict = s.search_student_id(data)
            studentTranscript = studentsDict["_transcript"]
            if studentTranscript == {}:
                raise ValueError('This student hasn\'t taken any courses, please choose a different ID')
            else:
                print("Current Transcript: {}".format(studentTranscript))
        except ValueError as error:
            print("Hmmm... {}\n".format(error))
        else:
            break
    return searchStudentID, studentTranscript, studentsDict


# Make sure the mark is valid
def check_valid_mark():
    while True:  # make sure valid course grade
        print("Input your new course mark:")
        try:
            course_mark = int(input())  # make sure valid add to transcript
            if course_mark < 0 or course_mark > 100:  # negative zero counts
                raise ValueError
        except ValueError:
            print("Please input a valid course mark")
        else:
            break
    return course_mark

# Main mark change function
def mark_change(data):
    searchStudentID, studentTranscript,studentsDict = check_valid_ID(data)

    # Make sure valid existing subject
    while True:
        print("\nWhat existing subject\'s mark would you like to change? ")
        print("On the other hand: enter exit once your done editing")
        courseToChange = input().upper().replace(" ", "")
        if courseToChange == "EXIT":
            break
        elif courseToChange in studentTranscript:

            # Make sure valid mark
            while True:
                try:
                    courseMark = check_valid_mark()
                except ValueError as error:
                    print("Hmmm... {}".format(error))
                else:
                    break

            # Write it back in the right index
            studentTranscript[courseToChange] = courseMark
            print("Transcript updated: {}".format(studentTranscript))
            print(" *" * 18)

        else:
            print("Hmm... I can't seem to find that course")
            print("Please try again")

    # Revert reg back to str bool when convert obj
    s = student.StudentInfo(searchStudentID, studentsDict["_lastName"], studentsDict["_firstName"],
                            studentsDict["_gradeLevel"], studentTranscript, str(studentsDict["_registered"]))

    dataDict = s.change_mark(studentTranscript, data)  # return dict
    return dataDict
=======
# Ari
import student

# Make sure valid Student ID
def check_valid_ID(data):
    while True:
        print("Please input the student ID of the student to have their mark changed: ")
        searchStudentID = input()
        try:
            # Similar to search student validation, but also checks that courses are present
            # Try making instance make sure it's valid and exists
            s = student.StudentInfo(searchStudentID, "L", "A", 1, {}, 'true')
            if int(searchStudentID) > len(data) - 1:  # Make sure under the dict index of students
                raise ValueError('This student doesn\'t exist')

            # Search for the students dict and make sure transcript has courses
            studentsDict = s.search_student_id(data)
            studentTranscript = studentsDict["_transcript"]
            if studentTranscript == {}:
                raise ValueError('This student hasn\'t taken any courses, please choose a different ID')
            else:
                print("Current Transcript: {}".format(studentTranscript))
        except ValueError as error:
            print("Hmmm... {}\n".format(error))
        else:
            break
    return searchStudentID, studentTranscript, studentsDict


# Make sure the mark is valid
def check_valid_mark():
    while True:  # make sure valid course grade
        print("Input your new course mark:")
        try:
            course_mark = int(input())  # make sure valid add to transcript
            if course_mark < 0 or course_mark > 100:  # negative zero counts
                raise ValueError
        except ValueError:
            print("Please input a valid course mark")
        else:
            break
    return course_mark

# Main mark change function
def mark_change(data):
    searchStudentID, studentTranscript,studentsDict = check_valid_ID(data)

    # Make sure valid existing subject
    while True:
        print("\nWhat existing subject\'s mark would you like to change? ")
        print("On the other hand: enter exit once your done editing")
        courseToChange = input().upper().replace(" ", "")
        if courseToChange == "EXIT":
            break
        elif courseToChange in studentTranscript:

            # Make sure valid mark
            while True:
                try:
                    courseMark = check_valid_mark()
                except ValueError as error:
                    print("Hmmm... {}".format(error))
                else:
                    break

            # Write it back in the right index
            studentTranscript[courseToChange] = courseMark
            print("Transcript updated: {}".format(studentTranscript))
            print(" *" * 18)

        else:
            print("Hmm... I can't seem to find that course")
            print("Please try again")

    # Revert reg back to str bool when convert obj
    s = student.StudentInfo(searchStudentID, studentsDict["_lastName"], studentsDict["_firstName"],
                            studentsDict["_gradeLevel"], studentTranscript, str(studentsDict["_registered"]))

    dataDict = s.change_mark(studentTranscript, data)  # return dict
    return dataDict
>>>>>>> 8f5946147103d092ce4bb4ed0a3808b334187ed2
