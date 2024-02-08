class Solution:
    def numSquares(self, n: int) -> int:
        # 11 10 12-9: 3
        # 13/2= 6 + 1, 6-1
        # 6 + 2, 6-1
        # 6+1 , 6-2
        # 12
        # 1 2 3 4 5 6 7 
        # i to n
        # (1) 0 0 (1) (2) (3)
        #print(math.sqrt(11))
        dp = [math.inf for i in range(0,n+1)]
        
        for i in range(1,n+1):
            #print(dp)
            if i == math.isqrt(i) ** 2:
                #print(i)
                dp[i] = 1
            else:
                for j in range(math.isqrt(i)+1):
                    dp[i] = min(dp[i], dp[i-j*j] +1 )
                    # 12-4 = 8 so counting + 1 for (4) and take rest from 8 which 2
        return dp[n]
        