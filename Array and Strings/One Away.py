def OneEditAway(s1, s2):
    if len(s1) == len(s2):
        return oneEditReplace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return oneEditInsert(s1, s2)
    elif len(s1) - 1 == len(s2):
        return oneEditInsert(s2, s1)

def oneEditReplace(s1, s2):
    foundDifference = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if foundDifference:
                return False
            foundDifference = True
    return True

def oneEditInsert(s1, s2):
    index1, index2 = 0,0
    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True

print(OneEditAway('pale','bae'))