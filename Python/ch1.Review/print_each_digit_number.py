number = input("Enter an integer: ")
for digit in number:
    if int(digit) == 0:
        print(digit + ':')
    else:
        print(digit + ': ' + int(digit) * digit)