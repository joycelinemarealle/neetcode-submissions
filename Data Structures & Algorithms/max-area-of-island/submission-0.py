class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            #basecase return 0
            if (r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or (r,c) in visit): return 0

            visit.add((r,c))

            #base return 1 current point and all four neighbours
            return (1 + dfs(r + 1,c) + dfs(r - 1 ,c) + dfs(r,c + 1 ) + dfs(r,c -1) ) 
        #if not visited go through each r, c and do dfs
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r,c))
        return area
      

        #base case out of bonds min and max, if r,c is 0 return 0
        #base case if r,c, is 1 return 1
        #return 1+ r+1,r+1, r-1, c+1, c-1
        #loop for r in rows , for c in cols calls dfs, track areas
        #return max(area, dfs)
    