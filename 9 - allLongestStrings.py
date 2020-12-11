# https://app.codesignal.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL
def allLongestStrings(inputArray):
    longestWords = []
    lenLongest = len(inputArray[0])
    for word in inputArray:
        if len(word) > lenLongest:
            lenLongest = len(word)
    
    for wordL in inputArray:
        if len(wordL) == lenLongest:
            longestWords.append(wordL)
    return longestWords

print(allLongestStrings(["a", "abc", "cbd", "zzzzzz", "a", "abcdef", "asasa", "aaaaaa"]))