# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #basecase
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
         
        return 1 + max(left, right)

        #DFS
        #base case return 0 if not root
        #recursive 1+ maxDepth
        #compre max of left and right subtress and return max length
        #time BigO(n)
        #space  recrusive stack BigO(n) n number of ndoes    