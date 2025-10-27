
# Instructions:
# 1. Add a try...except block to catch the IndexError.
# 2. Print an informative message if the index is out of range.
# 3. Why: This prevents the program from crashing when accessing an invalid index.

# Explanation:
# IndexError occurs when you try to access an element of a sequence 
# (like a list) using an index that is outside the valid range of indices 
# for that sequence.

# Code that will cause an exception:
my_list = [1, 2, 3, 4, 5, 7, 12, 58, 17272]
try:
    value = my_list[5]  # Index out of range 
    print(value)
except IndexError as ie:
    print(f'The exception is: {ie}')

else:
    print("My accessed value is", value)

finally:
    print("Execution is complete!")


