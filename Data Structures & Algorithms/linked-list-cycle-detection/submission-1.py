# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dict1 = {}
        while head:
            if head in dict1:
                return True
            dict1[head] = head.val
            head = head.next
        return False
        