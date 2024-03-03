class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            new_nums = nums[i]**2
            nums[i] = new_nums
            
        nums.sort()
        return nums
        