def remove_capitals(text):
    result = ""
    for i in range(len(text)):
        if text[i].lower() == text[i]:
            result = result + text[i]
    print(result)

remove_capitals("HellO")
