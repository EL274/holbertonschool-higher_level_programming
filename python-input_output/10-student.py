#!/usr/bin/python3
"""defines function writes class of student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name, self.last_name, self.age = first_name, last_name, age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
