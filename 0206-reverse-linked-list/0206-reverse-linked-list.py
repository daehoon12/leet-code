# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, node: Optional[ListNode], prev: Optional[ListNode]):
        if node == None:
            return prev

        _next = node.next
        node.next = prev
        return self.reverse(_next, node)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head, None)