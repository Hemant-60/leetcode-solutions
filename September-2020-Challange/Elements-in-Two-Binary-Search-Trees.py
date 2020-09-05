'''
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3449/
'''
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        current = root1  
        stack = [] 
        vals=[]

        while True:  
            if current is not None: 
                stack.append(current) 
                current = current.left  

            elif(stack): 
                current = stack.pop() 
                vals.append(current.val) 
                current = current.right  
            else: 
                break
        
        current = root2
        stack=[]
        
        while True:  
            if current is not None: 
                stack.append(current) 
                current = current.left  

            elif(stack): 
                current = stack.pop() 
                vals.append(current.val) 
                current = current.right  
            else: 
                break
        
        vals.sort()
        
        return vals
