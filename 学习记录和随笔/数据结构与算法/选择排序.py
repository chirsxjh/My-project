#!/usr/bin/env python
# coding:utf-8
arr = [7, 4, 3, 67, 34, 1, 8]  # length = 7

def select_sort(arr):
    n = len(arr)
    for j in range(n-1):
        min = j
        for i in range(j+1, n):
            if arr[min] > arr[i]:
                min = i
        arr[min], arr[j] = arr[j], arr[min]
select_sort(arr)
print(arr) 
