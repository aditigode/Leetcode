class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        dp = {}
        #dp[i][diff] will be arithmetic sequences ending at index i with difference diff
        #i can go from 0 to n-1 but diff can be unpredictable so we're using a hashmap
        #if dp[i][j] does not exist, it will output 0 because of defaultdict(int)
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[(i,diff)] = dp.get((i,diff),0) +  (dp.get((j,diff),0) + 1)
                res += (dp.get((j,diff),0) + 1)
            
        return res - ((n * (n-1))//2)
    
                
                    
                    