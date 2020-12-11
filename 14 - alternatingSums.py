# https://app.codesignal.com/arcade/intro/level-4/cC5QuL9fqvZjXJsW9
def alternatingSums(a):
    result = [0,0]
    if len(a) < 2:
        result[0] = a[0]
        return result
    sumWeight1 = a[0]
    sumWeight2 = a[1]
    ind1 = 2
    ind2 = 3
    while ind1 < len(a):
        sumWeight1 += a[ind1]
        if ind2 < len(a):
            sumWeight2 += a[ind2]
            ind2+=2
        ind1+=2
    result[0]=sumWeight1
    result[1]=sumWeight2
    return result

print(alternatingSums([50, 60, 60, 45, 70]))
print(alternatingSums([100, 50]))
print(alternatingSums([100, 50]))
print(alternatingSums([80]))