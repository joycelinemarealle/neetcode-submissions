# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val:
           root.left = self.insertIntoBST(root.left, val)
        
        return root

        #edge case if not root create new node and return new val in ndoe
        #if val > node then check right, if reach leaf node add child/val
        #else if val < node chekc left until reach the leaf node. add child/val
        