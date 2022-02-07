class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None: return list2
        if list2 == None: return list1
        head = None
        start = None
        while list1 or list2:
            # print(1)
            if list1 and list2:
                if list1.val <= list2.val:
                    if head:
                        head.next = ListNode(list1.val)
                        head = head.next
                    else:
                        head = ListNode(list1.val)
                        start = head
                    list1 = list1.next
                    
                else:
                    if head:
                        head.next = ListNode(list2.val)
                        head = head.next
                    else:
                        head = ListNode(list2.val)
                        start = head
                    list2 = list2.next
            elif list1 and not list2:
                head.next = list1
                # print("here1")
                return start
            elif list2 and not list1:
                # print("here2")
                head.next = list2
                return start
        return start
