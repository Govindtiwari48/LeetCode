class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # Return head if the list is empty or has only one node
        
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head
        
        while curr and curr.next:
            # Nodes to be swapped
            first, second = curr, curr.next
            
            # Swapping
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Update prev and curr for the next iteration
            prev = first
            curr = first.next
        
        return dummy.next  # Return the new head (after swapping)
