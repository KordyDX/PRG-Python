import random as rnd

def num_gen(length):
    l = []
    for x in range(0, length):
        l.append(rnd.randint(48, 57))

    s = ''.join(map(chr,l))
    return s

def upper_gen(length):
    l = []
    for x in range(0, length):
        l.append(rnd.randint(65, 90))

    s = ''.join(map(chr,l))
    return s

def lower_gen(length):
    l = []
    for x in range(0, length):
        l.append(rnd.randint(97, 122))

    s = ''.join(map(chr,l))
    return s

def sym_gen(length):
    l = []
    while (len(l) < length):
        i = rnd.randint(33, 46)
        if (i != 34 and i != 39 and i != 40 and i != 41 and i != 44 and i != 47):
            l.append(i)

    s = ''.join(map(chr,l))
    return s

print("""
                                || Hello there! ||
                     || Welcome to Kordy's password generator. ||

            || In a few moments you will be asked for how much various  ||
            || characters, symbols etc. you want your password to have. ||

|| Length of the password Is determined by the total number of elements you punch In. ||

""")

input("Press Enter to continue...")

max_num = int(input("How many numbers do you want the password to have?\n"))
max_upper = int(input("How many uppercase letters?\n"))
max_lower = int(input("How many lowercase letters?\n"))
max_sym = int(input("How many extra symbols?\n"))

var = num_gen(max_num) + upper_gen(max_upper) + lower_gen(max_lower) + sym_gen(max_sym)
var = rnd.sample(var, len(var))
var = "".join(var)

print("Your password is: " + var)