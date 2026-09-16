class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        #edge case no island
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0
        directions = [[1,0], [-1,0],[0,1], [0,-1]]

        def bfs(r,c):
            q = collections.deque()
           
            visit.add((r,c))
            q.append((r,c))

            while q:
                row,col= q.popleft()
                
                #Explore all 4 neighbours
                for dr,dc in directions:
                    nr, nc = row + dr, col + dc 
                    
                    #base case
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or
                    grid[nr][nc] == "0" or (nr,nc) in visit): continue

                    #if true then add to q and add neighbours visited
                    
                    q.append((nr,nc))
                    visit.add((nr,nc))

        for r in range(ROWS):
            for c in range(COLS):
                #if island and not visited
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r, c)
                    islands +=1
        return islands
        #solve using BFS
        #for every cell in grid check if island using bfs
        #in bfs have a stack to hold unprocessed cells, whiel q then pop cell check if island if it is add count
        #in bdfs have base case if '0', r,c already processed, out of bond < 0 or max rol, max col
        