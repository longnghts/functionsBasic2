#1
def countdown(num):
    y = []
    x = num
    while (x >= 0):
        y.append(x)
        x = x - 1
    print(y)

countdown(10)

#2
def printNumbers(nums):
    print(lists[0])
    return(lists[1])
lists = [1,2]
print(printNumbers(lists))

#3
def firstPlusLength(list):
        x = numberList[0] + len(numberList)
        print(x)

numberList = [1,2,3,4,5,6]
firstPlusLength(numberList)

#4
lists = [1,3,5,2,4,6]
def greaterThanSecond(lists):
    result = []
    if len(lists) < 2:
        return False
    for x in range(0,len(lists), 1):
        if lists[1] < lists[x]:
            result.append(lists[x])

    print(len(result))
    return(result)

print(greaterThanSecond(lists))

#5
def settingLength(size, value):
    arr = [value]*size
    print(arr)

settingLength(5,7)
