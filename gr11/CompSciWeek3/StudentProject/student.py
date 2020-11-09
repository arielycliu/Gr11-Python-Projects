<<<<<<< HEAD
import transcript

# Student class
class StudentInfo:
    def __init__(self, studentID, lastName, firstName, gradeLevel, transcript, registered):
        # Make sure len of 8 and num

        # --------------- STUDENT ID -----------------
        try:
            nstudentID = int(studentID)
        except:
            raise ValueError('Make sure you entered your studentID correctly')
        if not nstudentID < 99999999 or nstudentID < 0:
            raise ValueError('Make sure that your studentID is correct')
        self._studentID = nstudentID # get rid of zeros converted to int then back for storage

        # --------------- STUDENT NAME -----------------
        # Make sure alpha and no spaces
        if lastName.isalpha() is False or firstName.isalpha() is False:
            raise ValueError('Make sure you entered your name correctly')
        if len(lastName) < 1 or len(firstName) < 1:
            raise ValueError('That doesn\'t look like a name')
        self._lastName = lastName
        self._firstName = firstName

        # --------------- STUDENT GRADE -----------------
        # Make sure grade is number
        try:
            ngradeLevel = int(gradeLevel)
        except:
            raise ValueError('Make sure you entered your grade correctly')
        # Make sure you don't assign above 12 bc Canadian education system
        if ngradeLevel < 1 or ngradeLevel > 12:
            raise ValueError('Sorry no grades above 12 or below 1 are accepted')
        self._gradeLevel = ngradeLevel

        # --------------- STUDENT TRANSCRIPT -----------------
        # Check courses are alphanumeric and that grades are from 0-100 in another function for faster user feedback
        self._transcript = transcript

        # --------------- STUDENT STATUS -----------------
        # Check if boolean
        if registered == True or registered.lower() == 'true' or registered.lower() == 'y' or registered.lower() == 'yes':
            self._registered = True
        elif registered == False or registered.lower() == 'false' or registered.lower() == 'n' or registered.lower() == 'no':
            self._registered = False
        else: raise ValueError('Make sure you entered your registration confirmation correctly')

    def add_student(self, data_dic):
        # add the new student object to dictionary
        data_dic[str(self._studentID)] = self.__dict__
        return data_dic

    def search_student_id(self, data_dict):
        return data_dict.get(str(self._studentID))

    def update_student(self, subjectToChange, new_value, data_dict):
        # change to object, search by id

        if subjectToChange == "lastname":
            # Check if valid
            s = StudentInfo(self._studentID, new_value, self._firstName, self._gradeLevel,
                                    self._transcript, str(self._registered))
            self._lastName = new_value  # update

        elif subjectToChange == "firstname":
            # Check if valid
            s = StudentInfo(self._studentID, self._lastName, new_value, self._gradeLevel,
                                    self._transcript, str(self._registered))
            self._firstName = new_value  # update

        elif subjectToChange == "grade" or subjectToChange == "gradelevel":
            # Check if valid
            s = StudentInfo(self._studentID, self._lastName, self._firstName, new_value,
                            self._transcript, str(self._registered))
            self._gradeLevel = int(new_value)  # update write as int

        elif subjectToChange == "transcript":
            transcriptNew = transcript.add_transcript(new_value)  # Ensures valid input no need to check again
            # I used new value to store the dict
            self._transcript = new_value.update(transcriptNew)
            self._transcript = new_value  # update

        elif subjectToChange == "registered":
            # Check if valid
            s = StudentInfo(self._studentID, self._lastName, self._firstName, self._gradeLevel,
                                    self._transcript, new_value)
            self._registered = s._registered  # update

        else:
            raise ValueError('Sorry that is not an available attribute to update')
        data_dict[str(self._studentID)] = self.__dict__
        return data_dict

    def search_student_last(self, data_dict):
        print("Searching for " + self._lastName)
        count = 0
        for i in data_dict:
            lastName = data_dict[i]["_lastName"]
            if lastName.lower() == self._lastName.lower():
                student = data_dict[i]
                print("%08d" % (int(student["_studentID"]),),  end="    ")
                print(student["_lastName"] + ',' + student["_firstName"])
                count += 1
        print("{} total results found".format(count))
        print(" *" * 9)
        return

    def change_mark(self, StudentTranscript, data_dict):
        self._transcript = StudentTranscript  # update
        data_dict[str(self._studentID)] = self.__dict__
        return data_dict


