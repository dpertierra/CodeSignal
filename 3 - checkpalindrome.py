# https://app.codesignal.com/arcade/intro/level-1/s5PbmwxfECC52PWyQ
def checkPalindrome(inputString):
    revsersed = inputString[::-1]
    if inputString == revsersed:
        return True
    return False

print(checkPalindrome("aabaa"))