# Write a function `maximum(numbers)` that accepts a list of numbers.
# The function should return the largest number in the list.
# If the list is empty, return None.

# Example:
# maximum([5, 6, 3, 7]) -> 7
# maximum([17, 15, 19, 11, 2]) -> 19
# maximum([]) -> None

def maximum(numbers):
    if not numbers:
        return None

    larger = numbers[0]

    for num in numbers:
        if num > larger:
            larger = num

    return larger

maximum([5, 6, 3, 7])
maximum([17, 15, 19, 11, 2])
maximum([])