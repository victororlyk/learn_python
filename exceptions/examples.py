import sys


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("invalid number entered, please try again")
        except EOFError:
            sys.exit(0)


first_number = getint("first ")
second_number = getint("second ")

try:
    print("{} divided by {} is {}".format(first_number, second_number,
                                          first_number / second_number))
except ZeroDivisionError:
    print("you can't divide by 0")
    sys.exit(2)
