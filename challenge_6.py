# Instructions:
# 1. Create a custom exception class called `InvalidInputError` that inherits
#    from `ValueError`.
# 2. In the `validate_input` function, raise an `InvalidInputError` if the
#    input string contains any non-alphanumeric characters or is longer
#    than 10 characters.
# 3. In the `process_data` function, call `validate_input` within a
#    try...except block.
# 4. If an `InvalidInputError` is caught, print an error message indicating
#    the invalid input.
# 5. Why: Demonstrates creating custom exceptions for specific validation
#    scenarios, improving code readability and maintainability.

def process_list(func, my_list):
  """Applies a function to each element of a list.

  Args:
    func: The function to apply.
    my_list: The list to process.

  Returns:
    A new list with the function applied to each element.
  """
  new_list = []
  for item in my_list:
      new_list.append(func(item))
  return new_list

# Different functions to apply


def square(x):
  """Returns the square of a number."""
  return x * x


def double(x):
  """Returns twice the value of a number."""
  return x * 2


def add_one(x):
  """Returns a number incremented by one."""
  return x + 1


# Example usage with different functions
numbers = [1,5,6,2,6,2,6,23,4,76,9]

squared_numbers = process_list(square, numbers)
print("Squared numbers:", squared_numbers)  # Output:

doubled_numbers = process_list(double, numbers)
print("Doubled numbers:", doubled_numbers)  # Output:

incremented_numbers = process_list(add_one, numbers)
print("Incremented numbers:", incremented_numbers)  # Output:
