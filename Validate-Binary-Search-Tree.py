'''
https://leetcode.com/problems/validate-binary-search-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        current = root
        stack = []
        mx = -1<<32
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif(stack):
                current = stack.pop()
                if mx>=current.val: return False
                mx = current.val
                current = current.right
            else:
                return True
