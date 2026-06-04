# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_d = 0
    def height(self, ptr: Optional[TreeNode]):
        if not root:
            return 0
        lt_ht = 1 + self.height(ptr.left) if ptr else 1
        rt_ht = 1 + self.height(ptr.right) if ptr else 1
        return max(lt_ht, rt_ht)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)

        lt_ht = self.height(root.left)
        rt_ht = self.height(root.right)
        self.max_d = max(self.max_d, abs(lt_ht + rt_ht - 2))
        return self.max_d
        