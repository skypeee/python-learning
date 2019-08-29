'''
@Author: skypeee
@LastEditors: skypeee
@Description: file content
@Date: 2019-08-29 22:36:40
'''
def bubble(alist):
    for i in range(len(alist)-1,0,-1):
        for j in range(i):
            print(j)
            if alist[j] < alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist

print(bubble([5,1,3,7,9]))