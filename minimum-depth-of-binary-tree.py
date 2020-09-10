'''
https://leetcode.com/problems/minimum-depth-of-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        level=0
        count=1
        q=[root]
        d=[]
        if root is None:
            return 0
        while q!=[]:

            k=q.pop(0)
            count-=1
            if k.left is None and k.right is None:
                d.append(level)
                
            if(k.left is not None):
                q.append(k.left)    
            if(k.right is not None):
                q.append(k.right)
                
            if (count == 0):
                level += 1
                count = len(q)
                
        return min(d)+1
