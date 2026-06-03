# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def calcHeight(self, ptr: Option[TreeNode]):
        if not ptr:
            return (0, True)
        lt_ht, stat1 = self.calcHeight(ptr.left)
        rt_ht, stat2 = self.calcHeight(ptr.right)
        if not stat1 or not stat2:
            return (0, False)
        return (
            1 + max(lt_ht, rt_ht), 
            stat1 and stat2 and abs(lt_ht - rt_ht) <= 1
        )
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.calcHeight(root)[1]
        
        