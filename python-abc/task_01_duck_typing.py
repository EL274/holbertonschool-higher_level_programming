from abc import ABC, abstractmethod

""" Abstract class Animal inheriting from ABC"""

class Animal(ABC):
"""Abstract method that must be implemented in subclasses"""
    @abstractmethod
    def sound(self):
        pass

"""Subclass Dog inheriting from Animal"""
class Dog(Animal):
    
    """Implementing the sound method for Dog"""
    def sound(self):
        return "Bark"

# Subclass Cat inheriting from Animal
class Cat(Animal):
    
    # Implementing the sound method for Cat
    def sound(self):
        return "Meow"
