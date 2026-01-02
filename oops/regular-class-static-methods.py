class Employee:

    raise_amount = 1.04
    instance_count = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        Employee.instance_count += 1
    
    # Regular methods automatically pass the instance as the first argument (self)
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    # Class methods automatically pass the class as the first argument (cls)
    # To convert a regular method to a class method use '@classmethod' decorator
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    """
    Use class methods as alternative constructor.

    What does it mean?

    You can use these class methods to create multiple ways of creating objects.
    """

    @classmethod
    def create_from_string(cls, name):
        first_name, last_name = name.split(" ")
        return cls(first_name, last_name)
    
    # Static methods don't pass anything automatically. The just behave like regular functions
    # To convert a regular method to a static method use '@staticmethod' decorator
    # Note: The method should be a static method if you don't access the instance or class in anywhere within the function 

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee.create_from_string("Vishnu Pradeep")
print(emp1.first_name)
print(emp1.last_name)

import datetime

# guess what datetime.date.today() is? It's a class method returns an instance of a 'date' class
print(emp1.is_workday(datetime.date.today()))