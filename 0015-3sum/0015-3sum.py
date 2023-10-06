class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #time complexity 
        #O(nlogn) + O(n2) = O(n2) 
        #sort the list
        nums.sort()

        #result set
        res = []

        #fix the first element
        for i, num in enumerate(nums):
            #if 1st element is duplicate skip it to avoid duplicate answers
            if i > 0 and num == nums[i-1]:
                continue
                #print("hi")
            #left and right pointer like in sum2
            l , r = i+1, len(nums) - 1
            while l < r:
                sum1 = num + nums[l] + nums[r]
                #print(sum1)
                if sum1 == 0:
                    res.append([num, nums[l], nums[r]])
                    #if res found increase left ptr(move forward)
                    l += 1
                    #two avoid duplicate answer because of 2nd duplicate element so skip it
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                elif sum1 < 0:
                    l += 1
                else:
                    r -= 1
        return res
