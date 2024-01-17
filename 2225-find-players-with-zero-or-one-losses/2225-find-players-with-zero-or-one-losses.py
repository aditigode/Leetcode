class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        MatchesDict = {}
        
        #keep the count of loses and wins as values in dict
        for winner,loser in matches:
            if loser not in MatchesDict:
                MatchesDict[loser] = [0,0]
            if winner not in MatchesDict:
                MatchesDict[winner] = [0,0]
            MatchesDict[loser][0] += 1
            MatchesDict[winner][1] += 1
            
            
        #heap.__lt__ = lambda self, x : 
        hq = [(key,value[0],value[1]) for key, value in MatchesDict.items()]
        #print(hq)
        #O(n) complexity
        heapify(hq)
       
        result = [[],[]]
        while hq:
            player,lost, won = heapq.heappop(hq)
            
            #if player has lost 0 matches
            if lost == 0:
                result[0].append(player)
            # if player has lost exactly one match
            elif lost == 1:
                result[1].append(player)
                
        
        return result
        