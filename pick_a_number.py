#!/usr/bin/env python3

# Created by: Izza Khalid
# Created on: October 2019
# This program checks if your number is right
# with user input

import constants


def main():
    # this function checks if your number is right

    # input
    print("Quick! Pick a number between 0 and 9")
    print("")
    your_number = int(input("Enter the number of your choice: "))

    # process
    if your_number == constants.MY_NUMBER:
        # output
        print("")
        print("You got it right")


if __name__ == "__main__":
    main()
