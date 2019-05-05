# -*-coding:utf-8-*-
'''
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
'''

def bubbleSort(myList):
    #首先获取list的总长度,为之后的循环比较作准备
    length = len(myList)

    #一共进行几轮列表比较,一共是(length-1)轮
    for i in range(0,length-1):

        #每一轮的比较,注意range的变化,这里需要进行length-1-长的比较,注意-i的意义(可以减少比较已经排好序的元素)
        for j in range(0,length-1-i):

            #交换
            if myList[j] > myList[j+1]:
                tmp = myList[j]
                myList[j]=myList[j+1]
                myList[j+1] = tmp
    
    return myList



arr = [3,2,1,5,6,4,4,5,5,5]

res = bubbleSort(arr)
res.reverse()
print res[k-1]
