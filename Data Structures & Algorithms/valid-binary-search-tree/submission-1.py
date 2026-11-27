# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node,left,right):
            if not node:
                return True
            
            if not ( left < node.val < right):
                return False

            return valid(node.left, left, node.val) and valid(node.right,node.val,right)

        return valid(root,float("-inf"), float("+inf"))

        
        #BST a node has atmost 2 children, left < curr node and right > curr node
        #recursively for every node check if all left descendants < curr node and all right descendants > curr node
        #helper valid left the children -inf - left,  valid right right - +(inf)
        #if not then not binary
        #if not root return True
        #DFS from -inf - +inf
        