class Student:
    def __init__(self, first_name, last_name, age):
        """Initialise une nouvelle instance de Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retourne la représentation sous forme de dictionnaire de l'instance"""
        return self.__dict__

