"""
Abstract classes can be considered as blueprints for other classes.
They allow you to define methods that must be created within any child classes built from the abstract class.
A class that contains one or more abstract methods is called an abstract class.
Abstract classes cannot be instantiated, meaning you cannot create objects from them directly.
"""

from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def sound(self):
        ...
    
    @abstractmethod
    def move(self):
        ...

class Dog(Animal):
    
    def sound(self):
        return "Bark"
    
    def move(self):
        return "Runs on all fours"

class Bird(Animal):
    
    def sound(self):
        return "Chirp"
    
    def move(self):
        return "Flies in the sky"

def print_animal_sound(animal: Animal):
    print(f"{animal.name} makes a sound: {animal.sound()}")

dog1 = Dog("Buddy")
# print(f"{dog1.name} says {dog1.sound()} and {dog1.move()}.")

bird1 = Bird("Tweety")
# print(f"{bird1.name} says {bird1.sound()} and {bird1.move()}.")

print_animal_sound(dog1)
print_animal_sound(bird1)