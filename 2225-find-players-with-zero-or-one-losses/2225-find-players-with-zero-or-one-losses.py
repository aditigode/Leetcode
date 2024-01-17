class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zeroLosses,oneLosses,moreLosses = set(), set(), set()
        for winner, loser in matches:
            # if winner has not lost match add it to zero losses
            if winner not in oneLosses and winner not in moreLosses:
                zeroLosses.add(winner)
            
            # if loser has already lost one match, then current losses=2, move it to moreLosses
            if loser in oneLosses:
                oneLosses.remove(loser)
                moreLosses.add(loser)
            # else add the loser to oneLosses
            else:
                if loser in zeroLosses:
                    zeroLosses.remove(loser)
                if loser not in moreLosses:
                    oneLosses.add(loser)
                
        result = [sorted(list(zeroLosses)),sorted(list(oneLosses))]
        return result
                         
                  
#         MatchesDict = {}
        
#         #keep the count of loses and wins as values in dict
#         for winner,loser in matches:
#             if loser not in MatchesDict:
#                 MatchesDict[loser] = [0,0]
#             if winner not in MatchesDict:
#                 MatchesDict[winner] = [0,0]
#             MatchesDict[loser][0] += 1
#             MatchesDict[winner][1] += 1
            
            
#         #heap.__lt__ = lambda self, x : 
#         hq = [(key,value[0],value[1]) for key, value in MatchesDict.items()]
#         #print(hq)
#         #O(n) complexity
#         heapify(hq)
       
#         result = [[],[]]
#         while hq:
#             player,lost, won = heapq.heappop(hq)
            
#             #if player has lost 0 matches
#             if lost == 0:
#                 result[0].append(player)
#             # if player has lost exactly one match
#             elif lost == 1:
#                 result[1].append(player)
                
        
#         return result
        