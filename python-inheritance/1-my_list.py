#!/usr/bin/python3
"""creates class Mylist"""


class MyList(list):
    """class which inherate the list and add methods to ptint sorted list"""

    def print_sorted(self):
        print(sorted(self))
