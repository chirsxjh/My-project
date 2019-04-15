#_*_ coding:utf-8 _*_
import numpy as np
import pdb
i = 0

dict= {'name': 'xiaoming', 'age':'3', 'grade':'5' }
dict('name')

'''

def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)//2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)


if __name__ == '__main__':
   a = []
   wait_sort = {1: 1770, 2: 3335, 3: 1034, 4: 1027, 5: 1772, 6: 1019, 7: 43, 8: 135, 9: 3, 10: 5, 11: 8}
   for i in range(1, len(wait_sort)+1):
      a.append(wait_sort[i])
   a = merge_sort(a)
   print a
   for j in range(0, len(a)):
      for i in range(1, len(wait_sort)):
         if a[j] == wait_sort[i]:
            print i


elements = [20, 30 ,40 , 50 ]
#对应的权值列表
weights = [0.4, 0.3, 0.2, 0.1]


print np.average(elements, weights=weights)

i = 11
wait_sort = {}

x = {1: 21, 2: 10, 3: 9, 4: 7, 5: 8, 6: 8, 7: 13, 8: 7, 9: 8, 10: 18, 11: 22}
y = {1: 5693, 2: 10713, 3: 3136, 4: 93, 5: 3083, 6: 3067, 7: 5565, 8: 0, 9: 0, 10: 0, 11:0 }
z = {1: 77, 2: 160, 3: 221, 4: 279, 5: 365, 6: 0, 7: 414, 8: 489, 9: 0, 10: 0, 11: 0} 
w = {1: 33, 2: 72, 3: 317, 4: 317, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}
for j in range(1, i+1):
   #pdb.set_trace()
   elements = [x[j], y[j], z[j], w[j]]
   weights = [0.4, 0.1, 0.2, 0.3]
   
   wait_sort[j] = [int(np.average(elements, weights=weights))]
   return

  #[1766, 3326, 1033, 1023, 1769, 1019, 41, 135, 3, 5, 8]
  '''