class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagramDict = {}
        #print(sorted(strs[0]))
        
        for string in strs:
            sortedString = tuple(sorted(string))
            if sortedString in anagramDict:
                anagramDict[sortedString].append(string)
            else:
                anagramDict[sortedString] = [string]
                
        return anagramDict.values()
        