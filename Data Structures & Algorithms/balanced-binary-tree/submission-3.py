# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [True,0] #keep track both height and if balanced
            left = dfs(root.left)
            right = dfs(root.right)

            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1) #true or false
            return [balanced, 1 + max (left[1], right[1])]
        return dfs(root)[0]    #return is array so choose the 
        #keep track of count, check diff of max left, max right <=1 then balanced
        #traverse through nodes track count, check left snd right if dff <=1 Big O(n)
        #base case if not root [True,0] empty nodes is balanced count, bool if balanced or not
        #balanced check diff abs (left count - right count) and that bool is true
        #if nodes not balanced no need to process them
        