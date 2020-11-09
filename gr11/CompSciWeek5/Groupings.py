"""
GROUPINGS

Ariel Liu

The Woodlands Secondary School

Input list and integer and outputs a list of lists showing all groupings of the indicated integer

Notes:
- The order of the sub-lists is not important
- You should not generate any subsets of size greater than the input n

"""

temp = []
ver = []
count = 0


def group(arr, size):
    if len(temp) == size:
        global ver
        if temp not in ver:  # check that variation not already added
            ver.append(list(temp))
    else:
        for n in range(len(arr)):
            arr2 = arr[:n] + arr[n + 1:]
            temp.append(arr[n])
            group(arr2, size)
            temp.pop()
    return ver


# Get Input for list
print("Input the list's elements separated by a space:")
arra = input().split()

while True: # Ensure number is integer
    try:
        print("Input the size of the sub lists")
        s = int(input())

        if s < 0: # if over len of arra will return []
            raise ValueError
    except ValueError:
        print("Size must be above 0 and within the length of the og list")
        continue
    else:
        break

group(arra, s)
print(ver)
print("{} variations found ".format(len(ver)))