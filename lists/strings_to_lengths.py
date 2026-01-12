# Write a function `strings_to_lengths(strings)` that accepts a list of strings.
# The function should return a new list containing the lengths of each string.

# Example: strings_to_lengths(["belly", "echo", "irony", "pickled"]) -> [5, 4, 5, 7]
# strings_to_lengths(["on", "off", "handmade"]) #-> [2, 3, 8]

def strings_to_lengths(strings):
    length_count = []
    for str in strings:
        length_count.append(len(str))
    return length_count

strings_to_lengths(["on", "off", "handmade"])