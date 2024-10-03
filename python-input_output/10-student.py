class Student:
    def __init__(self, first_name, last_name, age):
        """Initialise une nouvelle instance de Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retourne la représentation sous forme de dictionnaire de l'instance.
        
        Si 'attrs' est une liste de chaînes de caractères, seuls les attributs
        mentionnés dans 'attrs' sont retournés. Sinon, tous les attributs sont retournés.
        """
        if attrs is not None and isinstance(attrs, list):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        else:
            return self.__dict__

