class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        
        #use changed grid to keep track
        def dfs(r,c):
            #base case return 0
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == "0": return 0
            #changed "1" to "0" to mark visited
            grid[r][c] = "0"
            
            #perform recursion in all four direction
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        return islands




        #for every cell in grid check if island "1" and not visited
        #if it perform dfs and add count of island
        #for dfs check out of bound, if r,c visited, grid[r][c] "0" return 0
        #add r,c to viist set
        #time+ space Big O( mxn)
        
        