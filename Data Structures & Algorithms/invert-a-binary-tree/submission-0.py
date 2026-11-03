
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
        
        queue = deque([root])

        while queue:
            node = queue.popleft()
            node.left , node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
            

        #check if tree empty return null
        #add queue BFS insert root note
        #while queue is not empty
            # remove frontnnote
            #swap left and right child
            #if left child exists add to queue
            #if right child exists add to queue
        #after all processed return root as inverted
        