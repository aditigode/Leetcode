class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        distance = {}
        
        @cache
        def minsum(i,j):
            
            nonlocal distance
            #print(i,j,distance)
            if 0 > i or i > len(grid) or 0 > j  or j > len(grid[0]):
                return math.inf
            
            elif (i,j) in distance:
                return distance[(i,j)]
            else:
                #came from up or left
                #coords = [(-1,0),(0,-1)]
                if i == 0 and j == 0:
                    distance[(i,j)] = grid[i][j]
                else:
                    distance[(i,j)] = grid[i][j] + min(minsum(i-1,j),minsum(i,j-1))
                #print(i,j, distance)
                return distance[(i,j)]
        minsum(len(grid)-1, len(grid[0])-1)
        #print(distance)
        return distance[(len(grid)-1, len(grid[0])-1)]
        