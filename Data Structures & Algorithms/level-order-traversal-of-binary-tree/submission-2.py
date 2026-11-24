# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque()
        res = []
        queue.append(root)

        while queue:
            level = []
            lenQ = len(queue)

            for i in range(lenQ):
                node = queue.popleft()
                
                if node:
                    level.append(node.val)

                if node:
                    queue.append(node.left)
                    queue.append(node.right)

            if level:
                res.append(level)
        return res



        #level by level BFS
        #collection. deque, res []
        #add root in deque
        #while q:
            # for len of q i need to pp node add to level []
            #add children of that node to que
            #add level [] to result
        #return res
        #Big O(n) number of nodes, space Big O(n) number of nodes