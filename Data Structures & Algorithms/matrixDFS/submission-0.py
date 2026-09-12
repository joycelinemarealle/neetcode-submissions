class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(grid, r,c, visit):
            ROWS, COLUMNS = len(grid), len(grid[0])

            #base case no path
            if (min(r,c)< 0 or
            r == ROWS or c == COLUMNS or
            (r,c) in visit or
            grid[r][c] == 1
            ):
                return 0

            #base case for path 
            if r == ROWS - 1 and c == COLUMNS - 1:
                return 1

            #add to set
            visit.add((r,c))

            #recurvies
            count = 0
            count += dfs(grid, r+1,c,visit)
            count += dfs(grid, r-1,c,visit)
            count += dfs(grid, r,c+1,visit)
            count += dfs(grid, r,c-1,visit)

            #backtrac
            visit.remove((r,c))
            return count #return count to previous node
        return (dfs(grid,0,0,set()))

            #base case no paht exist , out of bonds, if point in visit, if point is blocked
            #base case has path means from 0,0 to max r,max c
            #add to set for point at
            #recruve r+1, r-1, c+1, c-1
            #back track remove from set
            #return count
        