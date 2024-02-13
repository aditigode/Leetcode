class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for word in words:
            mid = len(word)//2
            #even palindrome
            # abba = 4/2 = 2
            # aabbaa = 6/2 = 3
            notFound = False
            if len(word) % 2 == 0:
                i,j = mid-1,mid
                
                while i >= 0 and j < len(word):
                    if word[i] != word[j]:
                        notFound = True
                        break
                    i -=1
                    j +=1
            else:
                i,j = mid,mid
                #notFound = False
                while i >= 0 and j < len(word):
                    if word[i] != word[j]:
                        notFound = True
                        break
                    i -=1
                    j +=1
                
            if not notFound:
                return word
        
        return ""
        