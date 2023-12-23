#!/usr/bin/env python3
import sys

def paircheck(arg: str) -> str:
    """
    Write a script that uses one or more functions to assess whether or not all parentheses in an input string are
    paired.
    arg: takes a string value that includes parentheses as an argument
    """
    if arg[0] == ")":
        print("NOT PAIRED")
    elif arg[-1] == "(":
        print("NOT PAIRED")
    elif arg.count("(") == arg.count(")"):
        print("PAIRED")
    else:
        print("NOT PAIRED")
            
#call a function
paircheck(sys.argv[1])




