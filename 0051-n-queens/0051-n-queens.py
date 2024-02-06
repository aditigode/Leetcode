class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        def checkAttack(board,i,j):
            # same column attack
            col = j
            row = 0
            for row in range(len(board)):
                if row != i and board[row][col] == 'Q':
                    #print("column",board)
                    return True
            
            # same row attack
            row = i
            col = 0
            for col in range(len(board[0])):
                if col != j and board[row][col] == 'Q':
                    #print("row")
                    return True
                
            # upper right diagonal attack
            row = i #negative
            col = j #positive
            row,col = i-1,j+1
            while row >= 0 and col < len(board[0]):
                if board[row][col] == 'Q':
                    #print("upper right",board)
                    return True
                row -= 1
                col += 1
                    
            
            # upper left diagonal attack
            # negative row, negative col
            row,col = i-1,j-1
            while row >= 0 and col >=0:
                if board[row][col] == 'Q':
                    #print("upper left",board)
                    return True
                row -= 1
                col -= 1
            
            # no attack
            return False
        
        def dfs(board,i,j,queens):
            nonlocal result
            if queens == n:
                #print(board,"queeensss")
                board1 = board[:]
                #print(board1)
                result.append([''.join(row) for row in board])
                
                
                
            else:
            
                #for row in range(i,len(board)):
                for col in range(0,len(board[0])):
                    board[i][col] = 'Q'
                    if not checkAttack(board,i,col):
                        #print(board,i,j)
                        dfs(board,i+1,col,queens+1)
                        #print(queens)
                    board[i][col] = '.'
                        
        rows, cols = n,n
        board = [['.' for j in range(cols)]for i in range(rows)]
        
        dfs(board,0,0,0)
        #print(len(result))
        return result
                                
                            
                
        
        
                
                
        