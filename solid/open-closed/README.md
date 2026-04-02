# Open-Closed Principle

The Open-Closed Principle (OCP) is a principle of object-oriented design that states that software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. This means that you should be able to add new functionality to a system without having to modify the existing code.


## What will happen if we violate the Open-Closed Principle?

1. Adding new features becomes chaotic because when you modify the existing code, you may break the existing functionality.
2. Modifying existing code becomes more complex because you may need to modify multiple parts of the code to add a new feature.

### Thumb rule

Avoid if-else statements where you are checking the type of the object. Instead, using a base class, create a subclass for each type of object and implement the desired functionality in the subclass.

