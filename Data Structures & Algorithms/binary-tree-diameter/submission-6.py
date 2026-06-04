# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = 0
        def height(ptr: Optional[TreeNode]):
            nonlocal max_d
            if not ptr:
                return -1
            lt_ht = 1 + height(ptr.left)
            rt_ht = 1 + height(ptr.right)
            max_d = max(max_d, lt_ht + rt_ht)
            return max(lt_ht, rt_ht)
        if not root:
            return 0
        height(root)
        return max_d
        