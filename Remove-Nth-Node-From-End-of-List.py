'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count=0
        temp=head
        while(temp != None):
            count+=1
            temp=temp.next
        
        curr=0
        temp=head
        if(count<n):
            return head
        if head.next==None:
            return None
                
        else:
            if(n==count):
                return head.next
            
            while(curr<(count-n-1)):
                temp=temp.next
                curr+=1

            temp.next=temp.next.next
                
        return head
