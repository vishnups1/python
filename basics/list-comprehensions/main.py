"""
[part-1 part-2 part3 part4(optional)]

part4 -> Condition (Optional)
part3 -> original_list
part2 -> for item in original_list
part1 -> operation or transformation
"""

#############
# Example 1:
#############

# nums = [1, 2, 3, 4, 5]
# squared_regular = []

# for num in nums:
#     square = num * num
#     squared_regular.append(square)

# squared_lc = [num * num for num in nums]

#############
# Example 2:
#############

# tv_shows = [
#     "friends", "parks and recreation", "the office", "30 rock"
# ]

# tv_shows_cap = [show.title() for show in tv_shows]

# print(tv_shows_cap)

#############
# Example 3: Working with Conditionals
#############

# tv_shows = [
#     "friends", "parks and recreation", "the office", "30 rock"
# ]

# shows_with_more_than_10chars = [show.title() for show in tv_shows if len(show) > 10]

# print(shows_with_more_than_10chars)

#############
# Example 3: Generate new lists from scratch
#############

# squares = [n*2 for n in range(1, 10)]


"""
List comprehensions also has performance benfits when its compared to for loops.
"""

#############
# Example 4: performance benifits
#############

from time import perf_counter

t1 = perf_counter()
[n*2 for n in range(1, 100000001)]
t2 = perf_counter()
print(f"Completed in {t2-t1} seconds") # Completed in 1.8616399159654975 seconds

t1 = perf_counter()
for n in range(1, 100000001):
    x = n*2
t2 = perf_counter()
print(f"Completed in {t2-t1} seconds") # Completed in 3.389499875018373 seconds