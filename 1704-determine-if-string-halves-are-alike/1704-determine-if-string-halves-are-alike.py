class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s)//2
        # even = 8//2 3,4
       
        i, j = half-1, half
        vowels = {"a","e","i","o","u","A","E","I","O","U"}
        countI, countJ = 0, 0
        #coout
        while i >= 0 and j < len(s):
            if s[i] in vowels:
                countI += 1
            if s[j] in vowels:
                countJ += 1
            i -= 1
            j += 1
            
                
        return countI == countJ
        
        