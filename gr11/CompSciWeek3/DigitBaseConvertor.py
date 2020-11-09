"""
DIGIT CONVERTER

Ariel Liu

The Woodlands Secondary School

Read inputs from conversions.txt, for each case read values of the original base,
the number to convert, and the base to convert to. Output the number in the new base.

Add-ons:
- Accept any base
- Negative inputs in any base converting to binary and represented in 8-bit two's complement form

"""


# Convert to the specified base
def to_base(num_10, new_base):
    new_num = ''
    while num_10 > 0:
        div = int(num_10 % new_base)
        # Check if over the digits we can use 0-9
        if div > 9:
            # Convert number to char
            new_num += chr(div - 10 + 65) # change 65 to 97 if you want lowercase
        else:
            # Add new num to str, concatenate as str
            new_num += str(div)
        # Find Remainder
        num_10 //= new_base
    return new_num[::-1]


# Convert to dec
def from_base(num, og_base):
    return int(num, og_base)


# Combine the two processes to convert stuff
def convert_to_base(og_base, og_num, new_base):
    dec_form = from_base(str(og_num), int(og_base))
    new_form = to_base(dec_form, new_base)
    return new_form


# Function for two's complement
def two_complement(og_base, og_num, new_base):
    # Make sure convert to binary
    if int(new_base) != 2:
        print("Sorry I can only convert negative nums t22o binary form")
        return
    else:
        # Convert the number to binary without the neg sign
        bin_num = convert_to_base(og_base, og_num[1:], 2)
        # Check if under 7 bits
        if int(bin_num) > 1111111 or int(bin_num) < 0:  # -128 and 127
            print("Hmm...heads up this number doesn't fit in (gonna get a chopped off version)")
            bin_num = bin_num[:7]

        # Convert to proper format, add zero to front and such
        bin_og_format = "0%07d" % (int(bin_num,))
        print("Number in Reg Binary Form: -{}".format(bin_og_format))
        two_c = ''

        # Inverse the binary string
        for b in bin_og_format:
            if b == '1':  two_c += '0'
            else:  two_c += '1'

        # Convert to decimal add 1, convert back
        fin_num = convert_to_base(10, from_base(two_c, 2)+1, 2)
        print("Two's Complement Form: {}".format(fin_num)) # add the one for neg or not?
        print("  -" * 8)
        return fin_num


# Read File
txt = open('conversions.txt', 'r')
while True:
    # Read the next case
    ogBase = txt.readline()
    ogNum = txt.readline()
    newBase = txt.readline()

    if ogBase == '%%%\n' or ogBase == '%%%': # Make sure not ending
        break

    # Just a bit of checking for input errors
    try:
        n_ogBase = int(ogBase)
        n_newBase = int(newBase)
    except ValueError:
        print("Invalid Base Input")
        break

    c_ogNum = ogNum.replace(' ','')

    # Check if starts with negative sign for twos complements
    if c_ogNum[:1] == '-':
        # checks if converting to binary in function
        two_complement(ogBase, c_ogNum, n_newBase)
    else:
        try:
            # ogBase: str or int, ogNum: str, newBase: int
            newNum = convert_to_base(ogBase, c_ogNum, n_newBase)
            print(newNum + '\n')
        except:
            print("Whoops something went wrong, please try again")

txt.close()  # Close files






