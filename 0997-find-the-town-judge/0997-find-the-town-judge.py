class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # if key does not exist, return it
        if n == 1 and not trust:
            return 1
        trustsDict = defaultdict(list)
        trustedByDict = defaultdict(list)
        
        for personA, personB in trust:
            trustsDict[personA].append(personB)
            trustedByDict[personB].append(personA)
            
        #print(trustsDict)
        #print(trustedByDict)
        for possJudge,personList in trustedByDict.items():
            if len(personList) == n-1:
                if not trustsDict[possJudge]:
                    return possJudge
                
        
            
        return -1
        
            
            
                
                
        