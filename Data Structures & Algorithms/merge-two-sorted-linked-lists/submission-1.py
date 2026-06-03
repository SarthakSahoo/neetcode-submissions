# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        if not list1:
            return list2
        else:
            ptr1, ptr2 = list1, list2
            dummy = ListNode(0, None)
            tail = dummy
            while ptr1 and ptr2:
                if ptr1.val <= ptr2.val:
                    tail.next = ptr1
                    ptr1 = ptr1.next
                    tail = tail.next
                else:
                    tail.next = ptr2
                    ptr2 = ptr2.next
                    tail = tail.next
            if ptr1:
                tail.next = ptr1
            if ptr2:
                tail.next = ptr2
            return dummy.next
                