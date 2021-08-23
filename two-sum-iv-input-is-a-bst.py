'''
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
'''
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root.left and not root.right: return False
        self.flag=0
        def trav(root,visited):
            if root:
                trav(root.left,visited)
                if (k - root.val) in visited:
                    self.flag=1
                    return
                else: visited.add(root.val)
                trav(root.right,visited)
        
        visited=set()
        trav(root,visited)
        if self.flag==1: return True
        return False
