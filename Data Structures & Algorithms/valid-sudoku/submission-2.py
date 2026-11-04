class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #check if digit in same row, same column, same 3X3 box
        #if digit appears again then sudoku must be invalid
        #hashmap of sets for rows[r], cols[c] squares [r//3, c//3] rows ttrack each row, cols track each cols, sqaures track digits in 3X3
        #loop through the board 
            #skip values with "."
            #check if val is already in the dictionariy if it is return False
            #if not then add the val in the rows, cols,squares
        #return True

       # collections import defaultdict

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                #skip if not a value
                if board[r][c] == ".":
                    continue
                
                #check if seen
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[r//3,c//3]):
                    return False

                #add it to set if not seen
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[r//3,c//3].add(board[r][c])

        return True



        