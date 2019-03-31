## 排序算法
[TOC] 
[冒泡排序](#冒泡排序)  
[选择排序](#选择排序)   
[插入排序](#插入排序)    
[希尔排序](#希尔排序)  
[快速排序](#快速排序)  
[基数排序](#基数排序)  
[桶排序](#桶排序)  
[堆排序](#堆排序)  
[归并排序](#归并排序)  
### 简介：
所谓排序，就是使一串记录，按照其中的某个或某些关键字的大小，递增或递减的排列起来的操作。排序算法，就是如何使得记录按照要求排列的方法。排序算法在很多领域得到相当地重视，尤其是在大量数据的处理方面。一个优秀的算法可以节省大量的资源。在各个领域中考虑到数据的各种限制和规范，要得到一个符合实际的优秀算法，得经过大量的推理和分析。
###算法分类
![](https://img2018.cnblogs.com/blog/849589/201903/849589-20190306165258970-1789860540.png)
### 算法复杂度
![](https://images2018.cnblogs.com/blog/849589/201804/849589-20180402133438219-1946132192.png)
### 相关概念
* 稳定：如果a原本在b前面，而a=b，排序之后a仍然在b的前面。
* 不稳定：如果a原本在b的前面，而a=b，排序之后 a 可能会出现在 b 的后面。
* 时间复杂度：对排序数据的总的操作次数。反映当n变化时，操作次数呈现什么规律。
* 空间复杂度：是指算法在计算机内执行时所需存储空间的度量，它也是数据规模n的函数。 

### 算法详细
#### 冒泡排序
冒泡排序是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。   

算法描述
* 比较相邻的元素。如果第一个比第二个大，就交换它们两个；
* 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
* 针对所有的元素重复以上的步骤，除了最后一个；
* 重复步骤1~3，直到排序完成。  
![](https://images2017.cnblogs.com/blog/849589/201710/849589-20171015223238449-2146169197.gif)
**代码**
```
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
                
        #打印每一轮交换后的列表       
        for item in myList:
            print(item)
            print("=============================")
            
print("Bubble Sort: ")
myList = [1,4,5,0,6]
bubbleSort(myList)
```
**流程图**  
![](https://wx3.sinaimg.cn/large/0071Dyx4ly1g171obcv6wj30lb0pgwfj.jpg)
#### 选择排序
选择排序(Selection-sort)是一种简单直观的排序算法。它的工作原理：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。 
**算法描述**  
n个记录的直接选择排序可经过n-1趟直接选择排序得到有序结果。具体算法描述如下：  
初始状态：无序区为R[1..n]，有序区为空；  
第i趟排序(i=1,2,3…n-1)开始时，当前有序区和无序区分别为R[1..i-1]和R(i..n）。该趟排序从当前无序区中-选出关键字最小的记录 R[k]，将它与无序区的第1个记录R交换，使R[1..i]和R[i+1..n)分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区；  
n-1趟结束，数组有序化了。
**分析**：  
表现最稳定的排序算法之一，因为无论什么数据进去都是O(n2)的时间复杂度，所以用到它的时候，数据规模越小越好。唯一的好处可能就是不占用额外的内存空间了吧。理论上讲，选择排序可能也是平时排序一般人想到的最多的排序方法了吧。
![](https://images2017.cnblogs.com/blog/849589/201710/849589-20171015224719590-1433219824.gif)
**代码**
```
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

```
**流程图**
![](https://wx4.sinaimg.cn/large/0071Dyx4ly1g171w6bcq3j30e70t6t99.jpg)

#### 插入排序
插入排序（Insertion-Sort）的算法描述是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
**算法描述***
一般来说，插入排序都采用in-place在数组上实现。具体算法描述如下：
* 从第一个元素开始，该元素可以认为已经被排序；
* 取出下一个元素，在已经排序的元素序列中从后向前扫描；
* 如果该元素（已排序）大于新元素，将该元素移到下一位置；
* 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
* 将新元素插入到该位置后；
* 重复步骤2~5。

**算法分析**
插入排序在实现上，通常采用in-place排序（即只需用到O(1)的额外空间的排序），因而在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。
![](https://images2017.cnblogs.com/blog/849589/201710/849589-20171015225645277-1151100000.gif)
**代码**
```
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

```
**流程图**  
![](https://wx1.sinaimg.cn/large/0071Dyx4ly1g1723tpu7oj30oc0srt9a.jpg)

#### 希尔排序
1959年Shell发明，第一个突破O(n2)的排序算法，是简单插入排序的改进版。它与插入排序的不同之处在于，它会优先比较距离较远的元素。希尔排序又叫缩小增量排序。
**算法描述**  
先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，具体算法描述：
选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1；
按增量序列个数k，对序列进行k 趟排序；
每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，分别对各子表进行直接插入排序。仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。
**算法分析**    
希尔排序的核心在于间隔序列的设定。既可以提前设定好间隔序列，也可以动态的定义间隔序列。动态定义间隔序列的算法是《算法（第4版）》的合著者Robert Sedgewick提出的。　
**代码**  
```
#!/usr/bin/env python
# coding:utf-8
def shell_sort(li ):
    n = len(li) #li列表中有n个数 下标从0到n-1
    gep = n//2 #设置初始步长进行分组
    #当步长大于等于1的时候 一直进行分组的插入排序
    while gep >= 1 :
        # 从gep的元素往后 一个一个元素对前面所有组跟自己处于相同位置的数进行插入排序
        for j in range( gep , n ):
            i = j   #标记下当前j的位置给i
            # 这层循环是为了回跳i所在位置，
            # 当一个新元素对前组同位置元素交换后，当前元素还需要跟再往前组的同位置元素比较决定是不是要交换
            # i - gep 能看我当前是不是第一组位置，如果是第一组位置，我前面没有组了，就不循环了，
            # 如果我是第三组，我会跳到前二组再跟第一组的相同位置元素进行比较
            while i - gep >= 0 :
                #如果当前数比前一组同位置数小，就交换数值
                if li[i] < li[i-gep] :
                    li[i] , li[i-gep] = li[i-gep] , li[i]
                    #如果我和前一组同位置元素交换了，我需要继续与再往前一组同位置元素比较是否需要交换
                    #这个操作是把我当前位置回跳到上一组的同位置
                    i -= gep
                #如果没有发生数据交换，说明前面的不用再比较了，前面的一定都比我当前数小，跳出回跳位置的循环
                else :
                    break
        #修改步长 缩小步长
        gep//=2

if __name__ == '__main__':
    li = [5,4,3,2,1]
    shell_sort(li)
    print(li)
```
**流程图**  
![](https://wx3.sinaimg.cn/large/0071Dyx4ly1g1lsv4fvtij30n90tngn2.jpg)

#### 归并排序
归并排序是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为2-路归并。 
**算法描述**    
* 把长度为n的输入序列分成两个长度为n/2的子序列；
* 对这两个子序列分别采用归并排序；
* 将两个排序好的子序列合并成一个最终的排序序列。
**算法分析**    
归并排序是一种稳定的排序方法。和选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好的多，因为始终都是O(nlogn）的时间复杂度。代价是需要额外的内存空间。
![](https://images2017.cnblogs.com/blog/849589/201710/849589-20171015230557043-37375010.gif)
**代码**
```
#!/usr/bin/env python
# coding:utf-8
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
    a = [14, 2, 34, 43, 21, 19]
    print (merge_sort(a))

```
**流程图**  
![](https://wx4.sinaimg.cn/large/0071Dyx4ly1g172foo7naj30d50qt3yv.jpg)

#### 快速排序
快速排序的基本思想：通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。
**算法描述**
快速排序使用分治法来把一个串（list）分为两个子串（sub-lists）。具体算法描述如下：  
列中挑出一个元素，称为 “基准”（pivot）；  
重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
![](https://images2017.cnblogs.com/blog/849589/201710/849589-20171015230936371-1413523412.gif)
**代码**
```
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
```
**流程图**  
![](https://wx4.sinaimg.cn/large/0071Dyx4ly1g172kl1wwhj30nw17mjte.jpg)

#### 堆排序
堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。
**算法描述**  
将初始待排序关键字序列(R1,R2….Rn)构建成大顶堆，此堆为初始的无序区；
将堆顶元素R[1]与最后一个元素R[n]交换，此时得到新的无序区(R1,R2,……Rn-1)和新的有序区(Rn),且满足R[1,2…n-1]<=R[n]；
由于交换后新的堆顶R[1]可能违反堆的性质，因此需要对当前无序区(R1,R2,……Rn-1)调整为新堆，然后再次将R[1]与无序区最后一个元素交换，得到新的无序区(R1,R2….Rn-2)和新的有序区(Rn-1,Rn)。不断重复此过程直到有序区的元素个数为n-1，则整个排序过程完成。
![](https://images2017.cnblogs.com/blog/849589/201710/849589-20171015231308699-356134237.gif)
**代码**
```
#!/usr/bin/env python
# coding:utf-8
def HeapSort(input_list):
	
	#调整parent结点为大根堆
	def HeapAdjust(input_list,parent,length):
		
		temp = input_list[parent]
		child = 2*parent+1
		
		while child < length:
			if child+1 <length and input_list[child] < input_list[child+1]:
				child +=1
			
			if temp > input_list[child]:
				break
			input_list[parent] = input_list[child]
			parent = child
			child = 2*child+1
		input_list[parent] = temp
	
	if input_list == []:
		return []
	sorted_list = input_list
	length = len(sorted_list)
	#最后一个结点的下标为length//2
	#建立初始大根堆
	for i in range(0,length // 2 +1)[::-1]:
		HeapAdjust(sorted_list,i,length)
	
	for j in range(1,length)[::-1]:
		#把堆顶元素即第一大的元素与最后一个元素互换位置
		temp = sorted_list[j]
		sorted_list[j] = sorted_list[0]
		sorted_list[0] = temp
		#换完位置之后将剩余的元素重新调整成大根堆
		HeapAdjust(sorted_list,0,j)
		print('%dth' % (length - j))
		print(sorted_list)
	return sorted_list
```
**流程图**  
#### 基数排序
基数排序是按照低位先排序，然后收集；再按照高位排序，然后再收集；依次类推，直到最高位。有时候有些属性是有优先级顺序的，先按低优先级排序，再按高优先级排序。最后的次序就是高优先级高的在前，高优先级相同的低优先级高的在前。
**算法描述**  
取得数组中的最大数，并取得位数；
arr为原始数组，从最低位开始取每个位组成radix数组；
对radix进行计数排序（利用计数排序适用于小范围数的特点）；
![](https://images2017.cnblogs.com/blog/849589/201710/849589-20171015232453668-1397662527.gif)
**算法分析**  
基数排序基于分别排序，分别收集，所以是稳定的。但基数排序的性能比桶排序要略差，每一次关键字的桶分配都需要O(n)的时间复杂度，而且分配之后得到新的关键字序列又需要O(n)的时间复杂度。假如待排数据可以分为d个关键字，则基数排序的时间复杂度将是O(d*2n) ，当然d要远远小于n，因此基本上还是线性级别的。
基数排序的空间复杂度为O(n+k)，其中k为桶的数量。一般来说n>>k，因此额外空间需要大概n个左右。

 
**代码**
```
def RadixSort(a):
    i = 0                                             #初始为个位排序
    n = 1                                           #最小的位数置为1（包含0）
    max_num = max(a)                       #得到带排序数组中最大数
    while max_num > 10**n:              #得到最大数是几位数
        n += 1
    while i < n:
        bucket = {}                             #用字典构建桶
        for x in range(10):
            bucket.setdefault(x, [])    #将每个桶置空
        for x in a:                               #对每一位进行排序
            radix =int((x / (10**i)) % 10)   #得到每位的基数
            bucket[radix].append(x) #将对应的数组元素加入到相应位基数的桶中
        j = 0
        for k in range(10):
            if len(bucket[k]) != 0:       #若桶不为空
                for y in bucket[k]:         #将该桶中每个元素
                    a[j] = y                       #放回到数组中
                    j += 1
        i += 1

if __name__ == '__main__':
    a = [12,3,45,3543,214,1,4553]
    print("Before sorting...")
    print(a)
    RadixSort(a)
    print("After sorting...")
    print(a)
```
**流程图**  
![](https://wx4.sinaimg.cn/large/0071Dyx4ly1g1jvvlh7qkj30gm13djt5.jpg)

#### 桶排序
桶排序是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。桶排序 (Bucket sort)的工作的原理：假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排）。
**算法描述**
设置一个定量的数组当作空桶；
遍历输入数据，并且把数据一个一个放到对应的桶里去；
对每个不是空的桶进行排序；
从不是空的桶里把排好序的数据拼接起来。 
![](https://images0.cnblogs.com/blog/601033/201402/190622018277217.jpg)
**代码**
```
#!/usr/bin/env python
# coding:utf-8
def bucket_sort(array, n):
    # 1.创建n个空桶
    new_list = [[] for _ in range(n)]

    # 2.把arr[i] 插入到bucket[n*array[i]]
    for data in array:
        index = int(data * n)
        new_list[index].append(data)

    # 3.桶内排序
    for i in range(n):
        new_list[i].sort()

    # 4.产生新的排序后的列表
    index = 0
    for i in range(n):
        for j in range(len(new_list[i])):
            array[index] = new_list[i][j]
            index += 1
    return array


def main():
    array = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    n = len(array)
    array = bucket_sort(array, n)
    print(array)
if __name__ == '__main__':
    main()
```
**流程图**  
![](https://wx4.sinaimg.cn/large/0071Dyx4ly1g1jvvltvk8j30gg10caba.jpg)
<<<<<<< HEAD
=======

>>>>>>> 1bfadbab5f6f14ab97c54f8de3264c5f6f96b79e

