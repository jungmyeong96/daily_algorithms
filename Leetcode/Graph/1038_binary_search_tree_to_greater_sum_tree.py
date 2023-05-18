# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val: int = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 오른쪽 기준 중위순회 방법으로 풀기 클 경우에만 값을 더하고 최종값을 root의 값으로 박제!
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)
        return root
å