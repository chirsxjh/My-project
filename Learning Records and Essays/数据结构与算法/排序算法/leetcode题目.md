### LeetCode 75. 颜色分类
**题目：**  
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。  
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
**注意:**  
不能使用代码库中的排序函数来解决这道题。  
**示例:** 
输入: [2,0,2,1,1,0]   
输出: [0,0,1,1,2,2]  
**分析**:  
在快速排序中寻找pivot的方式很像，区别在于需要使用三指针而非双指针。整个思路很直观：遍历数组，碰到0就放到最后面，碰到2就放到最前面，等遍历完成后所有的1自然都被放到中间。代码主体是一个while循环，i 和 j 分别表示下次遇到0和2时要移入的位置。如果碰到1可以直接忽略。判断 k>i 和 k<j 是为了减少不必要的交换。代码如下：
```
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 三路快排
        i, j, k = 0, len(nums) - 1, 0
        while k < len(nums):
            if nums[k] == 0 and k > i:
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
            elif nums[k] == 2 and k < j:
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1
            else:
                k += 1

```


  
