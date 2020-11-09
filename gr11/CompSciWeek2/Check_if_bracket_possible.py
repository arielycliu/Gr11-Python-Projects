'''

BRACKET LOGIC

Ariel Liu

The Woodlands Secondary School

Take in input of rounded brackets and determine if the brackets make 'sense'

Add-on:
Checking for input errors when the input is not a bracket

'''

start = ["(", "{", "["]
end = [")", "}", "]"]


# Function to check is all characters are brackets, if not to return the wrong vals
# Telling the user which inputs were not accepted
def check_if_bracket(inputVal):
    right_vals = []
    wrong_vals = []
    brackets_list = [i for i in inputVal] # Split it up by character
    for bracket in brackets_list:
        # If the character is valid bracket
        if bracket in start or bracket in end:
            right_vals.append(bracket)
        else:       # If the character is not a bracket
            wrong_vals.append(bracket)
    return wrong_vals, right_vals


# Function to check each bracket has a corresponding one and is nested properly
def check_bracket(brackets):
    expected_brackets = []
    for bracket in brackets:
        if bracket in start:        # If the bracket is an opening one
            # Find the index of the bracket in the start array
            # Append the corresponding bracket form the end array, using the index
            expected_brackets.append(end[start.index(bracket)])
        elif bracket in end:        # If the bracket is a closing one
            if expected_brackets == [] or bracket != expected_brackets.pop():
                # Remove and check the last element matches current bracket
                # Don't remove if blank
                return False

    return expected_brackets == []   # If it's empty, return True (each bracket is corresponding)


print("This is a program to verify if brackets make 'sense'")
while True:  # loop till correct input
    print("List all of your brackets: ")
    inputVal = input().replace(' ','')  # Take in input fix whitespace

    checkedInput = check_if_bracket(inputVal)  # Send to function return list of right and wrong values
    wrong = checkedInput[0]
    brackets = checkedInput[1]

    # If there is an invalid input
    if len(wrong) != 0:  # Take out the blank is true
        print("\nSorry I didn't understand")
        print(' '.join(wrong))
        print("Input valid brackets only: ()[]{}")
        print("Please try again...\n")
        continue
    else:
        print(check_bracket(brackets))
        # break


