# https://app.codesignal.com/arcade/intro/level-3/D6qmdBL2NYz49XHwM
def sortByHeight(a):
    auxA = [x for x in a if x != -1]
    auxA.sort()
    index = 0
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = auxA[index]
            index+=1
    return a


sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180])