class Student:
    def __init__(self, first_name, last_name, age):
        """Initialisation of new instance student"""

        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return representation dictionary instance"""
        return self.__dict__

