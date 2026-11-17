class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        #edge 
        if not grid:
            return 0

        #define the rows and cols
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(r,c):
            #base case
            if r < 0 or c < 0 or r == rows or c == cols or (r,c) in visit or grid[r][c] == "0": return 0

            visit.add((r,c))
            
            for dr,dc in directions:
                dfs(r + dr,c + dc)
           
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    #dfs check the neights
                    dfs(r,c)
                    islands+=1
        return islands

        #check every cell
        #go through every cell in grid
        #if 1 found then increment island count and run dfs in the cell
        #in dfs 
            #have base return retunr 0 
            # r and c out of bounds, r,c visited
            #mark r,c as visited
            #cell is 0 water
            #recursviely explore the 4 directions
        #continue until all cells ar eprocessed
        #return island counts

        