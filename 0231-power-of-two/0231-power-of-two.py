class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 11 >> 1
        # 10 >> 1 : 1
        # 100 >> 2
        # 110 : 1
        # 11: 
        # 16 8 4 2 1 = True
        # 3 != 1 so False
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
            
        return n == 1
        