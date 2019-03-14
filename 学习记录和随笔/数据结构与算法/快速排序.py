#!/usr/bin/env python
# coding:utf-8
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)
def quickSortHelper(alist,first,last):
    #基本结束条件
    if first<last:
        #分裂为两部分
        splitpoint=partition(alist,first,last)
        #递归调用
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)
def partition(alist,first,last):
    #选定中值
    mid=alist[first]
    leftmark=first+1
    rightmark=last
    done=False
    while not done:
        while leftmark<=rightmark and alist[leftmark]<=mid:
            leftmark=leftmark+1
        while rightmark>=leftmark and alist[rightmark]>=mid:
            rightmark-=1
        #两标相错就结束移动
        if rightmark<leftmark:  
            done=True
        #左右两标指向的值交换，继续移动
        else:
            temp=alist[leftmark]
            alist[leftmark]=alist[rightmark]
            alist[rightmark]=temp
            
    temp2=alist[first]
    alist[first]=alist[rightmark]
    alist[rightmark]=temp2
    return rightmark
    
alist=[52,312,54,7,3,2]
quickSort(alist)
print(alist)
#https://blog.csdn.net/weixin_36913190/article/details/80550347