# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def in_order(ptr, res):
            if not ptr:
                return
            in_order(ptr.left, res)
            res.append(ptr.val)
            in_order(ptr.right, res)
        res = []
        in_order(root, res)
        return res[k - 1]
