"""
How do you know when to use a

list  => [] => Square brackets
      => Duplicates: Yes
      => Ordered:    Yes
      => Mutable:    Yes

tuple => () => Paranthesis
      => Duplicates: Yes
      => Ordered:    Yes
      => Mutable:    No

set   => {} => Curly braces
      => Duplicates: No
      => Ordered:    No
      => Mutable:    Yes
"""

######################################################################################################################################################
# Set automatically drops duplicates, list and tuple keeps them. Sets are useful when you want to eliminate duplicate values from collections.
#
# Set's are un-ordered. Lists and Tuples are ordered. In ordered collections each items has a position also called an index.
#
# When you assign a list or set to a variable, you can accesses the items using index.
#
# Set's are un-ordered. Which means it's items are not assigned a position. You cannot do y[0] in sets.
######################################################################################################################################################

# x = [1, 1, 2, 2, 3, 3, 4, 4]
# y = set(x)
# print(x) # [1, 1, 2, 2, 3, 3, 4, 4]
# print(y) # {1, 2, 3, 4}

# You can add() and remove items from
# y.add(10)
# y.remove(3)
# print(y)

#######################
# List vs Tuples
# The difference is whether the collection can be modified after it's created, a trait called mutability
#
# Lists are mutable, you can modify them after creating them
# Tuples cannot be modified once created. Helps to keep your data safe from accidental changes.
#######################

x_list = [1, 2, 3, 3]
