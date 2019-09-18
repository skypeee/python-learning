'''
@Author: skypeee
@LastEditors: skypeee
@Description: file content
@Date: 2019-09-18 15:20:52
'''
def selectionSort(alist):
    """
    parameter:需要排序的列表
    return:排序后的列表
    """
    for i in range(len(alist)):
        minIndex = i
        for j in range(i+1, len(alist)):
            if alist[j] < alist[minIndex]:
                minIndex = j
        alist[i], alist[minIndex] = alist[minIndex], alist[i]
    return alist

print(selectionSort([3,6,1,3,5,6,8,9,5,3,2]))
