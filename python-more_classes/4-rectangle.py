#!/usr/bin/python3
class Rectangle:
    """Représente un rectangle."""

    def __init__(self, width=0, height=0):
        """Initialise un nouveau rectangle.

        Args:
            width (int): La largeur du rectangle.
            height (int): La hauteur du rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Récupère/Modifie la largeur du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Récupère/Modifie la hauteur du rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Renvoie l'aire du rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Renvoie le périmètre du rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Renvoie la représentation imprimable du rectangle.

        Représente le rectangle avec le caractère #.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Renvoie la représentation officielle du rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
