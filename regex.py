def regexCompute(s, ptn, i, j):
    if j == len(ptn) - 1:
        return True
    if i == len(s) - 1:
        return False
    i += 1
    j += 1
    astrictCount = 0
    while j < len(ptn):
        # alpha numeric checck
        if ptn[j].isalnum():
            if i >= len(s):
                return False
            if s[i] != ptn[j]:
                if j+1 < len(ptn):
                    if ptn[j+1] == "*":
                        j += 1
                        continue
                    elif ptn[j+1] == "?":
                        j += 2
                        continue
                return False
            else:
                i += 1
                j += 1
        # dot check -> matches any
        elif ptn[j] == ".":
            if i >= len(s):
                if j+1 < len(ptn) and ptn[j+1] in ["?", "*"]:
                    j += 2
                    continue
                return False
            if s[i] == "\n":
                return False
            else:
                i += 1
                j += 1
        # astric check -> zero or many
        elif ptn[j] == "*":
            prev = s[i-1]
            while i < len(s):
                if s[i] == prev:
                    astrictCount += 1
                    i += 1
                else:
                    break
            j += 1
            while astrictCount > 0 and j < len(ptn) and ptn[j] == prev:
                astrictCount -= 1
                j += 1
        # plus check -> one or more
        elif ptn[j] == "+":
            prev = s[i-1]
            while i < len(s):
                if s[i] == prev:
                    i += 1
                else:
                    break
            j += 1
        # question check - zero or one
        elif ptn[j] == "?":
            j += 1
    
    if j < len(ptn):
        return False
    else:
        return True
    
