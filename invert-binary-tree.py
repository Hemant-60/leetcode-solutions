''' https://leetcode.com/problems/invert-binary-tree/ '''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        curr=root
        self.invert(curr)
        return root
    
    def invert(self,root: TreeNode):
        if root is None or root.right is None and root.left is None:
            return
        tmp =root.left
        root.left=root.right
        root.right=tmp
        
        self.invert(root.left)
        self.invert(root.right)
