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

print(selectionSort([2,3,8,5,3,1,4,6,7]))
def dominantIndex(nums):
    maxindex = 0
    smallMaxNum = 0
    if len(nums) <= 1:
        return 0
    for i in range(len(nums)):
        if nums[i] >= nums[maxindex]:
            if i != 0:
                smallMaxNum = nums[maxindex]
            maxindex = i
        elif nums[i] > smallMaxNum:
            smallMaxNum = nums[i]
    if nums[maxindex] > smallMaxNum * 2:
        return maxindex
    else:
        return -1

print(dominantIndex([0,0,1,2]))