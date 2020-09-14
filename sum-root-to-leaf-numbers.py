'''
https://leetcode.com/problems/sum-root-to-leaf-numbers/submissions/
'''

class Solution:
    s=0
    def paths(self, stack, root): 
        if root == None: 
            return
 
        stack.append(root.val) 
        if(root.left == None and root.right == None): 
            temp_sum=0
            for i in stack:
                temp_sum=temp_sum*10+i
            self.s+=temp_sum
        self.paths(stack, root.left) 
        self.paths(stack, root.right) 
        stack.pop() 

    def sumNumbers(self,root: TreeNode) -> int:
        self.paths([],root)
        return self.s
