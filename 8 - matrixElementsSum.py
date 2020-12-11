# https://app.codesignal.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr
def matrixElementsSum(matrix):
    total = 0
    ignore = set()
    for i, row in enumerate(matrix):
        for j, numCol in enumerate(row):
            if matrix[i][j] == 0:
                ignore.add(j)
            if i == 0:
                total+=numCol
            else:
                if j not in ignore:
                    total+=numCol
    return total

print(matrixElementsSum([[1,1,1,0], 
                         [0,5,0,1], 
                         [2,1,3,10]]))