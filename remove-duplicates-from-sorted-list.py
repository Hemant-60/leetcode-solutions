class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head : return head
        cv= head.val
        cp = head
        parent=head
        while cp is not None:
            cp = cp.next
            if cp is None:
                parent.next = None
            elif cp.val!=cv:
                parent.next = cp
                parent=parent.next
                cv = cp.val
        return head
