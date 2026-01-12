# Write a function `choose_divisibles(numbers, target)` that accepts a list of numbers and a target number.
# The function should return a new list containing only the elements divisible by the target.

# Example:
# choose_divisibles([40, 7, 22, 20, 24], 4) -> [40, 20, 24]
# choose_divisibles([9, 33, 8, 17], 3) -> [9, 33]
# choose_divisibles([4, 25, 1000], 10) -> [1000]



def choose_divisibles(numbers , target):
    divisibles = []
    for num in numbers:
        if num % target == 0:
            divisibles.append(num)
        
    return divisibles

choose_divisibles([40, 7, 22, 20, 24], 4)
choose_divisibles([9, 33, 8, 17], 3)
choose_divisibles([4, 25, 1000], 10)