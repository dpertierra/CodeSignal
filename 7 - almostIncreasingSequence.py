# https://app.codesignal.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG
def almostIncreasingSequence(sequence):
    droppped = False
    last = prev = min(sequence) - 1
    for num in sequence:
        if num <= last:
            if droppped:
                return False
            else:
                droppped = True
            if num <= prev:
                prev = last
            elif num >= prev:
                prev = last = num
        else:
            prev, last = last, num
    return True

print(almostIncreasingSequence([1, 3, 2]))
print(almostIncreasingSequence([40, 50, 60, 10, 20, 30]))
print(almostIncreasingSequence([10, 1, 2, 3, 4, 5]))