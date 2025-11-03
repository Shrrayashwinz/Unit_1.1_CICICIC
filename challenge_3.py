# ZeroDivisionError is raised when you attempt to divide a number
# by zero, which is mathematically undefined.
# 
# Instructions:
# 1. Capture the ZeroDivisionError.
# 2. if exception is thrown return None
# 3. else return answer
# 4. Update documentation and the typehints so it is accurate for the function


def divide(a: float, b: float)  -> float | None:

    a = float(input("Enter numerator: "))
    b = float(input("Enter denominater: "))
    """
    Divides two numbers, handling division by zero.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        The result of a / b, or None if division by zero.

    Raises:
        ZeroDivisionError: If the denominator is zero.
    """
    try:
        return a / b
    except ValueError as ve:
        print(f"I am afraid this is not divisble. The exepction is: {ve}")
        return None
    except ZeroDivisionError as zde:
        print(f"WE CANT DIVDE BY ZERO U JERK! The exeption, you moron, is {zde}")
        return None
     


