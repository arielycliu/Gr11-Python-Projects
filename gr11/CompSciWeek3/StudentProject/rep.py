<<<<<<< HEAD
import json
fileJson = 'studentData.json'


# Class for reading and writing to the json
class Repository:
    def write(self, student): # program call for write file the data
        with open(fileJson, 'w') as json_file: # Make sure w overwrite
            json.dump(student, json_file, indent=4)
        return

    def read(self): # program call for read file return data
        with open(fileJson, "r") as json_file:
            student_loaded = json.load(json_file)
        return student_loaded
# Jan --> you don't need to use a class, you can also use a function
=======
import json
fileJson = 'studentData.json'


# Class for reading and writing to the json
class Repository:
    def write(self, student): # program call for write file the data
        with open(fileJson, 'w') as json_file: # Make sure w overwrite
            json.dump(student, json_file, indent=4)
        return

    def read(self): # program call for read file return data
        with open(fileJson, "r") as json_file:
            student_loaded = json.load(json_file)
        return student_loaded
# Jan --> you don't need to use a class, you can also use a function
>>>>>>> 8f5946147103d092ce4bb4ed0a3808b334187ed2
# but when you work on larger programs you would have classes for repositories (tis a good habit!)