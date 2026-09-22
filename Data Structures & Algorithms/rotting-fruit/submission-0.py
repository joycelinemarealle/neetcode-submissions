class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        ROWS,COLS = len(grid), len(grid[0])
        neighbours = [(1,0), (-1,0), (0,1), (0,-1)]
        time,fresh = 0,0
        
        #go through every cell to check what fresh and keep count, rotten and add to q
        #can have simultaneously BFS for every rotten fruit
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        #BFS    
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                
                for dr,dc in neighbours:
                        nr,nc = r + dr, c + dc
                        #check our bounds and not fresh
                        if (nr < 0 or nc < 0 or nr == ROWS or nc== COLS or grid[nr][nc]!=1):
                            continue
                        #change the valid neighbour to rotten a
                        grid[nr][nc] = 2 
                        q.append((nr,nc)) #add to queus
                        fresh -= 1
            time+=1  #all this happend in one unit    
        return time if fresh == 0 else -1

        #Loop through every cell to countkeep track of cells that fresh, and rotten add to q
        #have a time and fresh fruits 0
        #BFS
        #check while q and fresh fruit > 0 
        #then check up,down,right,left ( out of bond and not fresh skip 
        #if fresh and in bound then change to rottent
        #decream fresh count, increase time
        #return time or -1 if fresh is >0
        