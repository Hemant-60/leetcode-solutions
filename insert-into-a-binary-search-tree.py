class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        head = root
        while True:
            if root.val > val:
                if root.left: root = root.left
                else:
                    root.left = TreeNode(val)
                    return head
            if root.val <= val:
                if root.right: root = root.right
                else:
                    root.right = TreeNode(val)
                    return head
