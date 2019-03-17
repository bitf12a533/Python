import sys


# Exercise3.1. Writeafunctionnamed right_justify thattakesastringnamed s asaparameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display


def right_justify(string_to_be_justified):
    """
    string_to_be_justified: String which needs to be right justified
    """
    empty_space = " " * (70 - len(string_to_be_justified))
    justified_string = empty_space + string_to_be_justified
    print(justified_string)


def do_twice(fun):
    fun()
    fun()

def print_spam():
    print('spam')