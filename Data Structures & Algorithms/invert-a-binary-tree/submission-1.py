# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        #initialize the root
        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            #swap nodes
            node.left, node.right = node.right, node.left

            #add to queue if node has children
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

        return root

        #BFS
        #have a deque
        #add root
        #while queue
        #pop out node
        #for each node swap its children. nodeleft,node right = node right, nodeleft
        #add swapped nodes children in queue#if node has childreen add to deque
        #time Big O(n)
        #space Big O(n) max element in queue

        