class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #dynamic window sliding window
        length = math.inf
        totalSum = 0
        start = 0
        for end in range(len(nums)):
            totalSum += nums[end]
            while totalSum >= target:
                length = min(length, end-start+1)
                totalSum -= nums[start]
                start += 1
        return 0 if length == math.inf else length


        