class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        i, j = 0, len(num)-1
        while j >= 0:
            if int(num[j]) % 2 != 0:
                return num[i:j+1]
            else:
                j -= 1
        return ""
        
        