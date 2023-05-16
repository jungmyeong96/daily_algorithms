# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #재귀적으로 리프까지 타고들어감
        def check(root):
            if not root:
                return 0
        
            left = check(root.left)
            right = check(root.right)
            
            # -1은 1이상 차이가 난 경우 
            if left == -1 or \
                right == -1 or \
                abs(left - right) > 1:
                return - 1
            return max(left, right) + 1
        return check(root) != -1
            