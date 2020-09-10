'''
https://leetcode.com/problems/cousins-in-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        vals={}
        level=0
        count=1
        q=[root]
        while q!=[]:
            k=q.pop(0)
            vals[k.val]=level
            count-=1
            # vals.append(k.val)
            if(k.left is not None):
                q.append(k.left)
                if(k.left.val==min(x,y) and k.right is not None and k.right.val==max(x,y)) or (k.left.val==max(x,y) and k.right is not None and k.right.val==min(x,y)):    
                    return False
                    
            if (k.right is not None):
                q.append(k.right)
            if (count == 0):
                level += 1
                count = len(q)
                
        if(vals[x]!=vals[y]):return False
        else: return True
