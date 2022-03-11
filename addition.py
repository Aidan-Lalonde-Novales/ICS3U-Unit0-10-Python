#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created March 2022
# This program adds 0.1 and 0.2


def main():
    # this function adds 0.1 and 0.2

    # process
    total = 0.1 + 0.2

    # output
    print("0.1 + 0.2 = ?")
    print("")
    print("Your answer is {0} without scientific notation".format(total))
    print("")
    print("Your answer is {0:.1e} with scientific notation".format(total))
    print("\nDone.")


if __name__ == "__main__":
    main()
