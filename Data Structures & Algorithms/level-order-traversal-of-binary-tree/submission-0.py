# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        queue = collections.deque()
        queue.append(root)

        if not root:
            return []

        while queue:
            qLen = len(queue)
            level =  []

            for i in range(qLen):
                node = queue.popleft()
                
                if node: 
                    level.append(node.val)

                if node:
                    queue.append(node.left)
                    queue.append(node.right)

            if level:
                res.append(level)
        return res

        #BFS
        #empty list and queue for my noddes
        #recursive function 
        #push root to queue
        #remove current node and add to sublist level
        #add nodes children in the queu
        #continue until queue empty

        #Algorithm
        # create queue push root
        #while queu not empty
            #qLen 3 of nodes currenlty in eleve
            #create empty level []    
            #repeat qLen times
                #pop a node form the queu
                #add value to level
                #add left and right children to que
            #appen level to result list
        #return result list containing all levels