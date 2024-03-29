class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

longest: int = 0

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    def dfs(node: TreeNode) -> int:
        if not node:
            return -1
        # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
        left = dfs(node.left)
        right = dfs(node.right)

        #가장 긴 경로 (왼, 오)
        longest = max(longest, left + right + 2)
        #상태값
        return max(left, right) + 1
    
    dfs(root)
    return longest