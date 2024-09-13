#!/usr/bin/python3
a = 89
b = 10
temp = a  # Save the value of a in a temporary variable
a = b     # Assign the value of b to a
b = temp  # Assign the value of temp (original a) to b
print("a={:d} - b={:d}".format(a, b))
