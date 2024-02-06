class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        numLen = len(nums)

        for i in range(len(nums)):
            if 0 >= nums[i] or nums[i] > numLen:
                nums[i] = numLen + 1

        for i in range(len(nums)):
            num = abs(nums[i])
            num -= 1
            # negative or num > numLen: useless number so ignore
            if num+1 > numLen:
                continue
            
            # to prevent double negative; this will happen in case of duplicates
            elif nums[num] > 0:
                nums[num] = -1 * nums[num]

        # check for missing number
        for i in range(len(nums)):
            #print(i,nums)
            if nums[i] > 0:
                return i+1
        
        #if array if exhausted, return the next positive outside the array e.g [1] = 2
        return numLen+1

        




        
            

        