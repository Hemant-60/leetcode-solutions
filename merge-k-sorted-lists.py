# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        start = None
        
        Not_none_values = filter(None.__ne__, lists)
        lists = list(Not_none_values)
        
        if lists == []: return None
        # print(lists)
        while lists:
            index = -1
            mn= 100000
            for i in range(len(lists)):
                if lists[i] is not None:
                    if lists[i].val < mn:
                        index = i
                        mn = lists[i].val
            if head is None:
                head = ListNode(lists[index].val)
                start = head
            else:
                head.next = ListNode(lists[index].val)
                head = head.next
            
            lists[index] = lists[index].next
            if lists[index] is None:
                lists.pop(index)
        
        return start
