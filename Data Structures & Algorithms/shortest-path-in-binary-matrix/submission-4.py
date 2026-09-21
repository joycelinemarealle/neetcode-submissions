class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        #early exit
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1

        visit = set()
        q = collections.deque()
        q.append((0,0))
        visit.add((0,0))
        neighbours = [(0,1),(0,-1),(1,0),(-1,0), (1,1), (-1,-1), (-1,1), (1,-1)]
        length = 1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == ROWS -1 and c == COLS - 1:
                    return length

                #explore neighbours
                for dr , dc in neighbours:
                    nr, nc  = r + dr , c + dc

                    #base case to skip or add to quue valid cell or not
                    if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 1 or (nr, nc) in visit): continue
                    q.append((nr,nc))
                    visit.add((nr,nc))
            length += 1
        return -1

        #shorted path BFS
        #go level vy elvel, starrt 0,0 cell check if valid path
        #if valid add to queue
        #a queue to hold unprocessed cells
        #BFS
        # if not travel immediate exist if start and end = 1 return -1
        #base case return length if reached top right
        #base case for each neighbour (0,1), (1,0)  , (1,0) , (-1,0) if not unique skip neighbour ( out of bounds, already visited, cell is a rock)
        #for valid cell then add to q , and visit set
        #update length
        #Big O (nXn) time and space