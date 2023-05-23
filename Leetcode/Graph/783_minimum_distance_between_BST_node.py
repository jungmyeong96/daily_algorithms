# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #1. 재귀 방식
    # prev = -sys.maxsize
    # result = sys.maxsize

    # #재귀 구조로 중위순회 
    # def minDiffInBST(self, root: Optional[TreeNode]) -> int:
    #     if root.left:
    #         self.minDiffInBST(root.left) #전
        
    #     self.result = min(self.result, root.val - self.prev) # 중
    #     self.prev = root.val
    
    #     if root.right:
    #         self.minDiffInBST(root.right) # 후
        
    #     return self.result

    #2. 반복 방식
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = -sys.maxsize
        result = sys.maxsize

        stack = []
        node = root

        #반복구조로 중위 순회
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()

            result = min(result, node.val - prev)
            prev = node.val

            node = node.right
        
        return result