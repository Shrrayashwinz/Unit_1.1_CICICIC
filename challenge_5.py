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

def validate_input(input_string: str) -> None:
    """Validates the input string to meet specific criteria.

    Args:
        input_string (str): The input string to validate.
    """
    pass  # Implement your validation logic here


def process_data(data: list[str]) -> None:
    """Processes a list of strings, validating each input.

    Args:
        data (list[str]): A list of strings to process.
    """
    for input_string in data:
        validate_input(input_string)
        print(f"Processed: {input_string}")


# Test Cases
data_list = ["valid1", "invalid!", "another_valid", "toolong12345", ""]
process_data(data_list)
# Expected Output:
# Processed: valid1
# Error: Invalid input: invalid!
# Processed: another_valid
# Error: Invalid input: toolong12345
# Processed:
