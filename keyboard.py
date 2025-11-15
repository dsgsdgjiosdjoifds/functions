###
# Functions to read any data type from the keyboard
#
def input_string(message):
    a = input(message)
    return a

def input_integer(message):
    a = input(message)
    return int(a)

def input_real(message):
    a = input(message)
    return float(a)

def input_boolean(message):
    a = input(message)
    return bool(a)