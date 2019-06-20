class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #先将堆排序
        nums = sorted(nums)[::-1]
        #找出第k大元素，若值相等，亦视为一个
        length = len(nums)
        j = 0
        count = 1
        for i in range(1,length):
            if nums[i] <= nums[j]:
                count+=1
                if count ==k:
                    return nums[i]
                j=i
        return nums[0]