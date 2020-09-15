'''
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
'''
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if head.next is None: return head.val
        
        val=0
        count=0
        temp=head
        while(temp is not None):
            count+=1
            temp=temp.next

        count=2**(count-1)
        while(head is not None):
            val+=(head.val*count)
            count//=2
            head=head.next
        return val
