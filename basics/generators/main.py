"""
# https://www.youtube.com/watch?v=GWZf_B129zs

The yield keyword is what turns a regular function in to a generator function

Example (Generator):

def my_gen():
    # code
    yield value

Example (Regular Function):

def my_func():
    # code
    return value

At a high level 'yield' is similar to 'return' in a regular function. Both keywords send back a value from a function to the main program.

They difference is what happens after the value is sent back?

- In regular function once the value is handed back to main program, python stops executing the function.
- After passing back the value to the main program using yield, python pauses the execution. If there are remaining lines of code in the function,
they will be executed if the main program tells the generator to resume execution. Generators can be paused and resumed they can execute multiple yield statements.

This lets main program to request value one at a time which the generator produces only when asked.

def my_gen():
    # code
    yield value1
    yield value2
    yield value3

Like regular functions we can call generators using my_gen(), but when we run my_gen() it doesn't execute the function immediately, instead it returns an generator object.

You can think of this generator as a little machine that knows how to produce values and doesn't produce any values until we ask it to.

To ask our generator to produce a value you need to use next() function. This tells the generator to start running until it reaches the first yield hands back the value 1 and pause there

we will get "StopIteration" error when we run out of values


- SAVES MEMORY
- IMPROVES READABILITY
- IMPROVE MODULARITY
- IMPROVE MAINTAINABILITY


Generators are not perfect for every situations, because generators produce values on demand without storing them. Once the value is yielded the generator moves on and you cannot ask for that value again
"""

def my_gen():
    yield 1
    yield 2
    yield 3



######################################################################
# Scenario 1: Calling next() multiple times is not a feasible solution
######################################################################

# gen_object = my_gen()

# next(gen_object)
# next(gen_object)
# next(gen_object)
# next(gen_object) # StopIteration error

######################################################################
# Scenario 2: Using for loop handles calling next() on each iteration and handles StopIteration and exits loops automatically
######################################################################

# for value in my_gen():
#     print(value)

#############################
# Scenario 3: Proper usecase
#############################

# Below is a regular function, which is okay for smaller ranges.
# What if the range is in Millions and it's hard to store values in memory. Using a generator is a good usecase here.

# def get_primes_list(start, end):
#     primes = []
#     for num in range(start, end+1):
#         if num < 2:
#             continue
#         is_prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#         if is_prime:
#             primes.append(num)
#     return primes

# print(get_primes_list(50, 100))



######################
# WORK ONLY WHEN ASKED BEHAVIOUR = LAZY EVALUATION
#####################

def gen_primes_list(start, end):
    for num in range(start, end+1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            yield num

for i in gen_primes_list(50, 100):
    print(i)