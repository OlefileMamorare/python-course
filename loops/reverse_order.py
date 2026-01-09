def reverse_iterate(text):
    for char in range(len(text) - 1 , -1 , -1):
        print(text[char])

reverse_iterate("hello")