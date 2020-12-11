# https://app.codesignal.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ
def isLucky(n):
    firstHalf = 0
    secondHalf = 0
    strNum = str(n)
    for i, num in enumerate(strNum):
        if i < len(strNum) / 2:
            firstHalf+=int(num)
        else:
            secondHalf+=int(num)
    if firstHalf == secondHalf:
        return True
    return False

print(isLucky(1230))
print(isLucky(239017))
print(isLucky(134008))
