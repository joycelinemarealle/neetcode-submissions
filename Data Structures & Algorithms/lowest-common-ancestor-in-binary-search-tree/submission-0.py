# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if not root or not p or not q:
            return None
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr



        #since binary the left of node < than node , right > nodeo
        #if p, q > than node then move node to right
        #if p, q < tha node check nodeleft
        # else return the node because this is where split happens. you cano have common ancestors is going to be in different branch the split is where the least ancesort leaves#if it happens p, q = node then return the node lowestCommonAncestor
        #time Big O(h) height of tree this is for binary
        #spac Big O(n)