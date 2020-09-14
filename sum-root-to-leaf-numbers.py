'''
https://leetcode.com/problems/sum-root-to-leaf-numbers/submissions/
'''

class Solution:
    s=0
    tsum=0
    def paths(self, stack, root): 
        if root == None: 
            return
 
        stack.append(root.val)
        self.tsum=self.tsum*10+root.val
        if(root.left == None and root.right == None): 
            self.s+=self.tsum
        self.paths(stack, root.left) 
        self.paths(stack, root.right) 
        self.tsum//=10
        
        stack.pop() 

    def sumNumbers(self,root: TreeNode) -> int:
        self.paths([],root)
        return self.s
