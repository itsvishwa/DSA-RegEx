from regex import regexCompute

def kmp(s, ptn, subPtn, outputArr):
    lpsArr = [0] * len(subPtn)

    computeLPS(lpsArr, subPtn)
    
    i = 0 # for string
    j = 0 # for pattern
    while i < len(s):
        if s[i] == subPtn[j]:
            if j == (len(subPtn) - 1):
                #pattern has matched. now check the rest
                if regexCompute(s, ptn, i, j):
                    # if all pattern has matched
                    outputArr.append([i - j])
                i += 1
                j = lpsArr[j]
            else:
                i += 1
                j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lpsArr[j-1]


# creating pi array
def computeLPS(lpsArr, ptn):
    lenOfPtn = len(ptn)
    left, right = 0, 1
    lpsArr[left] = 0

    while right < lenOfPtn:
        if ptn[left] == ptn[right]:
            lpsArr[right] = left + 1
            right += 1
            left += 1
        else:
            if left != 0:
                left = lpsArr[left - 1]
            else:
                lpsArr[right] = 0
                right += 1


