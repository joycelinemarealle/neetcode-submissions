class Solution:
     def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def dfs(r,c):
            #base case no path
            if (r < 0 or c < 0 or
            r == ROWS or c == COLUMNS or
            (r,c) in visit or
            grid[r][c] == "0"
            ):
                return 0
           
           #add to set
            visit.add((r,c))
            #base case for path 
            dfs(r + 1, c) 
            dfs(r - 1, c)  
            dfs(r, c + 1) 
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range (COLUMNS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r,c)
                    islands += 1 
        return islands

             
                

        