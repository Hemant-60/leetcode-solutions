'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        level=0
        count=1
        q=[root]
        if root is None:
            return 0
        while q!=[]:
            k=q.pop(0)
            count-=1
                
            if(k.left is not None):
                q.append(k.left)    
            if(k.right is not None):
                q.append(k.right)
                
            if (count == 0):
                level += 1
                count = len(q)
                
        return level
