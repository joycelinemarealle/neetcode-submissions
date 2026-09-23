class Graph:
    
    def __init__(self):
        self.adj = {}
        

    def addEdge(self, src: int, dst: int) -> None:

        if src not in self.adj:
            self.adj[src] = set()
        if dst not in self.adj:
            self.adj[dst] = set()

        self.adj[src].add(dst)


    def removeEdge(self, src: int, dst: int) -> bool:

        if src not in self.adj or dst not in self.adj[src]:
             return False
        self.adj[src].remove(dst)
        return True
    


    def hasPath(self, src: int, dst: int) -> bool:

        visit = set()
        visit.add(src)
        q = collections.deque()
        q.append(src)

        while q:
            for _ in range(len(q)):
                current = q.popleft()
                
                #base case
                if current == dst:
                    return True
                for neighbour in self.adj[current]:
                    if neighbour not in visit:
                        visit.add(neighbour)
                        q.append(neighbour)
        return False

            




    # def adjacentList():
    #     edges[["A", "B"], ["C", "D"]]
    #     adjList = {}

    #     for src, dst in edges:
    #         if src not in adjList:
    #             adjList[src] = []
    #         if dst not in adjList:
    #             adjList[dst] = []
    #         adjList[src].append(dst)
    # def shortestPathBFS(node, target, adjList ):
    #     #BFS more effieince time (V+E) space (V)
    #     visit = set()
    #     visit.add((node))
    #     q = collections.deque()
    #     q.append((node))
    #     length = 0

    #     while q:

    #         for _ in range(len(q)):
    #             curr = q.pop.left()

    #             #base case
    #             if curr == target:
    #                 return length

    #             #explore neighbours through bfs
    #             for neighbours in adjList:
    #                 if neighbours not in visit:
    #                     visit.add(curr)
    #                     q.append(curr)
    #         length+=1
    #     return length

    # def shortestPathDFS(node,target,adjList):
        
    #     def dfs(node,target,adjList, visit)
    #         #backtracking
    #         if node in visit:
    #             return 0
    #         if node == target:
    #             return 1
            
    #         count = 0
    #         visit.add(node)
    #         for neighbour in adjList:
    #             count += dfs(node,target,adjList,visit)
    #         visit.remove(node)
    #     return count
                





