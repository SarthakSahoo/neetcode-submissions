# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self, ptr1: Optional[TreeNode], ptr2: Optional[TreeNode]):
        print(ptr1.val if ptr1 else None, ptr2.val if ptr2 else None)
        if not ptr1 and not ptr2:
            return True
        elif not ptr1 or not ptr2:
            return False
        elif ptr1.val != ptr2.val:
            return False
        return self.check(ptr1.left, ptr2.left) and self.check(ptr1.right, ptr2.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        val = False
        if not subRoot:
            return True
        if not root and subRoot:
            return False
        if root.val == subRoot.val:
            val = self.check(root, subRoot)
        return val or self.isSubtree(root.left, subRoot) or \
        self.isSubtree(root.right, subRoot)