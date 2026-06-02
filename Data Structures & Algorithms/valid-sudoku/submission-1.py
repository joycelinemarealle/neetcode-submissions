class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = collections.defaultdict(set) #key r
        cols = collections.defaultdict(set) #key c
        squares = collections.defaultdict(set) #key r//3, c//3

        #loop through columns and rowa
        for r in range(9):
            for c in range(9):
                #check if this value at a point in row set , col set, squares set
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                   board[r][c] in cols[c] or
                   board[r][c] in squares[r//3, c//3]):
                   return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[r//3,c//3].add(board[r][c])
        return True
            

                
        #input is a ;ist =
        #hashset for each row, col m square
        # loop through row for ech row loop through col and check if that point in row[r] or cols[c] or square
        #3x3 there will 9 , to get right index need for key r//3 , c//3
        #Time two loops loop within a loop Big O*=(n2) 9^2
        #memory Big O(n2) 9^2