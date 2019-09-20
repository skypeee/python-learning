'''
@Author: skypeee
@LastEditors: skypeee
@Description: shellSort
@Date: 2019-09-20 11:08:52
'''
def shellSort(alist):
    if len(alist) <= 1:
        return alist
    h = len(alist) // 2
    while h > 0:
        for i in range(h,len(alist)):
            tmp = alist[i]
            j = i
            while j >= h and alist[j-h] > tmp:
                alist[j] = alist[j-h]
                j -= h
            alist[j] = tmp
        h = h//2
    return alist

print(shellSort([9,4,6,8,3,2,5,1,7]))
