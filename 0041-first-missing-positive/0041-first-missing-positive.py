class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # remove -ve and 0 numbers
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums)+1
            
        # mark numbers which are present in the array
        
        for i in range(len(nums)):
            if 0 < abs(nums[i]) <= len(nums) and nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] *= -1
                
        #count = 1
        
        print(nums)
        # check for the marked numbers and return the one that has not been marked
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i+1
            
        return len(nums)+1
            
            
        