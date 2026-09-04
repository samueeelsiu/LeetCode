# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        min_heap = []
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i, lists[i]))

        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        return dummy.next