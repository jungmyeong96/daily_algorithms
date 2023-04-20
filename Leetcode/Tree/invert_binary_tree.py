# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    #1. 파이썬 풀이
    # if root:
    #     root.left, root.right = \
    #     invertTree(root.right), invertTree(root.left)
    #     return root
    # return None # 생략가능 

    #2. BFS
    # queue = collections.deque([root])

    # while queue:
    #     node = queue.popleft()
    #     if node:
    #         node.left, node.right = node.right, node.left

    #         queue.append(node.left)
    #         queue.append(node.right)
    # return root

    #3. DFS 전위순회
    # stack = collections.deque([root])

    # while stack:
    #     node = stack.pop()
    #     if node:
    #         node.left, node.right = node.right, node.left

    #         stack.append(node.left)
    #         stack.append(node.right)
    # return root

    #4. DFS 후위순회
    stack = collections.deque([root])

    while stack:
        node = stack.pop()
        if node:
            stack.append(node.left)
            stack.append(node.right)

            node.left, node.right = node.right, node.left
    return root