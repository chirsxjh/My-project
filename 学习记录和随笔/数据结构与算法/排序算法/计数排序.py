
max = 10
min = 0
countArray = [0 for i in range(max - min + 1)]
#print (sort_array)  
array = [9, 2, 8, 5, 1, 8, 6, 9, 5, 8, 1, 5, 8, 3, 4, 7, 0, 6, 2, 10]
for i in array:
    countArray[i - min] = countArray[i - min] + 1


sum = 0
for i,value in enumerate(countArray):
    sum = sum + value
    countArray[i] = sum
print (countArray)

sortArray = [0 for i in array]
print (sortArray)
for i in array:
    sortArray[countArray[i - min] - 1] = i
    countArray[i - min] = countArray[i - min] - 1

print (sortArray)
