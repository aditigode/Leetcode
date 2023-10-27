class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        s1_dict = collections.Counter(list(s1))
        #print(s1_dict)
        start = 0
        windowDict = {}
        for end in range(len(s2)):
            if end - start + 1 > k:
                print(windowDict, s1_dict)
                if windowDict == s1_dict:
                    return True
                else:
                    if windowDict[s2[start]] > 1:
                        windowDict[s2[start]] -= 1
                    else:
                        del windowDict[s2[start]]
                start += 1
            if s2[end] in windowDict:
                windowDict[s2[end]] += 1
            else:
                windowDict[s2[end]] = 1
        return windowDict == s1_dict
            

        