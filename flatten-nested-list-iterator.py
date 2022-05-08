from collections import deque

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.q = deque([])
        def trav(nestedList):
            for i in nestedList:
                if i.isInteger():
                    self.q.append(i.getInteger())
                else:
                    trav(i.getList())
        trav(nestedList)
        
    def next(self) -> int:
        return self.q.popleft()
    
    def hasNext(self) -> bool:
         return False if not self.q else True
