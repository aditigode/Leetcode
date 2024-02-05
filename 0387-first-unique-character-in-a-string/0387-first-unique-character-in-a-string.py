class Solution:
    def firstUniqChar(self, s: str) -> int:
        wordsDict = {}
        
        for i in range(len(s)):
            if s[i] in wordsDict:
                wordsDict[s[i]][1] += 1
            else:
                wordsDict[s[i]] = [i,1]
        
        index = math.inf
        found = False
        
        for key, values in wordsDict.items():
            if values[1] < 2 and values[0] < index:
                index = values[0]
                found = True
                
        return index if found else -1
        