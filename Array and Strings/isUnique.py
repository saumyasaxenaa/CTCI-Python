def isUnique(string):
    if len(string) > 128:
        return False
    charFreq = {}
    for char in string:
        if char in charFreq:
            return False
        charFreq[char] = True
    return True

print(isUnique('abcd'))