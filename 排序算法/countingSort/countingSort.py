def countingSort(alist):
    """
    计数排序
    """
    maxNumber = max(alist) + 1
    countingList = [0 for i in range(maxNumber)]
    for i in alist:
        countingList[i] += 1
    print(countingList)
    tmp = 0
    for j in range(len(countingList)):
        countingList[j] += tmp
        tmp = countingList[j]
    print(countingList)
    return countingList

countingSort([1,6,3,3,5,7,9,2,2,3,5,6,7,8,1,2,3,4,6,8,9])

def countingSort(alist):
    """
    计数排序
    第一次优化
    """
    minNumber = min(alist)
    lenth = max(alist) - minNumber + 1
    countingList = [0 for i in range(lenth)]
    for i in alist:
        countingList[i-minNumber] += 1
    print(countingList)
    tmp = 0
    for j in range(len(countingList)):
        countingList[j] += tmp
        tmp = countingList[j]
    print(countingList)
    return countingList
countingSort([1,6,3,3,5,7,9,2,2,3,5,6,7,8,1,2,3,4,6,8,9])
