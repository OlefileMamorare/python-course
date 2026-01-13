# Write a function `alternating_caps(sentence)` that accepts a string containing a sentence.
# The function should return the sentence where words alternate between lowercase and uppercase.

# Example:
# alternating_caps("take them to school") -> 'take THEM to SCHOOL'
# alternating_caps("What did ThEy EAT before?") -> 'what DID they EAT before?'

def alternating_caps(sentence):
    word_split = sentence.split(" ")
    new_string = ""

    for word in word_split:
        if (word_split.index(word) % 2 != 0):
            new_string = new_string + word.upper() + " "
        else:
            word = word.lower()
            new_string += word + " "

    return new_string.strip()

alternating_caps("take them to school")
alternating_caps("What did ThEy EAT before?")
alternating_caps("what are you eating today my boy?")