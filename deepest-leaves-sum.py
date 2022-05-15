from collections import Counter
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0)])
        curr_sum = root.val
        mx_level = -1
        while q:
            node, depth = q.popleft()
            if depth == mx_level:
                curr_sum += node.val
            elif depth > mx_level:
                curr_sum = node.val
                mx_level = depth
            if node.left: q.append((node.left, depth+1))
            if node.right: q.append((node.right, depth+1))
        
        return curr_sum
