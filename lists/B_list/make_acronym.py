# Write a function `make_acronym(sentence)` that accepts a string containing a sentence.
# The function should return a string containing the first character of each word in the sentence.

# Example:
# make_acronym("New York") -> 'NY'
# make_acronym("same stuff different day") -> 'SSDD'
# make_acronym("Laugh out loud") -> 'LOL'
# make_acronym("don't over think stuff") -> 'DOTS'

def make_acronym(sentence):

    new_list = sentence.split()
    first_chars = ""
    
    for char in new_list:
        first_chars = first_chars + char[0]
    
    return first_chars.upper()

make_acronym("New York")
make_acronym("same stuff different day")
make_acronym("Laugh out loud")
make_acronym("don't over think stuff")