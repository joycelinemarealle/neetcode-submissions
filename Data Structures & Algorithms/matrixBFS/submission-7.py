class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        visit = set() #keep track of visited
        q = collections.deque() #store unprocessed cells
        neighbours = [(0,1), (0,-1), (1,0), (-1,0)] #directions of visit of a cell
        q.append((0,0)) #starting point top left
        visit.add((0,0)) #add visited
        ROWS, COLUMNS = len(grid), len(grid[0])

        length = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                #if no path blocked start or end not traversal posisble
                if grid[0][0] == 1 or grid[ROWS -1][COLUMNS-1] == 1:
                    return -1

                #base case return legnth
                if r == ROWS -1 and c == COLUMNS -1:
                    return length

                #base check neignhours case skip cell and pop another in queue
                for dr, dc in neighbours:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or nr == ROWS or nc == COLUMNS or (nr,nc) in visit or grid[nr][nc] == 1): continue #skip the neighbour cell and 
                   
                    q.append((nr,nc))
                    visit.add((nr,nc))
            length += 1 
        return -1
        


        
        #shorted efficient BFS
        #go through each level and check if valid path
        #keep track of length if valid bath
        #in bfs go through (0,1),(0,-1)(1,0),(-1,0)
        #a queue to store the unprocessed cells, pop left as i process them
        #base case return length if i reach max col, max row 
        #base case no valid lenght (1) out of bond, meet a rock, have visited the cell already then we continue. and check another cell in the queue
        #keep track of length
        #space, time, Big O(mxn)