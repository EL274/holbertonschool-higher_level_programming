                                                                                                                                                                                 class Student:
    def __init__(self, first_name, last_name, age):
        """Initialise les attributs de l'instance Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retourne un dictionnaire représentant l'instance Student.
        Si attrs est une liste de chaînes de caractères, seules les
        clés correspondant à ces attributs sont retournées.
        """
        if attrs is not None and isinstance(attrs, list):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Remplace les attributs de l'instance par les valeurs dans le dictionnaire json.
        """
        for key, value in json.items():
            setattr(self, key, value)

# Exemple d'utilisation :
student = Student("John", "Doe", 23)
print(student.to_json())  # Affiche le dictionnaire complet des attributs
print(student.to_json(["first_name", "age"]))  # Affiche seulement les attributs spécifiés

# Remplacer les attributs avec un nouveau dictionnaire
student.reload_from_json({"first_name": "Jane", "age": 25})
print(student.to_json())  # Affiche les attributs mis à jour

