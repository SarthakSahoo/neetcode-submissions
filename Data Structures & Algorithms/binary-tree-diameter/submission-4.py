# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_d = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(ptr: Optional[TreeNode]):
            if not ptr:
                return 0
            lt_ht = 1 + height(ptr.left)
            rt_ht = 1 + height(ptr.right)
            self.max_d = max(self.max_d, abs(lt_ht + rt_ht - 2))
            return max(lt_ht, rt_ht)
        if not root:
            return 0
        height(root)
        return self.max_d
        