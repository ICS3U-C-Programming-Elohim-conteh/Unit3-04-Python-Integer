#!/usr/bin/env python3

# Created by : elohim
# Created on : Oct 18 2026
# This program checks the user's integer in the program


def main():
    # Get the user's integer

    user_int = int(input("Enter an integer: "))

    # Check if user_int > 0

    if user_int > 0:

        # Display that the integer is positive

        print("{} is a positive integer".format(user_int))

    # Check if user_int < 0

    elif user_int < 0:

        # Display that the integer is negative

        print("{} is a negative integer".format(user_int))

    # Else

    else:

        # Display that the integer is equal to zero

        print("{} is equal to zero".format(user_int))


if __name__ == "__main__":

    main()
