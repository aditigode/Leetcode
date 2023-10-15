class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        arrLen = min(steps, arrLen)
        dp = [[-1 for _ in range(steps+1)]for _ in range(arrLen+1)]
        mod = 10**9 + 7

        def findWays(curr,k):
            if curr == 0 and k == 0:
                return 1
            if k == 0:
                return 0
            if dp[curr][k] > -1:
                return dp[curr][k]
            res = 0
            #only go right if it is possible to do in k steps
            if curr+1 < arrLen and curr+1 <= k-1:
                res = findWays(curr+1, k-1) % mod
            if curr <= k-1:
                res += findWays(curr, k-1) % mod
            if curr-1 >= 0 and curr-1 <= k-1:
                res += findWays(curr-1, k-1) % mod

            dp[curr][k] = res % mod
            return dp[curr][k]
        return findWays(0,steps)



        
        
        