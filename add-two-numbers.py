'''
https://leetcode.com/problems/add-two-numbers/
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s=0
        carry=0
        count=1
        while( l1 is not None or l2 is not None):
            s=carry
            if l1 is not None:
                s+=l1.val
                l1=l1.next
            if l2 is not None:
                s+=l2.val
                l2=l2.next
            
            temp=ListNode(s%10)
            carry=s//10
            
            if count==1:
                k=temp
                head=k
                if l1 is None and l2 is None:
                    if carry>0:
                        temp=ListNode(1)
                        k.next=temp
                        return head
            else:
                k.next=temp
                k=k.next
                
                if l1 is None and l2 is None:
                    if carry>0:
                        temp=ListNode(1)
                        k.next=temp
                        return head
    
            count+=1
        return head
