# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        
        prev_group = dummy
        
        while True:
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    break
                    
            if not kth:
                break

            old_head = prev_group.next

            prev = None
            curr = prev_group.next
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            old_head.next = curr
            prev_group.next = prev

            prev_group = old_head
            
        return dummy.next