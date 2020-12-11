# https://app.codesignal.com/arcade/intro/level-2/bq2XnSr5kbHqpHGJC
def makeArrayConsecutive2(statues):
    return (max(statues) - min(statues) - len(statues)) + 1

print(makeArrayConsecutive2([6, 2, 3, 8]))