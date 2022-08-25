#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, mul, div, sub
    import sys
    from sys import argv

    if len(argv) == 4:
        a = argv[1]
        b = argv[3]
        if argv[2] != '+' and argv[2] != '-' and argv[2] != '*' and argv[2] != '/':
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            if argv[2] == '+':
                print("{} + {} = {}".format(a, b, add(a, b)))
            elif argv[2] == '-':
                print("{} - {} = {}".format(a, b, sub(a, b)))
            elif argv[2] == '*':
                print("{} * {} = {}".format(a, b, mul(a, b)))
            else:
                print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
