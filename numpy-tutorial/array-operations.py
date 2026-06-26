import numpy as np

#########################
# Basic array operations
#########################

# a1 = np.arange(1, 6)
# b1 = np.arange(1, 6)

# print(a1+b1) # [ 2  4  6  8 10]
# print(a1-b1) # [0 0 0 0 0]
# print(a1*b1) # [ 1  4  9 16 25]
# print(a1/b1) # [1. 1. 1. 1. 1.]
# print(a1%b1) # [0 0 0 0 0]

# print(a1.sum()) # 15

# c1 = np.array([[1, 2, 3, 4, 5, 6]]).reshape(2, 3)
# print(c1.sum(axis=0)) # [5 7 9]
# print(c1.sum(axis=1)) # [ 6 15]

############################
# Min, Max, Mean, Std, Prod
############################

# a1 = np.array([[1, 2, 3, 4, 5, 6]]).reshape(2,3)

"""
[
  [1, 2, 3]
  [4, 5, 6]
]
"""

# print(a1.min())        # 1
# print(a1.min(axis=0))  # [1, 2, 3]
# print(a1.min(axis=1))  # [1, 4]

# print(a1.max())        # 6
# print(a1.max(axis=0))  # [4 5 6]
# print(a1.max(axis=1))  # [3 6]

# print(a1.prod())       # 720
# print(a1.prod(axis=0)) # [ 4 10 18]
# print(a1.prod(axis=1)) # [  6 120]

# print(a1.std())        # 1.707825127659933
# print(a1.std(axis=0))  # [1.5 1.5 1.5]
# print(a1.std(axis=1))  # [0.81649658 0.81649658]

#############################
# Generating Random Numbers
#############################

# create a 2x2 array and pick number randomly between 1, 10
# a1 = np.random.randint(1, 11, (2, 2))
# print(a1)

"""
[
  [5 9]
  [10 10]
]
"""

# Advanced version
# rng = random number generator
# b1 = np.random.default_rng()
# print(b1.integers(2, 10, (2, 2)))

"""
[
  [7 9]
  [2 7]
]
"""

##################################################
# Unique Items, Tansposing Matrix, Reverse Arrays
##################################################

###########
# unique()
###########

# a1 = np.array([1, 2, 3, 4, 4])
# print(np.unique(a1))                       # [1 2 3 4]
# print(np.unique(a1, return_index=True))    # (array([1, 2, 3, 4]), array([0, 1, 2, 3]))
# print(np.unique(a1, return_counts=True))   # (array([1, 2, 3, 4]), array([1, 1, 1, 2]))
# print(np.unique(a1, return_inverse=True))  # (array([1, 2, 3, 4]), array([0, 1, 2, 3, 3]))

###################
# transpose() or T
###################

# a1 = np.array([1, 2, 3, 4, 4, 5]).reshape(2, 3)

# print(a1)

"""
[
  [1 2 3]
  [4 4 5]
]
"""

# print(a1.T)

"""
[
  [1 4]
  [2 4]
  [3 5]
]
"""

##########
# reverse
##########

a1 = np.array([1, 2, 3, 4, 5])
print(np.flip(a1)) # [5 4 3 2 1]

a2 = np.arange(1, 7).reshape((2, 3))
print(a2)

"""
[
  [1 2 3]
  [4 5 6]
]
"""

print(np.flip(a2))

"""
[
  [6 5 4]
  [3 2 1]
]
"""

print(np.flip(a2, axis=0))

"""
[
  [4 5 6]
  [1 2 3]
]
"""

print(np.flip(a2, axis=1))

"""
[
 [3 2 1]
 [6 5 4]
]
"""

################
# ravel() vs flatten
# ravel() creates a copy which is a reference the original array. Memory efficient but changes made will reflect in original array
# flatten() creates a new copy
################

print(a2.ravel())   # [1 2 3 4 5 6]
print(a2.flatten()) # [1 2 3 4 5 6]