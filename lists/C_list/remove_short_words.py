# Write a function `remove_short_words(sentence)` that accepts a string containing a sentence.
# The function should return a new sentence where all words shorter than 4 characters are removed.

# Example:
# remove_short_words("knock on the door will you") -> 'knock door will'
# remove_short_words("a terrible plan") -> 'terrible plan'
# remove_short_words("run faster that way") -> 'faster that'

def remove_short_words(sentence):

    words_list = sentence.split()
    new_list = ""
    
    for word in words_list:
        if len(word) >= 4:
            new_list = new_list + word + " "
                
    return new_list.strip()

remove_short_words("knock on the door will you")
remove_short_words("a terrible plan")
remove_short_words("run faster that way")
    