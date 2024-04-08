__all__ = ("is_prime",)


def is_prime(number: int) -> bool:
    """Определяет, является ли число простым.

    Example:
        >> is_prime(0):
        False
        >> is_prime(1):
        False
        >> is_prime(4):
        True
    """
    import math
    if number > 1:
        for i in range(2, int(math.sqrt(number)) + 1):
            if (number % i) == 0:
                return False
        return True
    return False
