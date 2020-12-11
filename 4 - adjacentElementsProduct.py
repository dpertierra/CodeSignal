# https://app.codesignal.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m
def adjacentElementsProduct(inputArray):
    totalMax = -1001
    currentMax = -1001
    # Repurposing Kadane's Algorithm
    for i in range(len(inputArray)-1):
        currentMax = max(inputArray[i] * inputArray[i+1], currentMax)
        totalMax = max(totalMax, currentMax)
    return totalMax

print(adjacentElementsProduct([5, 1, 2, 3, 1, 4]))