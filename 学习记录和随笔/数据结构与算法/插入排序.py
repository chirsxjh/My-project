#!/usr/bin/env python
# coding:utf-8
def select_sort(li):
    n = len(li) #li列表中有n个数，下标从0到n-1
    # i从0到n-1 ，我们每次拿下标为i的数跟后面数比较 标记最小的数
    for i in range( n ):
        temp = i #用temp做临时标记，没遇见比下标temp更小的数，就用temp标记更小的数的下表
        # 从temp开始向后找到最后 找最小的数
        for j in range( temp , n ):
            #如果我们遇到比temp标记的数更小的，tamp就标记更小的数的下标
            if li[temp] > li[j] :
                temp = j
        #这次for循环之后 temp一定标记了i之后的最小的数的下标，我们把最小的数和i位置进行互换
        li[i] , li[temp] = li[temp] , li[i]

if __name__ == '__main__':
    li = [5,4,3,2,1]
    select_sort(li)
    print(li)