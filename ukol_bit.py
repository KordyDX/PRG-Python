num = int(input("Type in a number to work with.\n"))
bit = int(input("Type in the number of positions to jump.\n"))
dir = str(input("What direction? (Left or Right?)\n"))

try:
    print("Values before jump:  %i|" %num + bin(num))
    if(dir.casefold() == "left"):
        num <<= bit
    elif(dir.casefold() == "right"):
        num >>= bit
    else:
        exit("Enter only left or right")
    print("Value after jump %i|" %num + bin(num))
    
except ValueError:
    print("Wrong values in input.")