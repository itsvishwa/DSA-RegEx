def getFirstValidPattern(ptn):
    temp = ""
    for character in ptn:
        if not character.isalnum(): # if it's a symbol
            if character == "*":
                if len(temp) == 1:
                    return []
                return temp[:-1]
            elif character == "?":
                if len(temp) == 1:
                    return []
                return temp[:-1]
            else:
                return temp
        temp += character
    return temp

