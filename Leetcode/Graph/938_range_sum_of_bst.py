# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        #DFS를 사용한 부르트포스 알고리즘
        # if not root:
        #     return 0
        
        # return (root.val if low <= root.val <= high else 0) + \
        #     self.rangeSumBST(root.left, low, high) + \
        #     self.rangeSumBST(root.right, low, high)

        # DFS 가지치기로 필요한 노드 탐색하기

        # def dfs(node: TreeNode):
        #     if not node:
        #         return 0
        #     if node.val < low:
        #         return dfs(node.right)
        #     elif node.val > high:
        #         return dfs(node.left)
        #     return node.val + dfs(node.left) +dfs(node.right) #요 아이디어가 진짜 대박
    
        # return dfs(root)

        # 반복 구조로  DFS로 필요한 노드 탐색
        # stack, sum = [root], 0
        # #스택을 사용해서 노드 DFS반복하기
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         if node.val > low:
        #             stack.append(node.left)
        #         if node.val < high:
        #             stack.append(node.right)
        #         if low <= node.val <= high:
        #             sum += node.val
        # return sum

        #반복 구조로 BFS 사용
        queue, sum = [root], 0
        while queue:
            node = queue.pop(0)
            if node:
                if node.val > low:
                    queue.append(node.left)
                if node.val < high:
                    queue.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum