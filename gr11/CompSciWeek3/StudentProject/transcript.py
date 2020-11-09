<<<<<<< HEAD
# Function Ari made for inputting transcript and adding courses
# it's really only longer cause I'm checking for valid input and giving user feedback each step of the way


def add_transcript(transcript_dict):
    # Ask for how many courses
    while True:
        print("How many courses are you adding to your transcript?")
        try:
            course_count = int(input())
        except ValueError:
            print("Please input a valid number")
        else:
            break

    for i in range(course_count): # for each course
        while True:  # make sure valid course code
            print("Input your #{} course code:".format(i + 1))  # add one count from 0
            try:
                course_code = input().upper()  # make sure valid add to transcript
                course_code = course_code.replace(" ", "")

                # Make sure not a repeat course mark
                if course_code in transcript_dict:
                    print("This course already exists")
                    continue
                # you can't update it need to use mark change

                # Make sure valid course code actually
                if not len(course_code) == 5: # change length five
                    raise ValueError
                if not course_code[3].isnumeric() == True:
                    raise ValueError
                if not course_code[:3].isalpha() == True or not course_code[4:].isalpha() == True:
                    raise ValueError
            except ValueError:
                print("Please input a valid 5 digit course code: e.g, ICS3U")
            else: break

        while True:  # make sure valid course mark
            print("Input your #{} course mark:".format(i + 1))  # add one count from 0
            try:
                course_mark = int(input())  # make sure valid add to transcript
                if course_mark < 0 or course_mark > 100:  # negative zero counts
                    raise ValueError
                # Add to dictionary
                transcript_dict[course_code] = course_mark
            except ValueError:
                print("Please input a valid course mark")
            else:
                break

    return transcript_dict
=======
# Function Ari made for inputting transcript and adding courses
# it's really only longer cause I'm checking for valid input and giving user feedback each step of the way


def add_transcript(transcript_dict):
    # Ask for how many courses
    while True:
        print("How many courses are you adding to your transcript?")
        try:
            course_count = int(input())
        except ValueError:
            print("Please input a valid number")
        else:
            break

    for i in range(course_count): # for each course
        while True:  # make sure valid course code
            print("Input your #{} course code:".format(i + 1))  # add one count from 0
            try:
                course_code = input().upper()  # make sure valid add to transcript
                course_code = course_code.replace(" ", "")

                # Make sure not a repeat course mark
                if course_code in transcript_dict:
                    print("This course already exists")
                    continue
                # you can't update it need to use mark change

                # Make sure valid course code actually
                if not len(course_code) == 5: # change length five
                    raise ValueError
                if not course_code[3].isnumeric() == True:
                    raise ValueError
                if not course_code[:3].isalpha() == True or not course_code[4:].isalpha() == True:
                    raise ValueError
            except ValueError:
                print("Please input a valid 5 digit course code: e.g, ICS3U")
            else: break

        while True:  # make sure valid course mark
            print("Input your #{} course mark:".format(i + 1))  # add one count from 0
            try:
                course_mark = int(input())  # make sure valid add to transcript
                if course_mark < 0 or course_mark > 100:  # negative zero counts
                    raise ValueError
                # Add to dictionary
                transcript_dict[course_code] = course_mark
            except ValueError:
                print("Please input a valid course mark")
            else:
                break

    return transcript_dict
>>>>>>> 8f5946147103d092ce4bb4ed0a3808b334187ed2
