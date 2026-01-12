# Write a function `word_count(sentence, target_words)` that accepts a sentence string and a list of target words.
# The function should return a count of how many words in the sentence are also in target_words.

# Example:
# word_count("open the window please", ["please", "open", "sorry"]) -> 2
# word_count("drive to the cinema", ["the", "driver"]) -> 1
# word_count("can I have that can", ["can", "I"]) -> 3

def word_count(sentence , target_words):
    count = 0
    word_split = sentence.split()

    for word in target_words:
        if word in word_split:
            count = count + sentence.count(word)
    
    return count

word_count("open the window please", ["please", "open", "sorry"])
word_count("drive to the cinema", ["the", "driver"])
word_count("can I have that can", ["can", "I"])