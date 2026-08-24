# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        #edge case if node empty return node
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            #make root.right be new node we inserted
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)

        #no need else: since value added not seen befire
        
        return root
        

        #check if val > the node then insert at right, then change right value
        #if val < node then insert at left
        #check if has left or right child then insert ( 1 or 0 childreen)
        #if 
        #no target==val since new value does not exist
        #insert once reach leave node , at null once hit
        