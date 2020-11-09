<<<<<<< HEAD
# Ari
import student


# Search student last name function
def search_student_last(data):
    # Make sure last name is valid
    while True:
        print("Please input the student last name you are searching for: ")
        searchStudentLastName = input()
        try:
            s = student.StudentInfo(0, searchStudentLastName, "A", 1, {}, 'true')
        except ValueError as error:
            print("Hmmm... {}".format(error))
        else:
            break

    # search student last method
    s.search_student_last(data)
=======
# Ari
import student


# Search student last name function
def search_student_last(data):
    # Make sure last name is valid
    while True:
        print("Please input the student last name you are searching for: ")
        searchStudentLastName = input()
        try:
            s = student.StudentInfo(0, searchStudentLastName, "A", 1, {}, 'true')
        except ValueError as error:
            print("Hmmm... {}".format(error))
        else:
            break

    # search student last method
    s.search_student_last(data)
>>>>>>> 8f5946147103d092ce4bb4ed0a3808b334187ed2
    return