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

    # a = np.arange(1, 7)
    # print(a)                  # [1 2 3 4 5 6]
    # print(a.ndim)             # 1

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

if __name__ == "__main__":
    main()
