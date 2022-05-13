from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        q=[root]
        while q:
            count=0
            n = len(q)
            for i in range(n):
                if q[i].left:
                    q.append(q[i].left)
                    count+=1
                if q[i].right:
                    q.append(q[i].right)
                    count+=1
            for i in range(n-1):
                q[i].next = q[i+1]
            q = q[n:]
        return root
