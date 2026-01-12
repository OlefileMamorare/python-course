def bleep_vowels(str):
    vow = "aeiou"
    result = ""

    for char in str:
        if char in vow:
            result += "*"
        else:
            result += char
    return result

bleep_vowels("Olefile Mamorare")