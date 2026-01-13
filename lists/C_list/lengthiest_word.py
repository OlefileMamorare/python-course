# Write a function `lengthiest_word(sentence)` that accepts a string containing a sentence.
# The function should return the longest word in the sentence.
# If there is a tie, return the word that appears later in the sentence.

# Example:
# lengthiest_word("I am pretty hungry") -> 'hungry'
# lengthiest_word("we should think outside of the box") -> 'outside'
# lengthiest_word("down the rabbit hole") -> 'rabbit'
# lengthiest_word("simmer down") -> 'simmer'

def lengthiest_word(sentence):

    word_list = sentence.split(" ")

    longest = ""

    for word in word_list:
        if len(word) > len(longest):
            longest = word

        elif len(word) == len(longest):
            longest = word
    return longest

lengthiest_word("I am pretty hungry")
lengthiest_word("we should think outside of the box")
lengthiest_word("down the rabbit hole")
lengthiest_word("simmer down")