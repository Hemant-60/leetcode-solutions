from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque([])

    def push(self, x: int) -> None:
        #Takes O(n) time
        self.q = deque([x]) + self.q

    def pop(self) -> int:
        #Takes O(1) time
        return self.q.popleft() if not self.empty() else None

    def top(self) -> int:
        return self.q[0] if not self.empty() else None

    def empty(self) -> bool:
        return True if not self.q else False
