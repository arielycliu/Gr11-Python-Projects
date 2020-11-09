"""
BRACKET LOGIC ADD-ON POSSIBILITIES

Ariel Liu

The Woodlands Secondary School

Take in input of number of brackets and print all possible combinations

"""

leftBracket = "("
rightBracket = ")"
bracket_list = []

# import time       # you can use for testing
# startingTime = time.time()


# Function for running actual work
def driver_portion(n_pairs):
    if n_pairs > 1:
        # outer most pair fixed
        usable_left = n_pairs

        # Starts at 0 with no brackets open
        usable_right = 0
        return_value = ""
        bracket_stuff(usable_left, usable_right, return_value)

    elif n_pairs == 1:
        global bracket_list
        bracket_list.append(leftBracket + rightBracket)

    return bracket_list


# The actual work being done
def bracket_stuff(usable_left, usable_right, return_value):
    final_brackets = return_value
    global rightBracket
    global leftBracket
    global bracket_list

    # Three cases
    # If there is no left brackets left to use, have to start closing
    # If there is no right brackets left can only use right
    # We can use both right and left brackets

    if usable_left == 0: # When there is no left brackets left to use
        for i in range(usable_right):
            final_brackets += rightBracket
        # Only place to add the results for that round
        bracket_list.append(final_brackets)
    else:
        if usable_right == 0: # When there are no right brackets left to use
            usable_left -= 1
            final_brackets += leftBracket

            # Since you opened a bracket a new right bracket spot is opened up
            usable_right += 1
            final_brackets += bracket_stuff(usable_left, usable_right, final_brackets)
        elif usable_left > 0 and usable_right > 0: # Can use both left or right
            # First run path, using left first
            # You wanna keep both left and right for the second run
            temp_left = usable_left
            temp_right = usable_right
            temp_brackets = final_brackets

            # Using a left bracket
            usable_left -= 1
            final_brackets += leftBracket

            # Increasing usable right bracket by one, since you opened a new bracket
            usable_right += 1
            final_brackets += bracket_stuff(usable_left, usable_right, final_brackets)

            # Need to reset both the usable left and right sides back to the value before recursive call
            # This part makes sure to catch all the edge cases missed from ver 1.2
            usable_left = temp_left
            usable_right = temp_right
            final_brackets = temp_brackets

            # Then run the second path for right brackets
            usable_right -= 1
            final_brackets += rightBracket
            final_brackets += bracket_stuff(usable_left, usable_right, final_brackets)

    return final_brackets


# Loop till input is a valid one
while True:
    print("Input the number of brackets: ")
    try:
        num = int(input())
    except ValueError:
        print("Input a valid integer please ")
        continue
    if num <= 0:
        print("'No zeros accepted Ariel' - Janice An 2020 ")
    elif (num % 2) != 0:
        print("Whoops even numbers only")
    else:
        break

# Calculate for pairs, call function
result = driver_portion(num/2)
print("The total possibilities for {} brackets is {}".format(num/2, len(result)))
# print("Taking {} secs".format(time.time()-startingTime))

count = 1
for i in result:
    print("Possibility #" + str(count), end=":  ")
    print(i)
    count += 1





