class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return root if(root is None or root.val == val) else (self.searchBST(root.left,val) if root.val > val else self.searchBST(root.right, val))
