class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost)+1)
        dp[len(cost)] = 0
        dp[len(cost)-1] = cost[len(cost)-1]

        for i in range(len(cost)-2,-1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])

        return min(dp[0], dp[1])

        