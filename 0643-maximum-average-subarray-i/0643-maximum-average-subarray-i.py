class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        totalSum = 0
        average = -math.inf
        for i in range(len(nums)):
            totalSum += nums[i]
            if i >= k-1:
                temp = totalSum/k
                average = max(average, temp)
                #print(i, i-k-1)
                totalSum -= nums[i-(k-1)]
        return average
        