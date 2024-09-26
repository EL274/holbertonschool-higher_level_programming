from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class defines a sound method implemented by subclasses"""
    @abstractmethod
    def sound(self):
        """Abstract method implimented in subclass"""
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
