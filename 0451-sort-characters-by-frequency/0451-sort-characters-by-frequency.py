class Solution:
    def frequencySort(self, s: str) -> str:
        freqDict = {}
        for char in s:
            if char not in freqDict:
                freqDict[char] = 1
            else:
                freqDict[char] += 1
        
        
        sorted_dict = dict(sorted(freqDict.items(),key = lambda item: item[1],reverse=True))
        
        res = ""
        for key,val in sorted_dict.items():
            res += (key*val)
            
        return res
        
        