class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # 1 15 7 9 2 5 10
        # 15 15 15 
        
        # 1 15 15 
        # 1 15 7 
        # j = 1 to k
        # dp[i] = dp[i-j] + max(A[i-1], A[i-2], A[i-3]) * j
        # j = 1
        # dp[3] = dp[2] + max(A[2]) * 1
        # dp[3] = dp[1] + max(A[2],A[1]) * 2
        # dp[3] = dp[0] + max(A[2],A[1],A[0]) * 3
        
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            max_val = float('-inf')
            for j in range(1, min(i + 1, k + 1)):
                max_val = max(max_val, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + max_val * j)

        return dp[n]
                    
                
        
       
            
            
        
                
                
        
        
        