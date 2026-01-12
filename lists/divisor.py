# Write a function `divisors(num)` that accepts a number.
# The function should return a list containing all positive numbers that divide num exactly.

# Example:
# divisors(15) #-> [1, 3, 5, 15]
# divisors(7) #-> [1, 7]
# divisors(24) #-> [1, 2, 3, 4, 6, 8, 12, 24]

def divisors(num):
    num_divisible = []
    for n in range(1 , num + 1):
        if num % n == 0:
            num_divisible.append(n)
    return num_divisible

divisors(15)
divisors(7)
divisors(24)