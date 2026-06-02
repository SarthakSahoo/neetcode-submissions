# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev, curr, new = None, head, head.next
        while curr:
            curr.next = prev
            prev, curr = curr, new
            if new:
                new = new.next
        return prev

