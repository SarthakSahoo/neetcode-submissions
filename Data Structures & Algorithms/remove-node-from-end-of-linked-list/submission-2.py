# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        ptr = head

        while ptr:
            arr.append(ptr.val)
            ptr = ptr.next
        
        removed = arr.pop(len(arr) - n)
        
        prev, head = None, None

        for i in range(len(arr)):
            if not head:
                head = ListNode(val=arr[i])
                prev = head
            else:
                temp = ListNode(val=arr[i])
                prev.next = temp
                prev = temp

        return head