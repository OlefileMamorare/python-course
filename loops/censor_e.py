# Write a function `censor_e(text)` that returns a new string where all 'e' characters
# are replaced with '*'.

# Example:
#censor_e("speedy")  -> 'sp**dy'

def censor_e(text):
    result = ""
    for i in range(len(text)):
        if text[i] == "e":
            result = result + "*"
        else:
            result = result + text[i]
    return result

censor_e("heat")