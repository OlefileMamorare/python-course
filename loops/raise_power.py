#Write a function `raise_power(base, exponent)` that returns the result of
# base raised to the exponent using loops (do not use ** operator or math.pow).

# example: raise_power(2 , 5) = 32

def raise_power(base, exponent):
    result = base
    for i in range(1 , exponent):
        result = result * base
    return result

raise_power(7 , 2)
