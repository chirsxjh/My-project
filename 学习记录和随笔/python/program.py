def ADD(x, list=[]):
    list.append(x)
    return list

list1 = ADD(10)
list2 = ADD(123, [])
list3 = ADD('a')

print "list1 = %s" %list1
print "list2 = %s" %list2
print "list3 = %s" %list3