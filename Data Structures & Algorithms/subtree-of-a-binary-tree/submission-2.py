# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True
        
        if not root and subRoot:
            return False

        if self.isSameTree(root,subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

    def isSameTree(self,root:Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val!= subRoot.val:
            return False

        return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)

        #recursion
        #DFS
        #check node of Root if same as subRoot
        #check if subtree same a subRoot
        #if node not same return false
        #bigO n, time , space h~ n/2
        #base casese 
            #if subroot null then it must be sub tree, but if root null can never subtree
            #if node of root == node of sub root then true
            #recursive call isSubTree on left and right
        #helper to check is same tree
            #base is if not r and not s then true
            #if not r or not q then false
            #if r.val != s.val return false
            #recursive call left and right children
            #return
        