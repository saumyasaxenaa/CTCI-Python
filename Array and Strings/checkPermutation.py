def checkPermutation(str1,str2):
    count = {}
    for char in str1:
        if char not in count:
            count[char] = 0
        count[char] += 1

    for char in str2:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] == 0:
            del count[char]
    return len(count) == 0

print(checkPermutation('aba','bab'))