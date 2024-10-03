class Student:
     """defines function writes class of student"""


    def __init__(self, first_name, last_name, age):
        """Initialise une nouvelle instance de Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns attribute  instance"""
        if attrs is not None and isinstance(attrs, list):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        else:
            return self.__dict__

