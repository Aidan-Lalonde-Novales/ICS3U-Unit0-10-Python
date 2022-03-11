#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created March 2022
# This program adds 0.1 and 0.2


def main():
    # this function adds 0.1 and 0.2

    # input
    number = float(input("Enter a number: "))

    # process
    output = number + 1

    # output
    print("")
    print("Your answer is {0:,.2f}".format(output))
    print("\nDone.")


if __name__ == "__main__":
    main()
