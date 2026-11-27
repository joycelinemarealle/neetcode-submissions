# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def dfs(node):
            #base case
            if not node:
                return 

            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)  
        dfs(root)
        #arr.sort()
        return arr[k-1]
        #BST left sub tree, right subtree
        #can i traverse 
        #then put in array in order in order traversal so to sort it ou already, 
        #sort it and 
        #check k-1 position?#have a way to store the values of nodes in order and return k-1 positoon in array
        #Big O(h) height of tree Big O(nlong) n sorted
        #space Big O(n) storing stack,
        