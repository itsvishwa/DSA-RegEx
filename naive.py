from regex import regexCompute

def naiveMatch(s, ptn, temp):
    for i in range(len(s)):
        if regexCompute(s, ptn, i, 0):
            temp.append([i])
