class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if len(nums) > 1 and  k > 0:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]
