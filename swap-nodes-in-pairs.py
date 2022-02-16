class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode(10)
        start.next = head
        head = start
    
        while start:
            if start.next is None or start.next.next is None:
                break
            temp = start.next
            start.next = start.next.next
            temp.next = start.next.next
            start.next.next = temp
            start = start.next.next
            
        return head.next