=======
import transcript

# Student class
class StudentInfo:
    def __init__(self, studentID, lastName, firstName, gradeLevel, transcript, registered):
        # Make sure len of 8 and num

        # --------------- STUDENT ID -----------------
        try:
            nstudentID = int(studentID)
        except:
            raise ValueError('Make sure you entered your studentID correctly')
        if not nstudentID < 99999999 or nstudentID < 0:
            raise ValueError('Make sure that your studentID is correct')
        self._studentID = nstudentID # get rid of zeros converted to int then back for storage

        # --------------- STUDENT NAME -----------------
        # Make sure alpha and no spaces
        if lastName.isalpha() is False or firstName.isalpha() is False:
            raise ValueError('Make sure you entered your name correctly')
        if len(lastName) < 1 or len(firstName) < 1:
            raise ValueError('That doesn\'t look like a name')
        self._lastName = lastName
        self._firstName = firstName

        # --------------- STUDENT GRADE -----------------
        # Make sure grade is number
        try:
            ngradeLevel = int(gradeLevel)
        except:
            raise ValueError('Make sure you entered your grade correctly')
        # Make sure you don't assign above 12 bc Canadian education system
        if ngradeLevel < 1 or ngradeLevel > 12:
            raise ValueError('Sorry no grades above 12 or below 1 are accepted')
        self._gradeLevel = ngradeLevel

        # --------------- STUDENT TRANSCRIPT -----------------
        # Check courses are alphanumeric and that grades are from 0-100 in another function for faster user feedback
        self._transcript = transcript

        # --------------- STUDENT STATUS -----------------
        # Check if boolean
        if registered == True or registered.lower() == 'true' or registered.lower() == 'y' or registered.lower() == 'yes':
            self._registered = True
        elif registered == False or registered.lower() == 'false' or registered.lower() == 'n' or registered.lower() == 'no':
            self._registered = False
        else: raise ValueError('Make sure you entered your registration confirmation correctly')

    def add_student(self, data_dic):
        # add the new student object to dictionary
        data_dic[str(self._studentID)] = self.__dict__
        return data_dic

    def search_student_id(self, data_dict):
        return data_dict.get(str(self._studentID))

    def update_student(self, subjectToChange, new_value, data_dict):
        # change to object, search by id

        if subjectToChange == "lastname":
            # Check if valid
            s = StudentInfo(self._studentID, new_value, self._firstName, self._gradeLevel,
                                    self._transcript, str(self._registered))
            self._lastName = new_value  # update

        elif subjectToChange == "firstname":
            # Check if valid
            s = StudentInfo(self._studentID, self._lastName, new_value, self._gradeLevel,
                                    self._transcript, str(self._registered))
            self._firstName = new_value  # update

        elif subjectToChange == "grade" or subjectToChange == "gradelevel":
            # Check if valid
            s = StudentInfo(self._studentID, self._lastName, self._firstName, new_value,
                            self._transcript, str(self._registered))
            self._gradeLevel = int(new_value)  # update write as int

        elif subjectToChange == "transcript":
            transcriptNew = transcript.add_transcript(new_value)  # Ensures valid input no need to check again
            # I used new value to store the dict
            self._transcript = new_value.update(transcriptNew)
            self._transcript = new_value  # update

        elif subjectToChange == "registered":
            # Check if valid
            s = StudentInfo(self._studentID, self._lastName, self._firstName, self._gradeLevel,
                                    self._transcript, new_value)
            self._registered = s._registered  # update

        else:
            raise ValueError('Sorry that is not an available attribute to update')
        data_dict[str(self._studentID)] = self.__dict__
        return data_dict

    def search_student_last(self, data_dict):
        print("Searching for " + self._lastName)
        count = 0
        for i in data_dict:
            lastName = data_dict[i]["_lastName"]
            if lastName.lower() == self._lastName.lower():
                student = data_dict[i]
                print("%08d" % (int(student["_studentID"]),),  end="    ")
                print(student["_lastName"] + ',' + student["_firstName"])
                count += 1
        print("{} total results found".format(count))
        print(" *" * 9)
        return

    def change_mark(self, StudentTranscript, data_dict):
        self._transcript = StudentTranscript  # update
        data_dict[str(self._studentID)] = self.__dict__
        return data_dict


>>>>>>> 8f5946147103d092ce4bb4ed0a3808b334187ed2
