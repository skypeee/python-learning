'''
@Author: skypeee
@LastEditors: skypeee
@Description: file content
@Date: 2019-09-10 09:55:52
'''
def countingSort(alist):
    """
    计数排序
    """
    maxNumber = max(alist) + 1
    countingList = [0 for i in range(maxNumber)]
    for i in alist:
        countingList[i] += 1
    tmp = 0
    for j in range(len(countingList)):
        countingList[j] += tmp
        tmp = countingList[j]
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
    tmp = 0
    for j in range(len(countingList)):
        countingList[j] += tmp
        tmp = countingList[j]
    result = []
    for i in range(len(countingList)):
        if i == 0:
            for j in range(countingList[i]):
                result.append(minNumber)
        else:
            for j in range(countingList[i] - countingList[i-1]):
                result.append(minNumber+i)
    return result
countingSort([1,6,3,3,5,7,9,2,2,3,5,6,7,8,1,2,3,4,6,8,9])
# print(countingSort([1,6,5,7,9,2,2,5,6,7,8,1,2,4,6,8,9]))

def sort(a):
    n=len(a)
    b=[None]*n
    for i in range(n):
        p=0
        q=0
        for j in range(n):
            print("a[j]",a[j],"a[i]" ,a[i])
            if a[j]<a[i]:
                p+=1
                print("p", p)
            elif a[j]==a[i]:
                q+=1
                print("q", q)
        for k in range(p,p+q):
            b[k]=a[i]
            print(b)
    print(b)
sort([2,1,3])

