class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        cache = {}
        def fallingSum(row,col):
            nonlocal cache
            if row == len(matrix):
                return 0
            
            elif (row,col) in cache:
                return cache[(row,col)]
            else:
                coords = [(1,-1),(1,0),(1,1)]
                minSum = math.inf
                for i, j in coords:
                    # check < for col and <= for row. This is done intentionally
                    if 0 <= row+i <= len(matrix) and 0 <= col+j < len(matrix[0]):
                        currSum = fallingSum(row+i,col+j)
                        minSum = min(minSum,currSum + matrix[row][col])
                cache[(row,col)] = minSum
                        
                return minSum
            
        minFallingSum = math.inf
        for col in range(len(matrix[0])):
            #print(cache)
            #cache = {}
            minFallingSum = min(minFallingSum, fallingSum(0,col))
            
        return minFallingSum
            
                    
        