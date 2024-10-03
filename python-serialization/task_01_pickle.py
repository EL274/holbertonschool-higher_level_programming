#!/usr/bin/python3
"""defines function creates custom class"""


import pickle


class CustomObject:
    """initialization of function"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

        
    def display(self):
        """print all of attributes"""                               
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"Object serialized and saved to {filename}")
        except Exception as e:
            print(f"Error serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                print(f"Object deserialized from {filename}")
                return obj
        except (FileNotFoundError, pickle.PickleError) as e:
            print(f"Error deserializing object: {e}")
            return None
