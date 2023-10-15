class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        if (endPos - startPos) > k:
            return 0
        positions = (endPos - startPos +1) * 2
        diff = (endPos - startPos + 1)
        #print(positions, diff)

        dp = [[-1 for _ in range(1001)]for _ in range(4001)]
        #print(dp)
        mod = 10**9 + 7

        def recurse(curr, target, steps):
            #base case
            if curr == target and steps == 0:
                return 1
            if steps == 0:
                return 0
            #print(curr+diff, curr, diff, steps)
            if dp[curr+1000][steps] > -1:
                return dp[curr+1000][steps]
            left = curr -1
            res = 0
            res = (recurse(curr+1, target, steps-1) % mod)
            right = curr + 1
            res += (recurse(curr-1, target, steps-1)% mod)


            dp[curr+1000][steps] = res % mod

            return dp[curr+1000][steps]

        return recurse(startPos, endPos, k)



        