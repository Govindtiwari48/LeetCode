# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=head
        temp=head
        f=head.next
        n=0
        while(temp):
            n=n+1
            temp=temp.next
        while(f and f.next):
            s=s.next
            f=f.next.next
        if(n%2==0):
            return (s.next)
        return (s)
        