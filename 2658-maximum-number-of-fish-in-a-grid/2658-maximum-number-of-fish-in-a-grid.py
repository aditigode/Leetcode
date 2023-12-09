class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def catchFish(i,j):
            nonlocal visited, total
            coords = [(0,1),(1,0),(0,-1),(-1,0)]
            total += grid[i][j]
            #print("catchFish",total, i, j)
            for r,c in coords:
                if (i+r,j+c) not in visited:
                    if 0 <= i+r < len(grid) and 0 <= j+c < len(grid[0]) and grid[i+r][j+c] != 0:
                        visited.add((i+r,j+c))
                        catchFish(i+r,j+c)
            #print("catchFish2",total, i, j)
            
            
        visited = set()
        #total = 0
        maxTotal = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0 and (i,j) not in visited:
                    total = 0
                    #print(visited, i,j, total, maxTotal)
                    visited.add((i,j))
                    catchFish(i,j)
                    #print("total now is", total)
                    maxTotal = max(maxTotal, total)
        return maxTotal
                
        