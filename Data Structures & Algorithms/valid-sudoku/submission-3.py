class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #for every cell check if appeared in row , col, square

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):

                #check if cell has been seen  
                if board[r][c] == "." :
                    continue

                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[r//3,c//3]:return False

                #means not seen so add to set
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[r//3,c//3].add(board[r][c])
        return True
        