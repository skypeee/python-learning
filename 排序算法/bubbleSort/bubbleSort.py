'''
@Author: skypeee
@LastEditors: skypeee
@Description: file content
@Date: 2019-08-29 22:36:40
'''
def bubble(alist):
    for i in range(len(alist)-1,0,-1):
        for j in range(i):
            if alist[j] < alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist

# print(bubble([5,1,3,7,9]))

# 第一次优化
def bubble1(alist):
    for i in range(len(alist)-1, 0, -1):
        isChanged = False
        for j in range(i):
            if alist[j] < alist[j+1]:
                alist[j] , alist[j+1] = alist[j+1], alist[j]
                isChanged = True
        if not isChanged:
            return alist
    return alist

# print(bubble1([7,8,6,5,4,3,2,1]))

# 第二次优化
def bubble2(alist):
    position = len(alist)-1
    for i in range(len(alist)-1, 0, -1):
        print("alist:", alist)
        isChanged = False
        for j in range(position):
            if alist[j] < alist[j+1]:
                alist[j] , alist[j+1] = alist[j+1], alist[j]
                isChanged = True
                position = j
        if not isChanged:
            return alist
    return alist

print(bubble2([7,9,6,8,4,3,2,1]))