# Write a function `fizz_buzz(max_num)` that prints all numbers <= max_num
# that are divisible by 3 or 5 but not both.
# The function does not return a value, just prints.

def fizz_buzz(max_num):
    for i in range(1, max_num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("NOP")
        elif i % 3 == 0 or i % 5 == 0:
            print(i)

fizz_buzz(33)