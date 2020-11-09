"""
ARRANGEMENTS

Ariel Liu

The Woodlands Secondary School

Read input list generates all possible variations/permutations for the list

Notes:
- Solve this only using the commands def (defining a function); selections (if/elif/else statements); and direct list manipulations (e.g. “.append”, “.index()”, etc..).
- Avoid use of numbers and arithmetic operators.
- The list input may contain elements other than integers (e.g. strings) so the perm function should be able to handle this possibility.
- You will likely be required to utilize “helper functions” that should also abide by the above conditions.
- Think carefully about the base case for each function that you write, and do not add additional base cases beyond the empty-list case.
- Not allowed to use LOOPS

"""
temp = []
exitP = False
ver = []


# Function to generate variations of the list
def perms(arr):
    global temp, exitP
    if len(arr) < 1:
        print("Invalid input, must input something")
        return []
    # If the array is over one element
    elif len(arr) > 1:
        rec(0, arr)  # Call other function
    else:
        temp.append(arr[0])  # Apply the last element to array
        global ver
        if temp not in ver:  # check that variation not already added
            ver.append(list(temp))
        temp.pop()  # delete the cache
    return ver


def rec(n, arr): # Recursive helper function to avoid using loops
    if n >= len(arr):  # if counter over return, replace for loop
        return
    else:
        arr2 = arr[:n] + arr[n + 1:]  # prepare array without the current element
        temp.append(arr[n])
        perms(arr2)  # going down the possibilities for remaining element in a smaller array
        temp.pop()
        rec(n+1, arr) # loop thru it again


# Get input
print("Input the list's elements separated by a space:")
array = input().split()

variations = perms(array)  # Call function
print(variations)
print("{} Variations of the list found".format(len(ver)))


