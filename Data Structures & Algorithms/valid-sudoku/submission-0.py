class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = collections.defaultdict(set) #key r
        cols = collections.defaultdict(set) #key c
        squares = collections.defaultdict(set) #key r//3 c//3
        #loop through each row
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or #check if point in col # or row 1,2,3
                   board[r][c] in cols[c] or
                   board[r][c] in squares[(r//3, c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[r//3, c//3].add(board[r][c])
        return True

        
        #loop through row for each row 
         #loop through c columns to check if that point is duplicate or not
        # at that point check if in set of col, row, index
        #there ar emultiple rows /columns so use key rows[r]
        #for 3x3 can do integer division to pont to correct box 0,1,2
        #if not then add it to set
        #if all looping done return true
        #tiime big O(n2) 92
        #memory Big(n2) 92 since have the hashset for each row+column