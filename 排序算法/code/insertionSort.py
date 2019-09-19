'''
@Author: skypeee
@LastEditors: skypeee
@Description: insertSort
@Date: 2019-09-19 15:15:43
'''
def insertSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key <= arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
arr = [8,1,6,7,4,3,2]
insertSort(arr)
print(arr)