class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sSet = collections.Counter(s)
        tSet = collections.Counter(t)
        #print(sSet, tSet)
        count = 0
        for char,charCount in sSet.items():
            if char in tSet:
                count += (charCount - tSet[char] if (charCount - tSet[char]) >= 0 else 0)
            else:
                count += charCount
                
        return count