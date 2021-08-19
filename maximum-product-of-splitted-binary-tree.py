'''
https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
'''
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.s=0
        self.mx=-float('inf')
        self.mod = 10**9 + 7
        
        #Storing sum of a sub tree in its root
        def trav(root):
            if root:
                trav(root.left)
                trav(root.right)
                self.s=(self.s + root.val)
                if root.left: root.val=(root.val + root.left.val)
                if root.right: root.val=(root.val+root.right.val)
        
        #Finding sub trees with max Sum Product
        def FindMaxSum(root):
            if root:
                FindMaxSum(root.left)
                FindMaxSum(root.right)
                self.mx = max(((self.s - root.val)*root.val), self.mx)
                
        
        trav(root)
        FindMaxSum(root)
        return self.mx%self.mod
        
