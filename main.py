from kmp import kmp
from filtterPattern import getFirstValidPattern
from naive import naiveMatch

ptns = [] # list of patterns
s = [] # string
outputArr = [] # store otputs

with open("input.txt", "r") as file:
    s = file.readlines()

with open("patterns.txt", "r") as file:
    ptns = file.readlines()
    ptns = [ptn.strip("\n") for ptn in ptns]

for ptn in ptns:
    for lineNum, line in enumerate(s):
        temp = []
        # filttering the pattern
        subPtn = getFirstValidPattern(ptn)
        if len(subPtn) == 0: # symbols are at the first of the pattern
            naiveMatch(line, ptn, temp)
        else:
            kmp(line, ptn, subPtn, temp)
        if temp != []:
            outputArr.append([temp, lineNum + 1, ptn])
    outputArr.append([])


with open("output.txt", "w") as file:
    for result in outputArr:
        print(result)
        if result == []:
            file.write("\n")
            continue
        for index in result[0]:
            temp = f"Patter: {result[2]}, Line number: {result[1]}, Index number: {index}"
            file.write(temp + "\n")
