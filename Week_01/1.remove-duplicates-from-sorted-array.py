class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) ==0:return 0
        first = 0
        for i in range(1,len(nums)):
            if nums[first] != nums(i):
                first +=1
                nums[first]=nums[i]
        return first+1
        
