from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class that defines a sound method to be implemented by subclasses"""
    @abstractmethod
    def sound(self):
        """Abstract method must be implemented in subclasses to make a sound."""
        pass


class Dog(Animal):
    """Subclass Dog inheriting from Animal."""
    def sound(self):
        """Implementing the sound method for Dog."""
        return "Bark"


class Cat(Animal):
    """Subclass Cat inheriting from Animal."""
    def sound(self):
        """Implementing the sound method for Cat."""
        return "Meow"
