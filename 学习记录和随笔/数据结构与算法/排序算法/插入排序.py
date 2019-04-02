#!/usr/bin/env python
# coding:utf-8
def insertion_sort(list):
    n = len(list)
    for i in range(1, n):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    return list

list1 = [5,6,2,7,9,0,1,3,8,4]
print("原列表：%s" %list1)
insertion_sort(list1)
print("排序后列表：%s" %list1)