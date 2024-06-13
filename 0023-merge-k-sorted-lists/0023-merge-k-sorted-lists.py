# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, [l.val, i, l])
    
        root = answer = ListNode(None)
        print(root)

        while heap:
            curr_element = heapq.heappop(heap)
            idx = curr_element[1]
            answer.next = curr_element[2]
            answer = answer.next
            
            if answer.next:
                heapq.heappush(heap, [answer.next.val, idx, answer.next])
        return root.next