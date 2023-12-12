class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def countIslands(i,j):
            nonlocal visited
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return True
            elif grid[i][j]  == '0':
                return True
            else:
                coords = [(0,1),(1,0),(-1,0),(0,-1)]
                flag = True
                for r,c in coords:
                    if (i+r,j+c) not in visited:
                        visited.add((i+r,j+c))
                        if not countIslands(i+r,j+c):
                            flag = False
                
                return flag
            
        #countIslands(0,0)
        count = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in visited:
                    visited.add((i,j))
                    if countIslands(i,j):
                        count += 1
        return count
                    
                    
                
        