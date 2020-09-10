'''
https://leetcode.com/problems/binary-tree-level-order-traversal/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        vals=[[]]
        level=0
        count=1
        q=[root]
        if root is None:
            return []
        while q!=[]:
            k=q.pop(0)
            if k is not None:
                vals[level].append(k.val)
            count-=1
            if(k.left is not None):
                q.append(k.left)
            if (k.right is not None):
                q.append(k.right)
            if (count == 0):
                if q!=[]:
                    vals.append([])
                level += 1
                count = len(q)
        
        return vals
