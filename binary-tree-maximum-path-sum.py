# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        sums = []
        mx = []
        def trav(root, mx):
            if root:
                trav(root.left, mx)
                trav(root.right, mx)
                l = 0
                r = 0
                if root.left: l = root.left.val[1]
                if root.right: r = root.right.val[1]
                root.val = (root.val+l+r, max(max(l,r)+root.val, root.val))
                mx = mx.append(max(root.val))
        trav(root, mx)
        return max(mx)
            
        
