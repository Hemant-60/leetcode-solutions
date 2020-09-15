'''
https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
'''
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        s=0
        q=[root]
        
        while q!=[]:
            k=q.pop(0)
            if k.left is not None:
                q.append(k.left)
                if k.val%2==0:
                    if k.left.left is not None: s+=k.left.left.val
                    if k.left.right is not None: s+=k.left.right.val
            
            if k.right is not None:
                q.append(k.right)
                if k.val%2==0:
                    if k.right.left is not None: s+=k.right.left.val
                    if k.right.right is not None: s+=k.right.right.val
            
        return s
