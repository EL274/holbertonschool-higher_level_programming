#!/usr/bin/python3
"""Creates class Square with
private instance attribute size and position and
public instance methods to calculate area and print square."""


class Square:
    """Defines class with private instance attributes size and position
    and public instance methods to calculate area and print square."""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiates attribute size to 0 and position to (0, 0)"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the private instance attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the private instance attribute size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the private instance attribute position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the private instance attribute position"""
        check = 0
        while True:
            if type(value) is not tuple or len(value) != 2:
                check += 1
                break
            if type(value[0]) is not int or type(value[1]) is not int:
                check += 1
                break
            if value[0] < 0 or value[1] < 0:
                check += 1
            break
        if check == 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculates and returns current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Prints square of size self.__size using #"""
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for column in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for row in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
