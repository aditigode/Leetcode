class Solution:
    def rob(self, nums: List[int]) -> int:
        prevSum, prevPrevSum = 0, 0
        
        for i in range(len(nums)):
            currSum = max(prevSum, nums[i]+prevPrevSum)
            prevPrevSum = prevSum 
            prevSum = currSum
            
        return max(prevSum, prevPrevSum)