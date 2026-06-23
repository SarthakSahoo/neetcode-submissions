# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        res = root.val

        def in_order(ptr):
            nonlocal count, res
            if not ptr:
                return
            in_order(ptr.left)
            if count == 0:
                return
            count -= 1
            if count == 0:
                res = ptr.val
                return
            in_order(ptr.right)

        in_order(root)
        return res
