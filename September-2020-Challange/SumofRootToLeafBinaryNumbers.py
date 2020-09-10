'''
https://leetcode.com/explore/featured/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3453/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    s=0
    def paths(self, stack, root): 
        if root == None: 
            return
 
        stack.append(root.val) 
        if(root.left == None and root.right == None): 
            self.s+=int(''.join([str(i) for i in stack]),2)

        self.paths(stack, root.left) 
        self.paths(stack, root.right) 
        stack.pop() 

    def sumRootToLeaf(self,root: TreeNode) -> int:
        self.paths([],root)
        return self.s
