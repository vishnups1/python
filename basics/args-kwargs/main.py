"""
In a nutshell writing a function definition *args, **kwargs allows us to call the functions with flexible number of arguments

def tea_order(*args, **kwargs):
    # code

tea_order("Alice", "green")
tea_order("Alice", "green", milk="oat")
tea_order("Alice", "green", "honey", "lemon")

Ideally we want our function to support any number of order extras without having to constantly modify it.

*args    -> Collect any number of positional arguments in to a tuple called args. "*" pack extra poistional arguments in to tuple.
**kwargs -> Collect any number of keyword arguments in to a dictionary called kwargs.

NOTE: While calling the function you MUST always pass positional arguments before keyword arguments.
"""

"""
In function calls * and ** acts as unpack, where as in function definition it acts as pack

* -> can act as unpack operator lists and tuples
** -> can act as unpack operator for dictionaries
"""

def tea_order(customer_name: str, tea_type: str, *args, **kwargs):
    print(f"{customer_name} ordered {tea_type}")
    for arg in args:
        print(f"  - {arg}")
    for key, value in kwargs.items():
        print(f"{key} -> {value}")

vishnu_preferences = ["nosugar", "tetley"]
vishnu_preferences_dict = {"foo": "bar", "bar": "baz"}

tea_order("vishnu", "green", *vishnu_preferences, **vishnu_preferences_dict)