# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 리스트를 Height Balanced BST 로 변환하는 문제

        if not nums:
            return None

        value = len(nums)// 2
        node = TreeNode(nums[value])
        node.left = self.sortedArrayToBST(nums[:value])
        node.right = self.sortedArrayToBST(nums[value + 1:])

        return node