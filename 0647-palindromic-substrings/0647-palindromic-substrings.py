class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # a b c
        # aaa
        # aaa aa a a
        # abc aababcc
        # aa
        palindrome = 0
        
        for curr in range(len(s)):
            # odd length palindromes
            i,j = curr, curr
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                i -= 1
                j += 1
                palindrome += 1
                    
            
            # even length palindromes
            i,j = curr, curr+1
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                i -= 1
                j += 1
                palindrome += 1
        return palindrome
        