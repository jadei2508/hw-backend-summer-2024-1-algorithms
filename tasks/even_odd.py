__all__ = ("even_odd",)


def even_odd(numbers: list[int]) -> float:
    """Определяет отношение суммы четных элементов списка
    к сумме нечетных.

    Example:
        >> even_odd([1, 2, 3, 4, 5])
        0.6667
    """
    evenSum = 0
    oddSum = 0
    try:
        if arr.count == 0:
            return 0;
 
        for i in arr:
            if i % 2:
                evenSum += i
            else:
                oddSum += i
    except ZeroDivisionError:
        return 0
    if oddSum == 0:
        return 0
    return evenSum / oddSum
