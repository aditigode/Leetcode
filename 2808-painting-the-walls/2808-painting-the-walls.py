class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:

        walls = len(cost)
        index = len(cost)
        #dp = [[-1 for _ in range(index)]for _ in range(walls+1)]
        dp = {}
        
        def dfs(i, remainWalls):
            if remainWalls <= 0:
                return 0
            if i == index:
                return math.inf

            if (remainWalls,i) in dp:
                return dp[(remainWalls,i)]

           

            paint = cost[i] + dfs(i+1, remainWalls - time[i] - 1)
            skip = dfs(i+1, remainWalls)
            dp[(remainWalls,i)] = min(paint, skip)
            return dp[(remainWalls,i)]

        return dfs(0,len(cost))
       


        


        
        