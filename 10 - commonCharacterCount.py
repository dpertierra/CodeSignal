# https://app.codesignal.com/arcade/intro/level-3/JKKuHJknZNj4YGL32
def commonCharacterCount(s1, s2):
    lettersS1 = {}
    lettersS2 = {}
    intersection = {}
    for c in s1:
        if c in lettersS1:
            lettersS1[c]+=1
        else:
            lettersS1[c] = 1
    for c in s2:
        if c in lettersS2:
            lettersS2[c]+=1
        else:
            lettersS2[c] = 1
    
    for key, value in lettersS2.items():
        if key in lettersS1:
            intersection[key] = min(lettersS1[key], value)
    return sum(intersection.values())

print(commonCharacterCount("aabcc","adcaa"))
print(commonCharacterCount("zzzz","zzzzzzz"))