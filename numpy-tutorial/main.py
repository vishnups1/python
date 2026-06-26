from matplotlib import axes
import numpy as np
import matplotlib.pyplot as plt

def main():

    #########
    # Scalar
    #########

    # a = np.array(5)
    # print(a.shape)
    # print(a.ndim)
    # print(a)

    ###########
    # 1D Array
    ###########

    # b = np.array([1, 2, 3])
    # print(b.shape)
    # print(b.ndim)
    # print(b)

    ###########
    # 2D Array
    ###########

    """
    [
      [1, 2, 3]
      [1, 2, 3]
    ]
    """

    # c = np.array([[1, 2, 3], [1, 2, 3]])
    # print(c.shape)
    # print(len(c.shape))
    # print(c.ndim)
    # print(c)

    ###########
    # 3D Array
    ###########

    """
    [
      [
        [1, 2, 3]
        [1, 2, 3]
      ]
      [
        [1, 2, 3]
        [1, 2, 3]
      ]
    ]
    """

    # d = np.array(
    #     [
    #         [
    #             [1, 2, 3],
    #             [1, 2, 3]
    #         ],
    #         [
    #             [1, 2, 3],
    #             [1, 2, 3]
    #         ]
    #     ]
    # )
    # print(d.shape)
    # print(d.ndim)
    # print(d)

    #############################################
    # Create an Array Initialize to Zeros or Ones
    #############################################

    # a = np.zeros(shape=(1, 2, 2)) # hey can you create a 3D array with one 2x2 2D array?
    # print(a) # a 3D array containing one 2x2 matrix

    # b = np.ones(shape=(1, 2, 2))
    # print(b)

    #############################################################
    # Create an Array of Particular Size and Don't Initialize it
    #############################################################

    # c = np.empty(shape=(2,2))
    # print(c)

    ###############################################################################
    # arange: Create an array with evenly spaced intervals (start, end, step-size)
    ###############################################################################

    # d = np.arange(2, 10, 3)
    # print(d)

    #################################################################################################
    # linspace: Create an array with values that are linearly spaced ((start, end, number_of_values)
    #################################################################################################

    # e = np.linspace(10, 20, 5, dtype=np.int32)
    # print(e)
    # print(e.dtype)

    #########
    # Sorting
    #########

    # a = np.array([[20,   4,  18], [5,  19,   3]])

    """
    axis=0 move down the rows  (vertical direction)
    axis=1 move across columns (horizontal direction)
    """

    # print(np.sort(a, axis=0))
    # print(np.sort(a, axis=1))

    """
    lexsort
    It performs an indirect sort (returns indices, not the sorted data).
    """
    
    # a = np.array(["car", "apple", "cat"])
    # print(np.lexsort((a,))) # [1, 0 ,2]

    # names = np.array(["vishnu", "pradeep", "venkat"])
    # ages = np.array([10, 15, 35])

    """
    Primary Key   = names
    Secondary Key = ages
    """

    # index=np.lexsort((ages, names))
    # print(names[index])
    # print(ages[index])

    ###############
    # Concatenation
    ###############

    # a1 = np.array([[1, 2], [3, 4]])
    # a2 = np.array([[1, 2], [1, 1]])

    # print(np.concat((a1, a2), axis=0))
    # print(np.concat((a1, a2), axis=1))

    ###################
    # Reshaping Arrays
    ###################

    """
    order="F" => Vertical
    order="C" => Horizontal

      axis=1 → move across columns
      [1 2 3]
      [4 5 6]
      axis=0
      ↓ 
      move down rows 
    """

    # a = np.array(
    #   [
    #     [4, 3, 2, 1],
    #     [1, 2, 3, 4]
    #   ]
    # )
    # print(np.reshape(a, (4,2)))
    # print(np.reshape(a, (4,2), order="F"))
    # print(np.reshape(a, (4,2), order="C"))

    #########################
    # Add new Axis to arrays
    #########################

    """
    np.newaxis
    np.expand_dims
    """

    # a1 = np.arange(1, 6)
    # print(a1)                  # [1 2 3 4 5]
    # print(a1.shape)            # (9,)

    # a2 = a1[np.newaxis, :]     # [[1 2 3 4 5]]
    # print(a2)                  # (1, 9)
    # print(a2.shape)
 
    # a1=a[np.newaxis, :]
    # print(a1)                 # [[1 2 3 4 5 6]]
    # print(a1.ndim)            # 2

    # z=a1[np.newaxis, :]
    # print(z)                  # [[[1 2 3 4 5 6]]]
    # print(z.ndim)             # 3

    # a2=a[:, np.newaxis]
    # print(a2)                 # 2
    # """
    # [[1]
    #  [2]
    #  [3]
    #  [4]
    #  [5]
    #  [6]]
    # """
    # print(a2.ndim)

    #########
    # argmin
    #########

    # a = np.array([[5, 1, 8], [2, 4, 7]])
    # print(np.argmin(a))         # This flattens to 1D array [5, 1, 8, 2, 4, 7] and send the index 1 which is the minimum
    # print(np.argmin(a, axis=0)) # Compare column wise # [1, 0, 1]
    # print(np.argmin(a, axis=1)) # Compare row wise # [1 0]

    #########################
    # Slicing & Indexing
    #########################

    # a1 = np.array([1, 2, 3, 4, 5])
    # print(a1[0])    # 1
    # print(a1[0:5])  # [1 2 3 4 5]
    # print(a1[0:])   # [1 2 3 4 5]
    # print(a1[:-1])  # [1 2 3 4]

    ######################
    # Conditional Slicing
    ######################

    # print(a1[a1>2]) # [3 4 5]

    # a2 = np.array([
    #   [1, 2, 3, 4, 5],
    #   [6, 7, 8, 9, 10],
    #   [11, 12, 13, 14, 15]
    # ])

    # print(a2>5)
    """
    [
      [False False False False False]
      [ True  True  True  True  True]
      [ True  True  True  True  True]
    ]
    """
    # print(a2[a2>5]) # [ 6  7  8  9 10 11 12 13 14 15]

    # divisible_by_2=a2[a2%2 == 0]
    # print(divisible_by_2)  # [ 2  4  6  8 10 12 14]

    # # return indexes instead of values.

    # print(np.nonzero(a2>10))     # (array([2, 2, 2, 2, 2]), array([0, 1, 2, 3, 4]))
    # print(np.nonzero((a2%2)==0)) # (array([0, 0, 1, 1, 1, 2, 2]), array([1, 3, 0, 2, 4, 1, 3]))

    ###############################################
    # Horizontal, Vertical Stack, Horizontal Split
    ###############################################

    # a1 = np.array([[1, 1], [2, 2]])
    # a2 = np.array([[3, 3], [4, 4]])

    # print(a1+a2)

    # print(np.vstack((a1, a2)))

    """
    [
      [1 1]
      [2 2]
      [3 3]
      [4 4]
    ]
    """

    # print(np.hstack((a1, a2)))

    """
    [
      [1 1 3 3]
      [2 2 4 4]
    ]
    """

    # a1 = np.arange(1, 25).reshape(2, 12)
    # print(a1)

    """
    [
      [ 1  2  3  4  5  6  7  8  9 10 11 12]
      [13 14 15 16 17 18 19 20 21 22 23 24]
    ]
    """

    # print(np.hsplit(a1, 3))

    """
    [
      [ 1,  2,  3,  4]
      [13, 14, 15, 16]
    ]

    [
      [ 5,  6,  7,  8]
      [17, 18, 19, 20]
    ]

    [
      [ 9, 10, 11, 12]
      [21, 22, 23, 24]
    ]
    """
    
    # print(np.hsplit(a1, (3, 4))) # Split at 3rd and 4th Column

    """
    [
      [ 1,  2,  3]
      [13, 14, 15]
    ]

    [
      [ 4]
      [16]
    ]

    [
      [ 5,  6,  7,  8,  9, 10, 11, 12]
      [17, 18, 19, 20, 21, 22, 23, 24]
    ]
    """

    #############
    # View, Copy
    #############

    """
    Whenever we are splitting and creating new arrays, we are creating shallow copies,
    both of them are pointing to the same memory location.
    """

    a1 = np.arange(1, 5)
    # print(a1) # [1 2 3 4]
    # b1 = a1

    # b1[0] = 5
    # print(a1) # [5 2 3 4]

    # To create deep copies use copy() function

    b1 = a1.copy()
    b1[0] = 11
    print(a1) # [1 2 3 4]
    print(b1) # [11  2  3  4]

if __name__ == "__main__":
    main()
