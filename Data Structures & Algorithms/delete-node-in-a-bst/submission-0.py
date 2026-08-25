# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        #edge case root null return null
        if not root:
            return root
        
        #traverse right
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        #traverse left
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        #found the key
        else:
            #check if no left child, return right child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            #has two children traverse to right subtree look for min
            #Use right substree find min on left most side, replace current node with mini and delete the right node
            cur = root.right
            while cur.left: 
                cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)
        
        return root



        #recursively check for key going left or right subtree
        #if got it delete node
        #if key has one child then return the one child to parent node
        #if key has 2 children then find min of right subtree then replace key node with min (left of right subtree then delete the root right) still met the BST
        #bigo (h)
        #space constant node h
        