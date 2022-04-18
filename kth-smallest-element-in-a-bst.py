from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current = root
        stk = deque([])

        while True:
            if current is not None:
                stk.append(current)
                current = current.left

            elif(stk):
                current = stk.pop()
                k-=1
                if k<=0:
                    return current.val
                current = current.right
