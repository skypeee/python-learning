from random import randint
def quickSort(alist):
    """
    快速排序
    标准元素为随机选择
    使用双边选择法
    """
    if len(alist) <= 1:
        return alist
    standard = randint(0, len(alist)-1)
    alist[0], alist[standard] = alist[standard], alist[0]
    left = 0
    right = len(alist) - 1
    flag = True
    while left != right:
        if flag is True:
            if alist[right] >= alist[0]:
                right -= 1
            else:
                flag = not flag
        else:
            if alist[left] <= alist[0]:
                left += 1
            else:
                alist[left], alist[right] = alist[right], alist[left]
                flag = not flag
    return quickSort(alist[1:right+1]) + [alist[0]] + quickSort(alist[right+1:])

print(quickSort([1,3,6,7,8,2,4,6,7]))

def quickSort1(alist):
    """
    快速排序
    单边循环法
    """
    if len(alist) <= 1:
        return alist
    standard = randint(0, len(alist)-1)
    alist[0], alist[standard] = alist[standard], alist[0]
    mark = 1
    for i in range(1,len(alist)):
        if alist[i] >= alist[0]:
            continue
        else:
            alist[mark], alist[i] = alist[i], alist[mark]
            mark += 1
    return quickSort1(alist[1:mark]) + [alist[0]] + quickSort1(alist[mark:])
print(quickSort1([1,3,6,7,8,2,4,6,7]))